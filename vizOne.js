var React = require('react');
var io = require('socket.io-client')

var socket = io();

socket.on('update', function (data) {
    console.log(data);
    document.getElementById("console").innerHTML += "<p>Received!"+JSON.stringify(data)+"</p>"
});