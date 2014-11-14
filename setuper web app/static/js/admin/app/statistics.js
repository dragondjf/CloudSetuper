define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var util = require('app/util');
    var log = require('log');
    var logout = require('../app/logout');
    $(function(){
        log('statistics');
        logout.logout();
    });
});
