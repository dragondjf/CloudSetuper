define(function (require) {
    var $ = require('jquery');
    var log = require('log');
    var util = require('./util');
    $(function(){
        log('help');
        $.each($('[data-toggle="dropdown"]'), function(index, value){
            $(value).click(function(){
                $(this).siblings().fadeToggle();
            });
        });
        document.getElementById("container").addEventListener('click', function(){
            $('.dropdown-menu').fadeOut();
        })
        util.logout()
    });
});
