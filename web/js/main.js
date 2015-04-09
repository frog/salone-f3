var React = require('react');

if (typeof window !== 'undefined') {
    window.renderClient = function (rootView, props) {
        var mountNode = document.getElementById("content");
        var rootViewClass = require('./'+rootView).ViewClass;

        React.render(React.createElement(rootViewClass, props), mountNode);
    }
}
