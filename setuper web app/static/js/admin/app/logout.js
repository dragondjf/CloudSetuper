define(function () {
    var util = require('app/util');
    return {
        logout: function () {
            $('#Signout').click(function(){
                 $.ajax({
                    url: '/admin/logout',
                    type: 'post',
                    success: function(res) {
                        console.log(res)
                        console.log("logout success");

                        util.deleteAllCookies();
                        location.href="/admin/login";
                    },
                    error: function() {
                        util.deleteAllCookies();
                        location.href="/admin/login";
                    }
                })
            });
        }
    };
});