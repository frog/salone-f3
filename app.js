var express = require('express');
var http = require('http');
var socketio = require('socket.io');
var winston = require('winston');

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
    process.env.ENV = "PROD";
} else {
    logger.info("Starting up DEV");
    dbUrl = 'mongodb://localhost:27017/f3-production'
    process.env.ENV = "DEV";
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
    app.use(express.static(__dirname + '/public'));


    var server = http.Server(app);
    var io = socketio(server);

    var collection = db.collection('spreads');
    var votes = db.collection('votes');

    //make sure that the spreads database is correctly initialized
    seed(collection);

    app.get('/isAlive', function (request, response) {
        response.send('yes, I\'m alive. Really');
    });

    app.get('/spreads', function (req, res) {
        collection.find().toArray(function (err, docs) {
            sendJSON(res, 200, docs);
        });
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

        votes.insertOne({spreadId: spreadId, which: a_field, tstamp: new Date()}, function (err, r) {
            //no op
            if (err != null) {
                logger.error('error inserting vote!', err);
            } else {
                io.emit('updateTstamp');
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
        spreadId: "lastdriver",
        headline: 'Meet the man with the last drivers licence',
        text: "Meet Henry, the happy Londoner who was granted the last drivers licence before The Great Ban of Human Driving Act in 2021. Full story on page 6.",
        tags: ['mobility/transportation'],
        href: 'http://www.wired.com/2015/03/mercedes-benz-f-015-autonomous-car'
    },
    {
        spreadId: "truckstrike",
        headline: 'Truck drivers on strike (against self-driving trucks)',
        text: "Robo-commerce: self-driving trucks and drones will deliver anything wherever your are in a few hours. Representatives of local unions gathered in town hall for regional march against “modern profanities”.",
        tags: ['mobility/transportation'],
        href: 'http://www.bloomberg.com/news/articles/2014-12-09/self-driving-trucks-to-revolutionize-logistics-dhl-says'
    },
    {
        spreadId: "parismanhattan",
        headline: 'Paris > Manhattan - 1 hour!',
        text: "Europeans flock to French capital as Hyperloop Tube System is extended below the Atlantic for quick and safe travels to the US in less than an hour.",
        tags: ['mobility/transportation'],
        href: 'http://en.wikipedia.org/wiki/Hyperloop'
    },
    {
        spreadId: "declinemoon",
        headline: 'Decline in moon tourism',
        text: 'Richard Branson: "Let’s face it, the moon was cool in the 60s, now it’s just a dead lump in the sky, blocking the view".',
        tags: ['mobility/transportation'],
        href: 'http://www.futuretimeline.net/21stcentury/2035.htm#.VPhASlPF_QE'
    },
    {
        spreadId: "savedbydrones",
        headline: 'Saved by drones',
        text: "A drone swarm saved twelve people from drowning after a boat incident outside Sicily. The drone patrol quickly reached the location and saved the passengers by releasing inflating file rafts to the people in water.",
        tags: ['mobility/transportation'],
        href: 'http://www.gizmag.com/pars-life-saving-flying-robot/29831'
    },
    {
        spreadId: "venushorror",
        headline: 'Venus cloud city horror',
        text: 'Crew burns in sulphur as Genesis Aircraft loses control. "We need to review security protocol" says commander in chief.',
        tags: ['mobility/transportation'],
        href: 'http://www.popularmechanics.com/space/a13379/nasa-cloud-city-venus-colony-17549027'
    },
    {
        spreadId: "augmentedeyes",
        headline: 'Augmented eyes',
        text: 'Google announced their next generation contact lenses at SXSW2025 last month. Early adopters are already complaining of severe dependencies to the new technology. “Taking the lenses off is basically impossible as I don’t want to loose any of the new features”.',
        tags: ['healthcarenbodies'],
        href: 'http://www.dailymail.co.uk/news/article-2334257/Mission-Impossible-style-contact-lenses-pictures-scan-data-step-closer-reality-scientists-develop-LED-soft-lenses.html'
    },
    {
        spreadId: "mybodyac",
        headline: 'My body AC',
        text: '“Cool as a breeze”. Barcelona residents rejoice as a new system for administrating their own temperature is installed directly into their bodies.',
        tags: ['healthcarenbodies'],
        href: 'http://www.wired.com/2013/10/an-ingenious-wristband-that-keeps-your-body-at-the-perfect-temperature-no-ac-required'
    },
    {
        spreadId: "swalloweddoctor",
        headline: '“I SWALLOWED MY DOCTOR”',
        text: 'Brooklyn mother-of-five explains how her medical condition is monitored from inside her body.',
        tags: ['healthcarenbodies'],
        href: 'http://www.fastcoexist.com/3042782/4-crazy-predictions-for-the-future-of-health-care-human-augmentation-hacked-dna-and-more'
    },
    {
        spreadId: "elevatoradviced",
        headline: '“THE ELEVATOR ADVICED ME TO TAKE THE STAIRS”',
        text: 'American senior citizen was told to take the stairs while visiting a super mall in Germany. By the elevator. “The elevator read public data and offered a suggestion to improve the woman’s health”.',
        tags: ['healthcarenbodies'],
        href: 'http://www.pleasurabletroublemakers.com/intervator/'
    },
    {
        spreadId: "thirdeye",
        headline: 'My third eye',
        text: 'Meet the mother-of-four that installed a third eye in her neck for perfect 360 degree vision. “I can’t believe I lived without it before”.',
        tags: ['healthcarenbodies'],
        href: 'http://getnarrative.com/shop'
    },
    {
        spreadId: "livingtatoos",
        headline: 'Living tatoos',
        text: 'Smart digital tattoos are on the rise in Japan. Teenage groups are exploring new ideas by uploading images to their skin for a fresh appearance every day.',
        tags: ['healthcarenbodies'],
        href: 'http://www.fastcodesign.com/3036175/from-the-designers-of-fitbit-a-digital-tattoo-implanted-under-your-skin'
    },
    {
        spreadId: "headtransplant",
        headline: 'MAN GETS HEAD TRANSPLANT',
        text: 'Neighbours flock to get their know “new” acquaintance. Best friend laughs: “He definitely had an upgrade”.',
        tags: ['healthcarenbodies'],
        href: 'http://www.telegraph.co.uk/news/science/science-news/11436319/Frankenstein-style-human-head-transplant-could-happen-in-two-years.html'
    },
    {
        spreadId: "dumbhome",
        headline: '“I WANT MY DUMB HOME BACK”',
        text: 'Man in a pub: “I dream of a day when I can just have a beer, mow the lawn and avoid awkward, cold conversations with my Scandinavian furniture”',
        tags: ['smarthome'],
        href: 'http://qz.com/324267/smart-furniture-multi-touch-screens-and-parametric-modeling-are-the-future-of-interior-design/'
    },
    {
        spreadId: "nocoffee",
        headline: 'No coffee for you!',
        text: 'Copenhagen. A smart, privately owned coffee machine refused to serve an ill owner her morning coffee, as the system perceived it as dangerous for her health. “If I need this type of advice I go to the doctor, thank you very much” the woman wrote in an open letter to the manufacturer.',
        tags: ['smarthome'],
        href: 'http://www.engadget.com/2015/01/02/smarter-wifi-coffee-machine/'
    },
    {
        spreadId: "fritz",
        headline: 'FRITZ - OUR ROBOT BUTLER',
        text: 'As families struggle to find the perfect support around the house, miniaturised mechanics is paving the way for embedded intelligence and robot assistants. Meet the family that purchase their own robot butlers to provide help to questions, facilitate communication with family and friends, carry heavy loads and shopping (inside and outside the home).',
        tags: ['smarthome'],
        href: 'http://www.technocrazed.com/romeo-an-intelligent-french-robot-to-help-elderly-with-daily-tasks'
    },
    {
        spreadId: "education",
        headline: 'KIDS CAN’T WRITE',
        text: 'Disaster as Finish Government presents school results just eight years after decision to stop teaching handwriting is taken. “It’s true our kids can’t write with their hands but our PISA results speak for themselves” says Head of Education.',
        tags: ['education'],
        href: 'http://www.bbc.com/news/blogs-news-from-elsewhere-30146160'
    },
    {
        spreadId: "grannies",
        headline: 'Skype grannies',
        text: 'Villages in remote parts of Africa get free English lessons from elderly in Europe and the US. “It’s lovely. We enjoy the company." says Cornwall based great-grandmother who dials in Nairobi every Tuesday and Thursday.',
        tags: ['education'],
        href: 'http://www.ncl.ac.uk/solecentral/join/granny/'
    },
    {
        spreadId: "lifelong",
        headline: 'LIFELONG LEARNING',
        text: 'Leading US Universities are announcing new degree programmes this summer. The new curriculums - designed to last for the full duration of a persons life – are distributed as one-month “sabbaticals” across the lifespan of a student. Head Principal: “It seems absurd to suggest that subjects learned while being a young teenager should dictate ones life forever”',
        tags: ['education'],
        href: 'http://www.ted.com/talks/sir_ken_robinson_bring_on_the_revolution'
    },
    {
        spreadId: "cashnotaccepted",
        headline: 'CASH NOT ACCEPTED',
        text: 'Confusion among tourists as Sweden removes all bills and coins from circulation.',
        tags: ['banking'],
        href: 'http://www.theguardian.com/world/2014/nov/11/welcome-sweden-electronic-money-not-so-funny'
    },
    {
        spreadId: "bitcoinwipesout",
        headline: 'BITCOIN WIPES OUT THE DOLLAR',
        text: 'Bitcoin surpasses the dollar as top currency for investment in the US. Elderly abandon traditional banks to secure their pensions.',
        tags: ['banking'],
        href: 'http://www.inc.com/christine-lagorio/fred-wilson-bitcoin-predictions.html'
    },
    {
        spreadId: "3dbabies",
        headline: '3D PRINTED BABIES',
        text: 'Outrage as NASA announces genetically designed babies for future space missions.',
        tags: ['misc'],
        href: 'http://www.dezeen.com/2015/03/06/will-i-am-interview-future-3d-printing-people/'
    },
    {
        spreadId: "manabandons",
        headline: 'MAN ABANDONS LIFE FOR VIRTUAL REALITY',
        text: 'Detroit resident decides to dedicate 100% of his time to his virtual life. “Let’s face it - real life stinks”.',
        tags: ['misc'],
        href: 'http://www.scienceclarified.com/scitech/Virtual-Reality/Which-World-Is-Real-The-Future-of-Virtual-Reality.html'
    },
    {
        spreadId: "fashionfury",
        headline: 'FASHION FURY: THE DREADED RETURN OF THE KHAKI',
        text: 'GAP-styled chinos are set for a comeback as Brooklyn fashion collectives are distributing Earth fashion to other planets. “Aliens won’t understand the irony” claims young fashion students at Central Saint Martins in London.',
        tags: ['misc'],
        href: 'http://en.wikipedia.org/wiki/Her_%28film%29'
    },
    {
        spreadId: "genderspasse",
        headline: 'GENDERS ABOLISHED',
        text: 'Public outcry in Scaninavia as men and women cannot be publicly distinguished using pronouns like “him” or “her”. Teenagers: “Genders are passé”.',
        tags: ['misc'],
        href: 'http://en.wikipedia.org/wiki/Hen_%28pronoun%29'
    },
    {
        spreadId: "forgiveme",
        headline: 'FORGIVE ME FATHER FOR I HAVE SINNED',
        text: 'New faith, in technology. Thousands joins AI-based religious cult founded by a robotic priest.',
        tags: ['misc'],
        href: 'http://www.salon.com/2014/09/14/what_robot_theology_tells_us_about_ourselves_partner/'
    },
    {
        spreadId: "mutantolympics",
        headline: 'MUTANT OLYMPICS',
        text: 'Join us for the launch of the first ever Mutant Olympics held between locations on Earth and the Moon in 2026. All chemicals allowed; record-breaking and time-trimming guaranteed!',
        tags: ['misc'],
        href: 'http://www.nytimes.com/2008/08/12/science/12tier.html?_r=0'
    },
    {
        spreadId: "massextinction",
        headline: 'MASS EXTINCTION : DISASTER AS EARTH HITS RESET',
        text: 'Multiple species are disappearing from the face of the Earth every year. “Project Ark” gathers millions of genetic samples to let extinct creatures roam our planet in the future.',
        tags: ['misc'],
        href: 'http://www.livescience.com/8557-mass-extinction-threat-earth-verge-huge-reset-button.html'
    }
];