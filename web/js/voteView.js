var React = require('react');
var io = require('socket.io-client');

var isBrowser = !(global && Object.prototype.toString.call(global.process) === '[object process]');

var TweetButton = React.createClass({
    displayName: 'TweetButton',
    render: function () {
        var postfix = " @frogdesign";
        var hashtags = ' #'+['factorfiction','frogmi'].join(' #');
        var url = "http://f3.cloud.frogdesign.com";
        var availableChars = 140 - hashtags.length - postfix.length -  /*url.length*/ 22 - 1;
        var tweetText = this.props.spread.text;
        if (tweetText.length >= availableChars) {
            tweetText = tweetText.substring(0, availableChars - 3);
            tweetText = tweetText +"\u2026";
        }
        var the_target = "https://twitter.com/share?";
        the_target += "&url="+url+"&counturl="+url;
        the_target += "&related=frogdesign&dnt=true";
        the_target += "&text="+encodeURIComponent(tweetText+hashtags+postfix);
        //the_target += "&hashtags="+hashtags.join(',');
        return (
            <div className="sharebutton">
                <a href={the_target} target="_blank" type="button" className="btn share">
                    <h6>Share on Twitter</h6>
                </a>
            </div>
        );
    }
});

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


            var masonry = require('masonry-layout');
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
                        <img src="/hpstatic/img/cover.png" width="100%" alt="Vote Now"/>
                    </a>
                </section>
                <section id="about" className="home-section text-center bg-gray">
                    <div className="container">
                        <div className="col-md-offset-3 col-md-6">
                            <img src="/hpstatic/img/ten.png" width="50%" alt="frog turns 10"/>

                            <h3>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,
                                totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae
                                dicta sunt explicabo.</h3>
                        </div>
                    </div>
                </section>
                <div id="separatore">
                    <img src="/hpstatic/img/fact-or-fiction.png" alt="Fact or Fiction"/>
                </div>
                <section id="voting">
                    <div className="row">
                        {the_cols}
                    </div>
                </section>
                <section id="contact" className="home-section">
                    <div className="heading-contact marginbot-50">
                        <div className="container">
                            <div className="row">
                                <div className="col-md-6 col-md-offset-1">
                                    qui va immagine quotidiano piegato
                                </div>
                                <div className="col-md-4">

                                    <div className="section">
                                        <div id="registerheadline">
                                            <h2>REGISTER TOBEFIXED</h2>
                                        </div>
                                        <p>You are invited to join us at frog Milan on April 14th as we will celebrate our 10th
                                            anniversary by speculating on possible futures. Together, we will assess what may become
                                            future fact or fiction for Salone in 2025.</p>

                                        <div className="rsvpbutton">
                                            <a href="http://info2.frogdesign.com/future-fact-or-fiction" target="_blank"
                                                className="btn-lg rsvp">
                                                <span>RSVP</span>
                                            </a>
                                        </div>
                                    </div>

                                </div>
                            </div>
                        </div>
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
                                <h6 className="hashtags col-xs-12">#FactOrFiction #FrogMI</h6>
                            </div>
                            <div className="col-md-11 col-md-offset-1">
                                <p class="className">© 2015 frog design inc. All Rights Reserved.
                                    <a
                                        href="http://www.frogdesign.com/privacy-policy.html">Privacy Policy</a>
                                    |
                                    <a
                                        href="http://www.frogdesign.com/terms-of-use.html">Terms of Use</a>
                                </p>
                            </div>
                        </div>
                    </div>
                </footer>
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