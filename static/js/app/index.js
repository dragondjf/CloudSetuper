define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var messages = require('./messages');
    var log = require('log');
    $(function(){
        log(messages.getHello());
        log(bootstrap);
        // $.ajax({
        //     url: '/join'
        // })
    });
});
