define(function () {
    var util = {
        'check_username': function(str){
            if(str.length == 0){
                return {
                    "status": false,
                    "tipmessage": "The username's length must greater than zero!"
                }
            }
            else if(str.length > 45){
                return {
                    "status": false,
                    "tipmessage": "The username's length must less than 45!"
                }
            } 
            else{
                if (str.match(/^([u4e00-u9fa5]|[ufe30-uffa0]|[a-za-z0-9_])*$/)){
                    return {
                        "status": true,
                        "tipmessage": "The username valid successfully."
                    }
                }else{
                    return {
                    "status": false,
                    "tipmessage": 'The username can only contains character, digital number and "_ "'
                }
                }
            }
        },
        'check_password': function(str){
            if(str.length == 0){
                return {
                    "status": false,
                    "tipmessage": "The password's length must greater than zero"
                }
            }
            else if(str.length > 45){
                return {
                    "status": false,
                    "tipmessage": "The password's length must less than 45!"
                }
            } 
            else{
                if (str.match(/^([u4e00-u9fa5]|[ufe30-uffa0]|[a-za-z0-9_])*$/)){
                    return {
                        "status": true,
                        "tipmessage": "The password valid successfully."
                    }
                }else{
                    return {
                    "status": false,
                    "tipmessage":  'The password can only contains character, digital number and "_ "'
                }
                }
            }
        },
        'check_email': function(str){
            if(str.match(/^[A-Za-z0-9+]+[A-Za-z0-9\.\_\-+]*@([A-Za-z0-9\-]+\.)+[A-Za-z0-9]+$/)){
                return {
                    "status": true,
                    "tipmessage": "email valid success"
                }

            }else{
                return {
                    "status": false,
                    "tipmessage": "email format invalid"
                }
            }
        },
        'deleteAllCookies': function() {
            var cookies = document.cookie.split(";");

            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i];
                var eqPos = cookie.indexOf("=");
                var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
                document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
            }
        }
    };
    return util
});