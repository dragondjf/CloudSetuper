define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var util = require('app/util');
    var log = require('log');
    var logout = require('../app/logout');
    $(function(){
        log('release');

        logout.logout();

        $("#Publish").click(function(){
            var softwarename = $("#software-name").val();
            var softwareversion = $("#software-version").val();
            var softwareauthor = $("#software-author").val();
            var softwareurl = $("#software-url").val();
            var releasenotes = $("#releasenotes").val();

            $.ajax({
                url: '/admin/release',
                type: 'post',
                dataType: 'json',
                traditional: true,
                data: {
                    'softwarename': softwarename,
                    'softwareversion': softwareversion,
                    'softwareauthor': softwareauthor,
                    'softwareurl': softwareurl,
                    'releasenotes': releasenotes
                },
                success: function(res) {
                    log(res)
                    log("publish success");
                },
                error: function() {
                    log("异常！");
                }
            })
        })
    });
});
