define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var flatui = require('flat-ui.min')
    var messages = require('./messages');
    var log = require('log');
    var util = require('./util');

    $(function(){
        log('join');
        $("#join").click(function(){
            var username = $("#login-name").val();
            var email = $("#login-email").val();
            var password = $("#login-pass").val();
            var result_username = util.check_username(username);
            var result_email = util.check_email(email);
            var result_password = util.check_password(password);
            if(!result_username['status']){
                $("#tipmessage>p").html(result_username['tipmessage']);
                return
            }
            if(!result_email['status']){
                $("#tipmessage>p").html(result_email['tipmessage']);
                return
            }
            if(!result_password['status']){
                $("#tipmessage>p").html(result_password['tipmessage']);
                return
            }
            if(result_username['status'] && result_email['status'] && result_password['status']){
                $.ajax({
                    url: '/join',
                    type: 'post',
                    dataType: 'json',
                    data:{
                        'username': username,
                        'email': email,
                        'password': password
                    },
                    success: function(res){
                        log(res)
                        log("join success");
                        if(res['status'] == "success"){
                            location.href = "/";
                        }else{
                            $("#tipmessage>p").html(res['info']);
                        }
                    },
                    error : function() {
                        log("error");
                        $("#tipmessage>p").html("internet error."); 
                    }
                })
            }
        });
    });
});
