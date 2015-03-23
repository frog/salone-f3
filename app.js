var express = require('express');
var http = require('http');
var socketio = require('socket.io');
var winston = require('winston');
var logger = new winston.Logger({
    transports: [
        new (winston.transports.Console)(),
        new (winston.transports.File)({ filename: 'server.log' })
    ]
});


var MongoClient = require('mongodb').MongoClient,
    format = require('util').format;

var dbUrl = process.env.MONGO_URL;
if (dbUrl) {
    logger.info("Starting up PRODUCTION");
    process.env.ENV = "PROD";
} else {
    logger.info("Starting up DEV");
    dbUrl = 'mongodb://localhost:27017/f3-production'
    process.env.ENV = "DEV";
}
logger.info("Connecting to ... "+dbUrl);
MongoClient.connect(dbUrl, function (err, db) {
    if (err) {
        logger.error("ERROR in connect", err);
        throw err;
    }
    //connection to the database open, we can
    //we can use the var DB as closured


    //create Express app on port 5000
    var app = express();
    app.set('port', 5000);
    app.use(express.static(__dirname + '/public'));
    var server = http.Server(app);
    var io = socketio(server);

    var collection = db.collection('spreads');

    //make sure that the spreads database is correctly initialized
    seed(collection);

    app.get('/isAlive', function (request, response) {
        response.send('yes, I\'m alive. Really');
    });

    app.get('/voteFiction/:spreadId', function (req, res) {
        var spreadId = req.param('spreadId');
        logger.info('FICTION vote for ' + spreadId);
        incrementVoteFor(spreadId, 'fiction',
            function () {
                sendJSONMessage(res, 200, 'Fiction vote registered! Thanks');
            });
    });

    app.get('/voteFact/:spreadId', function (req, res) {
        var spreadId = req.param('spreadId');
        logger.info('FACT vote for ' + spreadId);
        incrementVoteFor(spreadId, 'fact',
            function () {
                sendJSONMessage(res, 200, 'Fact vote registered! Thanks');
            });
    });

    var allowedFields = ['fact', 'fiction'];

    function incrementVoteFor(spreadId, a_field, cb) {
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
                    collection.findOne(query, {}, function (err, result) {
                        console.dir(result);
                        logger.info('sending', result);
                        io.emit('update', result);
                    });
                }
                cb(err, result);
            });
    }

    function sendJSON(res, status, content) {
        res.set('Content-Type', 'application/json');
        res.status(status).send(content);
    }

    function sendJSONMessage(res, the_status, the_message) {
        return sendJSON(res, the_status, {status: the_status, message: the_message})
    }

    app.get('/spreads', function (req, res) {
        collection.find().toArray(function (err, docs) {
            sendJSON(res, 200, docs);
        });
    });


    server.listen(app.get('port'), function () {
        logger.info('--> f3 server ready to rock on port:' + app.get('port'))
    });


    io.on('connection', function (socket) {
        logger.info('DataViz client connected');
        socket.on('disconnect', function () {
            logger.info('DataViz client disconnected');
        });
    });
});


var seed = function (collection) {
    logger.info("Seeding in data");
    spreads.map(function (value, idx) {
        var query = {"spreadId": value.spreadId};
        collection.findOneAndUpdate(query,
            value,
            {
                returnOriginal: false,
                upsert: true
            },
            function (err, result) {
                if (err) throw new Error("error in seeding", err);
            });
    });
    logger.info("End Seeding");
};

var spreads = [
    {
        spreadId: "3dbabies",
        text: "in the future a lot of printed babies around.",
        tags: ['human', '3d', 'printing']
    },
    {
        spreadId: "3dbabies1",
        text: "in the future a lot of printed babies around.",
        tags: ['human', '3d', 'printing']
    },
    {
        spreadId: "3dbabies3",
        text: "in the future a lot of printed babies around.",
        tags: ['human', '3d', 'printing']
    }
];