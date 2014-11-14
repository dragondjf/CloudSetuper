define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var log = require('log');
    var util = require('app/util');
    $(function(){
        log('index');
        
        $('#Signout').click(function(){
             $.ajax({
                url: '/admin/logout',
                type: 'post',
                success: function(res) {
                    log(res)
                    log("logout success");
                    util.deleteAllCookies();
                    location.href="/admin/login";
                },
                error: function() {
                    util.deleteAllCookies();
                    location.href="/admin/login";
                }
            })
        });
    });
});
