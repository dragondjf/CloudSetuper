define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var messages = require('./messages');
    var log = require('log');
    var util = require('./util');
    $(function(){
        log('login');
        $("#login").click(function(){
            var username = $("#login-name").val();
            var password = $("#login-pass").val();
            var result_username = util.check_username(username);
            var result_password = util.check_password(password);
            if(!result_username['status']){
                $("#tipmessage>p").html(result_username['tipmessage']);
                return
            }
            if(!result_password['status']){
                $("#tipmessage>p").html(result_password['tipmessage']);
                return
            }
            if(result_username['status'] && result_password['status']){
                $.ajax({
                    url: '/join',
                    type: 'post',
                    dataType: 'json',
                    data:{
                        'username': username,
                        'password': password
                    },
                    success: function(res){
                        log(res)
                        log("login success");
                        // location.href = "/"
                    },
                    error : function() {
                        log("异常！");    
                    }
                })
            }
        });
    });
});
