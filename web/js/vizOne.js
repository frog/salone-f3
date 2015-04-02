var React = require('react');
var io = require('socket.io-client');
var Chart = require('chart.js');
var reqwest = require('reqwest');

var socket = io();

socket.on('update', function (data) {
    console.log(data);
});

var VizOne = React.createClass({
    displayName: 'VizOne',
    fetchData: function () {
        reqwest({
            url: '/spreads'
            , type: 'json'
            , method: 'get'
            , error: function (err) {
            }
            , success: function (resp) {
                var count = resp.reduce(function (count, currentItem) {
                    if (currentItem.fiction) count += currentItem.fiction;
                    if (currentItem.fact) count += currentItem.fact;
                    return count;
                }, 0)
                this.setState({votes: count});
                console.log(resp)
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
            this.fetchData();
        }.bind(this));
    }
});
var VoteFlowChart = React.createClass({
    displayName: 'VoteFlowChart',
    render: function () {
        return (
            <canvas></canvas>
        );
    },
    componentDidMount: function () {
        var node = React.findDOMNode(this);
        var ctx = node.getContext("2d");
        var hours = 5;
        var everyMinutes = 10;
        var data = {
            labels: new Array(hours * 60 / everyMinutes),
            datasets: [
                {
                    fillColor: "white",
                    data: [65, 59, 90, 40, 15]
                }
            ]
        };
        this.theChart = new Chart(ctx).Line(data, {
            animation: false,
            bezierCurve: false,
            pointDot: false,
            responsive: true,
            maintainAspectRatio: false,
            showScale: false,
            scaleOverride: true,

            // ** Required if scaleOverride is true **
            // Number - The number of steps in a hard coded scale
            scaleSteps: 100,
            // Number - The value jump in the hard coded scale
            scaleStepWidth: 1,
            // Number - The scale starting value
            scaleStartValue: 0
        });
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

React.render(
    <VizOne />,
    document.getElementById('content')
);