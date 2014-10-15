define(function () {
    var autoresize = {
            resize: function(){
                var clientHeight = document.documentElement.clientHeight;
                var clientWidth = document.documentElement.clientWidth;
                document.getElementById("header").style.height = clientHeight * 0.05  + "px";
                document.getElementById("left").style.height = clientHeight * 0.90  + "px";
                document.getElementById("center").style.height = clientHeight * 0.90  + "px";
                document.getElementById("right").style.height = clientHeight * 0.90  + "px";
                document.getElementById("container").style.height = clientHeight * 0.90  + "px";
                document.getElementById("footer").style.height = clientHeight * 0.05  + "px";
            },
            init: function(){
                var that = this;
                window.onresize = function(){
                    that.resize()
                }
                that.resize();
            }
        };
    return autoresize;
});
