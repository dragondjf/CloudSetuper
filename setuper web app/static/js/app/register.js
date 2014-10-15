define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var messages = require('./messages');
    var log = require('log');
    $(function(){
        log('register');
        setTimeout(post, 1000);
        function post(){
            $.ajax({
                url: '/join',
                type: 'post',
                dataType: 'json',
                data:{
                    'name': 'dragondjf',
                    'email': '465398889@qq.com',
                    'password': '123456789'
                },
                success: function(res){
                    log(res);
                    log('hhhhh');
                }
            })
        }
        
    });
});
