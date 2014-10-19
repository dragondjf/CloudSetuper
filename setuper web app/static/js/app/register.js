define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var flatui = require('flat-ui.min')
    var messages = require('./messages');
    var log = require('log');
    $(function(){
        log('register');
        $("#register").click(function(){
            var name = $("#login-name").val();
            var emial = $("#login-email").val();
            var password = $("#login-pass").val();



            $.ajax({
                url: '/join',
                type: 'post',
                dataType: 'json',
                data:{
                    'name': name,
                    'email': emial,
                    'password': password
                },
                success: function(res){
                    log(res)
                    log("register success");
                    location.href = "/"
                },
                error : function() {
                    log("异常！");    
                }
            })
        });
    });
});
