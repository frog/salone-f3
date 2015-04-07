var React = require('react');
var io = require('socket.io-client');

var VoteView = React.createClass({
    displayName: 'VoteView',
    handleClick: function (spreadId, fof) {
        console.log("want to vote for", spreadId, fof);
        var parentElement = this;
        function checkSpreadAsVoted(spreadId, fof) {
            var attribName = "votedIds" + fof;
            var votedFact = parentElement.state[attribName];
            votedFact.push(spreadId);
            var delta = {};
            delta[attribName] = votedFact;
            parentElement.setState(delta);
        }

        function uncheckSpreadAsVoted(spreadId, fof) {
            var attribName = "votedIds" + fof;
            var votedFact = parentElement.state[attribName];
            var idx = votedFact.indexOf(spreadId);
            if (idx >= 0) {
                votedFact.splice(idx, 1);
                var delta = {};
                delta[attribName] = votedFact;
                parentElement.setState(delta);
            }
        }

        if (window !== undefined) {
            var reqwest = require('reqwest');
            //this.setState({});
            var the_url = '/vote' + fof + "/" + spreadId;
            console.log("about to vote " + the_url);
            //optimistically set as voted
            checkSpreadAsVoted(spreadId, fof);
            reqwest({
                url: the_url
                , type: 'json'
                , error: function (err) {
                    console.log("ERROR", err);
                    //418 is reserved for already voted
                    if (err.status != 418) {
                        uncheckSpreadAsVoted(spreadId, fof)
                    }
                }
                , success: function (resp) {
                    //don't to anything since optimistically set
                }.bind(this)
            });
        }
    },
    render: function () {
        console.log("render() called");
        //grabbing stuff from the state
        var spreads = this.state.spreads;
        var votedIdsFact = this.state.votedIdsFact;
        var votedIdsFiction = this.state.votedIdsFiction;

        var parentElement = this;

        //creating html for each of the spread
        var rows = spreads.map(function (elem) {

            //composing the class name
            var className = 'spread';
            var voteArea = (
                <div>
                    <button onClick={parentElement.handleClick.bind(parentElement, elem.spreadId, 'Fact')}>FACT</button>
                    <button onClick={parentElement.handleClick.bind(parentElement, elem.spreadId, 'Fiction')}>FICTION</button>
                </div>
            );
            if (votedIdsFact.indexOf(elem.spreadId) >= 0) {
                className += " voted votedFact";
                voteArea = <p> VOTED FACT </p>
            }
            if (votedIdsFiction.indexOf(elem.spreadId) >= 0) {
                className += " voted votedFiction";
                voteArea = <p> VOTED FICTION </p>
            }

            return (
                <div className={className}>
                    <p>{elem.spreadId}</p>
                    <p>{elem.headline}</p>
                    <p>{elem.text}</p>
                    {voteArea}
                </div>
            )
        });
        return (
            <div>
                {rows}
            </div>);
    },
    componentDidMount: function () {
        console.log("ComponentDidMount")
        var socket = io();
        socket.on('update', function (data) {
            console.log(data);
        });
    },
    getInitialState: function () {
        var state = {
            spreads: this.props.spreads ? this.props.spreads : [],
            votedIdsFact: this.props.votedIdsFact ? this.props.votedIdsFact : [],
            votedIdsFiction: this.props.votedIdsFiction ? this.props.votedIdsFiction : []
        };
        console.log("getInitialState() called");
        return state;
    }
});

module.exports.ViewClass = VoteView;