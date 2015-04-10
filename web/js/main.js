if (typeof window !== 'undefined') {
    var React = require('react');
    /**
     * Bootstrap the React application using the "content"
     * element placeholder
     */
    window.renderClient = function (rootView, props) {
        var mountNode = document.getElementById("content");
        var rootViewClass = require('./'+rootView).ViewClass;
        React.render(React.createElement(rootViewClass, props), mountNode);
    }
}
