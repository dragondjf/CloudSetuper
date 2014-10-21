define(function () {
    var autoresize = {
            resize: function(){
                var headerHeight = $("#header").height();
                var footerHeight = $("#footer").height();
                var centerHeight = Math.max($("#left").height(), $("#center").height())
                $("#container").height(centerHeight);
                $("#left").height(centerHeight);
                $("#right").height(centerHeight);
                $("body").height(headerHeight+ $("#center").height() + footerHeight);
            },
            init: function(){
                var that = this;
                window.onresize = function(){
                    that.resize();
                }
                that.resize();
            }
        };
    return autoresize;
});
