define(function () {
    var util = {
        'check_username': function(str){
            if(str.length == 0){
                return {
                    "status": false,
                    "tipmessage": "用户名长度必须大于0"
                }
            }
            else if(str.length > 45){
                return {
                    "status": false,
                    "tipmessage": "用户名长度必须小于45个字符"
                }
            } 
            else{
                if (str.match(/^([u4e00-u9fa5]|[ufe30-uffa0]|[a-za-z0-9_])*$/)){
                    return {
                        "status": true,
                        "tipmessage": "用户名校验成功"
                    }
                }else{
                    return {
                    "status": false,
                    "tipmessage": "用户名只能包含大小写英文字母、汉字、数字和下划线"
                }
                }
            }
        },
        'check_password': function(str){
            if(str.length == 0){
                return {
                    "status": false,
                    "tipmessage": "密码长度必须大于0"
                }
            }
            else if(str.length > 45){
                return {
                    "status": false,
                    "tipmessage": "密码长度必须小于45个字符"
                }
            } 
            else{
                if (str.match(/^([u4e00-u9fa5]|[ufe30-uffa0]|[a-za-z0-9_])*$/)){
                    return {
                        "status": true,
                        "tipmessage": "密码校验成功"
                    }
                }else{
                    return {
                    "status": false,
                    "tipmessage": "密码只能包含大小写英文字母、汉字、数字和下划线"
                }
                }
            }
        },
        'check_email': function(str){
            if(str.match(/^[A-Za-z0-9+]+[A-Za-z0-9\.\_\-+]*@([A-Za-z0-9\-]+\.)+[A-Za-z0-9]+$/)){
                return {
                    "status": true,
                    "tipmessage": "email校验成功"
                }

            }else{
                return {
                    "status": false,
                    "tipmessage": "email格式不正确"
                }
            }
        }
    };
    return util
});