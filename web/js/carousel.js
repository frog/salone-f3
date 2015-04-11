var React = require('react'),
    moment = require('moment-timezone');

var isBrowser = !(global && Object.prototype.toString.call(global.process) === '[object process]');
if (isBrowser) {
    var Chart = require('chart.js'),
        reqwest = require('reqwest'),
        io = require('socket.io-client');

    var socket = io();
    socket.on('update', function (data) {
        console.log(data);
    });
}

var VizOne = React.createClass({
    displayName: 'VizOne',
    fetchData: function () {
        reqwest({
            url: '/spreads'
            , type: 'json'
            , error: function (err) {
                console.log("WHAT?")
            }
            , success: function (resp) {
                var count = resp.reduce(function (count, currentItem) {
                    if (currentItem.fiction) count += currentItem.fiction;
                    if (currentItem.fact) count += currentItem.fact;
                    return count;
                }, 0)
                this.setState({votes: count});
                //console.log(resp)
            }.bind(this)
        });
    },

    render: function () {
        return (
            <div className="vizOne viz">
                <div className="counter">
                    <p className="title">Total votes collected</p>
                    <p className="number">{this.state.votes}</p>
                </div>
                <div className="flow">
                    <p className="title">Flow of voting</p>
                    <div className="chart">
                        <VoteFlowChart />
                    </div>
                    <VoteFlowLabels />
                </div>
            </div>
        );
    },
    getInitialState: function () {
        return {votes: 0};
    },
    componentDidMount: function () {
        this.fetchData();
        socket.on('update', function (data) {
            //fect data again on update
            this.fetchData();
        }.bind(this));
    }
});

var VoteFlowChart = React.createClass({
    displayName: 'VoteFlowChart',


    fetchData: function () {
        reqwest({
            url: '/votes'
            , type: 'json'
            , error: function (err) {
                console.log("WHAT?")
            }
            , success: function (resp) {
                var parsed = resp.map(function (a) {
                    var inbound = moment(a.tstamp);
                    var result = moment();
                    result.hours(inbound.hours());
                    result.minutes(inbound.minutes());
                    result.seconds(inbound.seconds());
                    //console.log("res ",result);
                    return result;
                });
                var limits = [];
                var startPoint = moment();
                startPoint.hours(18).minutes(0).seconds(0)
                var endPoint = moment();
                endPoint.hours(23).minutes(0).seconds(0)
                var cursor = moment(startPoint);
                while (cursor.isBefore(endPoint)) {
                    limits.push({
                        startTime: moment(cursor),
                        count: 0
                    });
                    cursor.add({minutes: 10});
                }

                parsed.forEach(function (element) {
                    limits.forEach(function (el, idx) {
                        var end = idx >= limits.length - 1 ? endPoint : limits[idx + 1].startTime;
                        //console.log(element, el.startTime, end);
                        if (element.isBetween(el.startTime, end)) {
                            el.count++;
                        }
                    });
                });
                console.log("parsed", parsed.map(function (e) {
                    return e.format("HH:mm:ss")
                }));
                console.log("limits", limits.map(function (e) {
                    return e.startTime.format("HH:mm:ss") + e.count
                }));

                this.setState({
                    points: limits.map(function (e) {
                        return e.count
                    })
                });
                this.createChart();
            }.bind(this)
        });
    },

    createChart: function () {
        var node = this.getDOMNode();
        var ctx = node.getContext("2d");
        var points = this.state.points;
        var data = {
            labels: new Array(points.length),
            datasets: [
                {
                    fillColor: "white",
                    data: points
                }
            ]
        };
        if (this.theChart) this.theChart.destroy();
        this.theChart = new Chart(ctx).Line(data, {
            animation: false,
            bezierCurve: false,
            pointDot: false,
            responsive: true,
            maintainAspectRatio: false,
            showScale: false,
            scaleOverride: true,
            scaleSteps: 150,
            scaleStepWidth: 1,
            scaleStartValue: 0
        });
    },
    render: function () {
        return (
            <canvas></canvas>
        );
    },
    componentDidMount: function () {
        this.fetchData();
        socket.on('updateTstamp', function (data) {
            //fect data again on update
            this.fetchData();
        }.bind(this));
    }
});

var VoteFlowLabels = React.createClass({
    displayName: 'VoteFlowLabels',

    render: function () {
        var hours = [18, 19, 20, 21, 22, 23];
        var nodes = hours.map(function (h) {
            return (
                <span className="label">h.{h}</span>
            );
        });
        return (
            <div className="voteFlowLabels">{nodes}</div>
        );
    }
});

var TweetDisplay = React.createClass({
    getInitialState: function () {
        return {tweet: this.props.tweet};
    },
    render: function () {
        var str = this.state.tweet.text;
        str = str.replace(/(\#[a-zA-Z0-9\-\_]+)/g, '<span class="greenHashtag">$1</span>');
        return (
            <div className="viz two" ref="twitter">
                <p className="title" style={{paddingTop: 26 + 'px'}}>Factorfiction tweet</p>
                <p className="tweetText" dangerouslySetInnerHTML={{__html: str}}>
                </p>
            </div>
        );
    },
    componentDidMount: function () {
        socket.on('newTweet', function (data) {
            this.setState({tweet: data});
        }.bind(this));
    }
});

var Carousel = React.createClass({

    displayName: 'Carousel',

    getInitialState: function () {
        return {currentIdx: 1, dir: 'right'}
    },

    render: function () {
        return (
            <div className="carousel">
                <TweetDisplay ref="twitter" tweet={this.props.tweet}/>
                <VizOne ref="chart"/>
                <div className="viz three" ref="single"/>
            </div>
        );
    },
    componentDidMount: function () {
        var components = [
            React.findDOMNode(this.refs.twitter),
            React.findDOMNode(this.refs.chart),
            React.findDOMNode(this.refs.single)
        ];
        var state = this.state;
        console.log('componentDidMount -> state', state);
        setInterval(function () {
            if (state.dir === 'right') {
                components[state.currentIdx].style.left = '-100%';
                state.currentIdx++;
                components[state.currentIdx].style.left = '0';
                if (state.currentIdx == 2) {
                    state.dir = 'left';
                }
            } else {
                components[state.currentIdx].style.left = '100%';
                state.currentIdx--;
                components[state.currentIdx].style.left = '0';
                if (state.currentIdx == 0) {
                    state.dir = 'right';
                }

            }
        }, 5000);
    }
});

module.exports.ViewClass = Carousel