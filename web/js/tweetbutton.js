var React = require('react');

var URL = "http://f3.cloud.frogdesign.com";
var URL_SHORTENED_LENGTH = 22;
var TWEET_LENGTH = 140;

var ACCOUNT = "frogdesign";
var HASHTAGS = ['factorfiction', 'frogmi']

module.exports.ViewClass = React.createClass({
    displayName: 'TweetButton',
    render: function () {
        //prepare chunks of tweet
        var postfix = " @" + ACCOUNT;
        var hashtags = ' #' + HASHTAGS.join(' #');
        var availableChars = TWEET_LENGTH - hashtags.length - postfix.length - URL_SHORTENED_LENGTH - 1;

        //cutting the last character if needed and showing ellipsis
        var tweetText = this.props.spread.text;
        if (tweetText.length >= availableChars) {
            tweetText = tweetText.substring(0, availableChars - 1);
            tweetText = tweetText + "\u2026";
        }

        var the_target = "https://twitter.com/share?";
        the_target += "&url=" + URL + "&counturl=" + URL;
        the_target += "&related="+ ACCOUNT + "&dnt=true";
        the_target += "&text=" + encodeURIComponent(tweetText + hashtags + postfix);

        return (
            <div className="sharebutton">
                <a href={the_target} target="_blank" className="btn share">
                    <h6>Share on Twitter</h6>
                </a>
            </div>
        );
    }
});