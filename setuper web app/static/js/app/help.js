define(function (require) {
    var $ = require('jquery');
    var log = require('log');
    $(function(){
        log('help');
        $.each($('[data-toggle="dropdown"]'), function(index, value){
            $(value).click(function(){
                $(this).siblings().fadeToggle();
            });
        })
    });
});
