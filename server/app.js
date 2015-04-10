var express = require('express');
var http = require('http');
var socketio = require('socket.io');
var winston = require('winston');
var async = require('async');
var session = require('express-session');
var MongoStore = require('connect-mongo')(session);
var React = require('react');
var Twitter = require('twitter');

//set up logger
var logger = new winston.Logger({
    transports: [
        new (winston.transports.Console)(),
        new (winston.transports.File)({filename: 'server.log'})
    ]
});


//set up db connection
var mongo = require('mongodb').MongoClient;
var dbUrl = process.env.MONGO_URL;
if (dbUrl) {
    logger.info("Starting up PRODUCTION");
    process.env.NODE_ENV = "PROD";
} else {
    logger.info("Starting up DEV");
    dbUrl = 'mongodb://localhost:27017/f3-production'
    process.env.NODE_ENV = "DEV";
}


logger.info("Connecting to ... " + dbUrl);
var PORT = 5000;
mongo.connect(dbUrl, function (err, db) {
    if (err) {
        logger.error("ERROR in connect", err);
        throw err;
    }

    //create Express app on port 5000
    var app = express();
    app.set('port', PORT);
    app.use(express.static(__dirname + '/../public'));

    app.use(session({
        store: new MongoStore({db: db}),
        secret: 'keyboard cat'
    }));

    app.use(function (req, res, next) {
        if (req.session.votedIdsFact == undefined) req.session.votedIdsFact = [];
        if (req.session.votedIdsFiction == undefined) req.session.votedIdsFiction = [];
        next()
    });

    app.set('view engine', 'ejs');
    require("node-jsx").install();

    var server = http.Server(app);
    var io = socketio(server);

    var collection = db.collection('spreads');
    var votes = db.collection('votes');

    var allowedFields = ['fact', 'fiction'];

    //make sure that the spreads database is correctly initialized
    seed(collection);

    app.get('/isAlive', function (request, response) {
        console.log("SESSION ", request.session);
        //request.session.pino = "YES"
        response.send('yes, I\'m alive. Really' + JSON.stringify(request.session));
    });

    app.get('/spreads', function (req, res) {
        collection.find().toArray(function (err, docs) {
            sendJSON(res, 200, docs);
        });
    });

    app.get('/votes', function (req, res) {
        votes.find().toArray(function (err, docs) {
            sendJSON(res, 200, docs);
        });
    });


    app.get('/voteFiction/:spreadId', function (req, res) {
        var spreadId = req.param('spreadId');
        if (req.session.votedIdsFiction.indexOf(spreadId) < 0) {
            req.session.votedIdsFiction.push(spreadId);
            logger.info('FICTION vote for ' + spreadId);
            incrementVoteFor(spreadId, 'fiction',
                function () {
                    sendJSONMessage(res, 200, 'Fiction vote registered! Thanks');
                });
        } else {
            sendJSONMessage(res, 418, 'A teapot');
        }
    });

    app.get('/voteFact/:spreadId', function (req, res) {
        var spreadId = req.param('spreadId');
        if (req.session.votedIdsFact.indexOf(spreadId) < 0) {
            req.session.votedIdsFact.push(spreadId);
            logger.info('FACT vote for ' + spreadId);
            incrementVoteFor(spreadId, 'fact',
                function () {
                    sendJSONMessage(res, 200, 'Fact vote registered! Thanks');
                });
        } else {
            sendJSONMessage(res, 418, 'A teapot');
        }
    });

    function incrementVoteFor(spreadId, a_field, cb, date) {
        if (allowedFields.indexOf(a_field) < 0) throw new Error("unknown field: " + a_field);
        var increment = {};
        increment[a_field] = 1;

        var query = {"spreadId": spreadId};
        collection.findOneAndUpdate(query,
            {'$inc': increment},
            {
                returnOriginal: false,
                upsert: true
            },
            function (err, result) {
                if (!err) {
                    // at every update of the db, we send out a websocket
                    // packet out
                    collection.findOne(query, {}, function (err, result) {
                        console.dir(result);
                        logger.info('sending', result);
                        io.emit('update', result);
                    });
                }
                cb(err, result);
            });

        if (!date) date = new Date();

        var new_vote = {spreadId: spreadId, which: a_field, tstamp: date};
        votes.insertOne(new_vote, function (err, r) {
            //no op
            if (err != null) {
                logger.error('error inserting vote!', err);
            } else {
                io.emit('updateTstamp', new_vote);

            }
        });
    }

    function sendJSON(res, status, content) {
        res.set('Content-Type', 'application/json');
        res.status(status).send(content);
    }

    function sendJSONMessage(res, the_status, the_message) {
        return sendJSON(res, the_status, {status: the_status, message: the_message})
    }

    //
    // WEB ENDPOINTS
    //
    app.get('/vizone', function (req, res) {

        collection.find().toArray(function (err, docs) {
            var viewFile = "carousel";
            var Carousel = React.createFactory(require('../web/js/' + viewFile).ViewClass);
            //console.log(docs[0])
            var startingProps = {
                spreads: docs,
                tweet: latestTweet
            };

            var reactHtml = React.renderToString(Carousel(startingProps))
            res.render('projection', {
                pageTitle: "Welcome",
                viewFile: viewFile,
                reactHtml: reactHtml,
                props: JSON.stringify(startingProps)
            });
        });
    });

    app.get('/', function (req, res) {
        collection.find().toArray(function (err, docs) {
            var viewFile = "voteView";
            var VoteView = React.createFactory(require('../web/js/' + viewFile).ViewClass);
            //console.log(docs[0])
            var startingProps = {
                spreads: docs,
                votedIdsFact: req.session.votedIdsFact ? req.session.votedIdsFact : [],
                votedIdsFiction: req.session.votedIdsFiction ? req.session.votedIdsFiction : []
            };
            var reactHtml = React.renderToString(VoteView(startingProps));
            res.render('index', {
                title: "Welcome",
                viewFile: viewFile,
                reactHtml: reactHtml,
                props: JSON.stringify(startingProps)
            });
        });
    });

    var gifs = {
        'one': 'tumblr_md8edt23e11qzt4vjo1_500.gif',
        'two': 'tumblr_mwmc51icCB1qzt4vjo1_500.gif',
        'three': 'tumblr_my81e4uj6M1qzt4vjo1_r1_500.gif',
        'four': 'tumblr_ncz5srzhGc1qzt4vjo1_500.gif',
        'five': 'tumblr_ngwwm7RKXD1qzt4vjo1_r2_500.gif',
        'six': 'tumblr_nidg6dE3lc1qzt4vjo1_500.gif',
        'seven': 'tumblr_nk2f8q1U8J1qzt4vjo1_r1_500.gif',
        'eight': 'tumblr_nlkkug2YwK1qzt4vjo1_r1_500.gif',
        'nine': 'tumblr_nme6a0GF8m1qzt4vjo1_500.gif'
    }

    app.get('/travellingwithoutmoving', function (req, res) {
        res.render('vizgif', {
            which: gifs[req.param('which')]
        });
    });

    if (process.env.NODE_ENV != "PROD") {
        app.get('/reseed', function (req, res) {
            seed(collection, true);
            res.status(200).send("WHOLE DB reseeded!");
        });
    }

    server.listen(app.get('port'), function () {
        logger.info('--> f3 server ready to rock on port:' + app.get('port') + process.env.NODE_ENV);
    });


    io.on('connection', function (socket) {
        logger.info('DataViz client connected');
        socket.on('disconnect', function () {
            logger.info('DataViz client disconnected');
        });
    });

    //setting up twitter
    var client = new Twitter({
        consumer_key: "7qCA2va8npELk1GLfpkOQ",
        consumer_secret: "vSeHlFYqOLtZrn7tOjGzfJvibbhdqGwH2Awyt8r64Q",
        access_token_key: "6989042-PYOdigebPjRLa6woacS0sC8JWgHYsrXEl15agGkFt2",
        access_token_secret: "b2uhlKMTvTKdJksIWsrssIavq1nj1ciEwosdFwNrZ9UPr"
    });

    var latestTweet = undefined;

    function retrieveTweet() {
        winston.info("retrieving twitter")
        client.get('search/tweets', {
            q: '#factorfiction',
            count: 1
        }, function (error, tweets, response) {
            if (tweets.statuses.length == 0) return;
            if (latestTweet == undefined || latestTweet.text !== tweets.statuses[0].text) {
                latestTweet = tweets.statuses[0];
                console.log("--> NEW TWEET");
                console.log(latestTweet.text);
                console.log("<-- END TWEET");
                io.emit('newTweet', latestTweet);
            } else {
                console.log("same tweet...");
            }
        });
    }

    retrieveTweet();
    setInterval(retrieveTweet, 20000);

    function seed(collection, reset) {
        logger.info("Seeding in data");
        function dropSpreads(cb) {
            collection.deleteMany({}, null, cb);
        }

        function dropVotes(cb) {
            votes.deleteMany({}, null, cb);
        }

        function insert(cb) {
            spreads.map(function (value, idx) {
                var query = {"spreadId": value.spreadId};
                collection.findOneAndUpdate(query,
                    {$set: value},
                    {
                        returnOriginal: false,
                        upsert: true
                    },
                    function (err, result) {
                        if (err) throw new Error("error in seeding", err);
                    });
            });
            if (reset && process.env.NODE_ENV != "PROD") {
                var moment = require('moment-timezone');
                var cursor = moment().tz("Europe/Rome").hours(18).minutes(2).seconds(0);

                function addNVotes(n, cursor) {
                    for (var i = 0; i < n; i++) {
                        incrementVoteFor('3dbabies', 'fact', function () {
                        }, cursor.toDate());
                    }
                }

                var votes = [25, 12, 45, 23, 56, 2, 5, 120];
                votes.map(function (a) {
                    addNVotes(a, cursor)
                    cursor.add({minutes: 10});
                });
            }
            cb(null, 'OK');
        }

        var funcs = [];

        if (reset == undefined) reset = false;
        if (reset) {
            funcs.push(dropSpreads);
            funcs.push(dropVotes);
        }
        funcs.push(insert);

        async.series(funcs, function (err, result) {
            logger.info("End Seeding!");
        });
    }

});
var fs = require('fs');
var spreads = JSON.parse(fs.readFileSync(__dirname + '/spreads.json', 'utf8'));

