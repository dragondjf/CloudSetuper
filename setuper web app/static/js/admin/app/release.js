define(function (require) {
    var $ = require('jquery');
    var flat_ui = require("flat-ui.min");
    var bootstrap = require('bootstrap');
    var util = require('app/util');
    var log = require('log');
    var logout = require('../app/logout');
    $(function(){
        log('release');

        logout.logout();

        if ($('[data-toggle="select"]').length) {
              $('[data-toggle="select"]').select2();
        }

        $.each($('[data-toggle="dropdown"]'), function(index, value){
            $(value).click(function(){
                $(this).siblings().fadeToggle();
            });
        })

        document.getElementById("container").addEventListener('click', function(){
            $('.dropdown-menu').fadeOut();
        })

        var softwarenames = ['CloudSetuper Desktop', 'CloudSetuper CLI']

        $("#Publish").click(function(){

            var softwarename = softwarenames[parseInt($("#softwarename").val())];
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
                    $("#Publish").addClass("disabled");
                },
                error: function() {
                    log("异常！");
                }
            })
        })
    });
});
