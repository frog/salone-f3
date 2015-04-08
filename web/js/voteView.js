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
            var className = 'team boxed-grey';
            var voteArea = (
                <div>
                    <button onClick={parentElement.handleClick.bind(parentElement, elem.spreadId, 'Fact')}>FACT</button>
                    <button onClick={parentElement.handleClick.bind(parentElement, elem.spreadId, 'Fiction')}>FICTION</button>
                </div>
            );
            if (votedIdsFact.indexOf(elem.spreadId) >= 0) {
                className += " votatofact";
                voteArea = <p> VOTED FACT </p>
            }
            if (votedIdsFiction.indexOf(elem.spreadId) >= 0) {
                className += " votatofiction";
                voteArea = <p> VOTED FICTION </p>
            }

            var spreadTitleImg = "/hpstatic/img/spreadTitles/"+elem.spreadId+".png";
            //console.log("el ",elem);
            if (elem.tags && elem.tags.length > 0) {
                var categoryId = elem.tags[0];
                var categoryTitleImg = "/hpstatic/img/categories/" + categoryId + ".png";
            }

            return (
                <div className={className}>
                    <img src="/hpstatic/img/fact-voted.png" width="50%" className="bollinofact bollino" alt="Fact"/>
                    <img src="/hpstatic/img/fiction-voted.png" width="50%" className="bollinofiction bollino" alt="Fact"/>
                    <img src={categoryTitleImg} width="70%" className="categoria" alt={categoryId}/>
                    <img src={spreadTitleImg} className="headline" width="100%"/>
                    <hr/>
                    <p>{elem.text}</p>
                    <div className="votingbuttons">
                        <button type="button" className="btn btn-circle btn-lg fact" onClick={parentElement.handleClick.bind(parentElement, elem.spreadId, 'Fact')}>
                            <h6>Fact</h6>
                        </button>
                        <button type="button" className="btn btn-circle btn-lg fiction" onClick={parentElement.handleClick.bind(parentElement, elem.spreadId, 'Fiction')}>
                            <h6>Fiction</h6>
                        </button>
                    </div>
                    <div className="sharebutton">
                        <a href="https://twitter.com/share?url=http://pinollo.com&via=hazam&text=eccomunque %23pino&related=myinteraction&dnt=true&counturl=http://realurl" target="_blank" type="button" className="btn share"><h6>Share on Twitter</h6></a>
                    </div>
                </div>
            )
        });

        var colsize = Math.ceil(rows.length / 4.0);
        var cols = [];

        for (var i = 0; i < 4; i++) {
            var nelem = Math.min(colsize, rows.length);
            cols[i] = rows.slice(0, nelem);
            rows =  rows.slice(nelem);
        }

        var the_cols = cols.map(function(a) {
            return (
                <div className="col-xs-12 col-sm-3 col-md-3">
                        {a}
                </div>
            );
        });



        return (
            <div className="container">
                <section id="voting">
                    <div class="row">
                        {the_cols}
                    </div>
                </section>
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