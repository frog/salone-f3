var React = require('react');
var io = require('socket.io-client')

var socket = io();

socket.on('update', function (data) {
    console.log(data);
    document.getElementById("console").innerHTML += "<p>Received!"+JSON.stringify(data)+"</p>"
});

var VizOne = React.createClass({displayName: 'VizOne',
    render: function() {
        return (
            <div className="vizOne viz">
                <div className="counter">
                    <p className="title">Total votes collected</p>
                    <p className="number">3</p>
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
    }
});

var Chart = require('chart.js');
var VoteFlowChart = React.createClass({displayName: 'VoteFlowChart',
    render: function() {
        return (
            <canvas></canvas>
        );
    },
    componentDidMount : function() {
        var node =  React.findDOMNode(this);
        var ctx = node.getContext("2d");
        var hours = 5;
        var everyMinutes = 10;
        var data = {
            labels: new Array(hours * 60 / everyMinutes),
            datasets: [
                {
                    fillColor: "white",
                    data: [65, 59, 90,40,15]
                }
            ]
        };
        this.theChart = new Chart(ctx).Line(data, {
            animation: false,
            bezierCurve:false,
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
var VoteFlowLabels = React.createClass({displayName: 'VoteFlowLabels',

    render: function() {
        var hours = [18, 19, 20, 21, 22, 23];
        var nodes = hours.map(function(h) {
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
