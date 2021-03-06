var React = require('react');
var io = require('socket.io-client');

var isBrowser = !(global && Object.prototype.toString.call(global.process) === '[object process]');

var TweetButton = require('./tweetbutton').ViewClass;

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

        if (isBrowser) {
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
            if (votedIdsFact.indexOf(elem.spreadId) >= 0) {
                className += " votatofact";
            } else if (votedIdsFiction.indexOf(elem.spreadId) >= 0) {
                className += " votatofiction";
            }

            var spreadTitleImg = "/hpstatic/img/spreadTitles/" + elem.spreadId + ".png";
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
                    <TweetButton spread={elem}/>
                </div>
            )
        });

        var colsize = Math.ceil(rows.length / 4.0);
        var cols = [];

        for (var i = 0; i < 4; i++) {
            var nelem = Math.min(colsize, rows.length);
            cols[i] = rows.slice(0, nelem);
            rows = rows.slice(nelem);
        }

        var the_cols = cols.map(function (a) {
            return (
                <div className="col-xs-12 col-sm-3 col-md-3">
                        {a}
                </div>
            );
        });


        return (
            <div className="container">
                <section id="intro" className="intro">
                    <a href="#voting" className="smoothScroll">
                        <img className="bannerBig" src="/hpstatic/img/cover.png" width="100%" alt="Vote Now"/>
                        <img className="bannerSmall" src="/hpstatic/img/cover_small.png" width="100%" alt="Vote Now"/>
                    </a>
                </section>
                <section id="about" className="text-center bg-gray">
                    <div className="container">
                        <div className="row">
                            <div className="col-md-6 blocktext">
                                <img src="/hpstatic/img/ten.png" width="50%" alt="frog turns 10"/>

                                <h3>Coinciding with the 54th Salone del Mobile, “Future Fact or Fiction” is an event hosted
                                    by frog that tackles aspirational themes just slightly out of reach for the 2015 edition
                                    of the world's largest furniture fair.</h3>

                                <div className="rsvpbutton">
                                    <a href="http://info2.frogdesign.com/future-fact-or-fiction" target="_blank"
                                        className="btn-lg" alt="frog">
                                        <img src="/hpstatic/img/friedolin_w.png" height="80" width="auto"/>
                                    </a>
                                </div>
                            </div>
                            <div className="vseparator"></div>
                            <div className="col-md-6 blocktext">

                                <img src="/hpstatic/img/registerhere.png" width="50%" alt="frog turns 10"/>

                                <h3>Please join us on April 14th as frog transforms its Milan studio for an immersive
                                    encounter with the technology-fuelled headlines of tomorrow - and explore what may become
                                    future factor or fiction together with panelists from IKEA, Empatica, and frog.
                                </h3>

                                <div className="rsvpbutton">
                                    <a href="http://info2.frogdesign.com/future-fact-or-fiction" target="_blank"
                                        className="btn-lg rsvp">
                                        <span>RSVP</span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                <div id="separatore">
                    <img src="/hpstatic/img/fact-or-fiction.png" alt="Fact or Fiction"/>
                    <p className="prompt">Give us your opinion on these fantastic future headlines</p>
                </div>
                <section id="voting">
                    <div className="row">
                        {the_cols}
                    </div>
                </section>

                <footer id="footer">
                    <div className="container">
                        <div className="row">
                            <div className="col-md-3 col-md-offset-1">
                                <p>
                                    <a href="http://www.frogdesign.com" target="_blank">
                                        <span className="frogfooter">frog</span>
                                    </a>
                                </p>

                                <p className="georgia">Design and innovation that advances the human experience.</p>
                            </div>
                            <div className="col-xs-12 col-xs-offset-0 col-md-5 col-md-offset-3">
                                <a href="https://twitter.com/frogdesign" target="_blank">
                                    <span className="fa-stack fa-lg">
                                        <i className="fa fa-circle fa-stack-2x"></i>
                                        <i className="fa fa-twitter fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                                <a href="http://www.facebook.com/pages/frog+design/5612622846" target="_blank">
                                    <span
                                        className="fa-stack fa-lg">
                                        <i className="fa fa-circle fa-stack-2x"></i>
                                        <i className="fa fa-facebook fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                                <h6 className="hashtags col-xs-12">#FactOrFiction #frogMI</h6>
                            </div>
                            <div className="col-md-11 col-md-offset-1">
                                <p className="legal">© 2015 frog design inc. All Rights Reserved.
                                    <a href="http://www.frogdesign.com/privacy-policy.html">Privacy Policy</a>
                                    |
                                    <a href="http://www.frogdesign.com/terms-of-use.html">Terms of Use</a>
                                </p>
                            </div>
                        </div>
                    </div>
                </footer>
            </div>
        );
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