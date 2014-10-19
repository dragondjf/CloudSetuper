define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var messages = require('./messages');
    var log = require('log');
    $(function(){
        log('login');
        $("#login").click(function(){
            var name = $("#login-name").val();
            var password = $("#login-pass").val();
            log(name);
            $.ajax({
                url: '/login',
                type: 'post',
                dataType: 'json',
                data:{
                    'name': name,
                    'password': password
                },
                success: function(res){
                    log(res)
                    log("login success");
                    location.href = "/"
                },
                error : function() {
                    log("异常！");    
                }
            })
        });
    });
});
