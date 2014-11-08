define(function (require) {
    var $ = require('jquery');
    var bootstrap = require('bootstrap');
    var messages = require('./messages');
    var flat_ui = require("flat-ui.min");
    var ui_widget = require("jquery.ui.widget");
    var knob = require("jquery.knob");
    var iframe_transport = require("jquery.iframe-transport");
    var fileupload = require("jquery.fileupload");
    var colorpicker = require('colorpicker');
    var log = require('log');
    var autoresize = require('./autoresize');
    var util = require('./util');
    $(function(){
        log(messages.getHello());
        log(bootstrap);
        var ul = $('#upload ul');

        // 自动调整body的大小
        autoresize.init();

        $('#drop a').click(function() {
            // Simulate a click on the file input button
            // to show the file browser dialog

            $(this).parent().find('input').click();
        });

        //select background color 
        color_hex = "#353d48";
        var colorpicker = ColorPicker(
            document.getElementById('color-picker'),
            function(hex, hsv, rgb) {
              // console.log(hsv.h, hsv.s, hsv.v);         // [0-359], [0-1], [0-1]
              //console.log(rgb.r, rgb.g, rgb.b);         // [0-255], [0-255], [0-255]
              color_hex = hex;       // #HEX
              // console.log(color_hex)
              $("#colorPreview").css({"background-color": hex})
            });
        colorpicker.setHex(color_hex);

        $('#Signout').click(function(){
             $.ajax({
                url: '/logout',
                type: 'post',
                success: function(res) {
                    log(res)
                    log("logout success");
                    util.deleteAllCookies();
                    location.href="/login";
                },
                error: function() {
                    util.deleteAllCookies();
                    location.href="/login";
                }
            })
        })


        function add2tpl(data){
            var tpl = $('<li class="working"><input type="text" value="0" data-width="48" data-height="48"' +
                    ' data-fgColor="#0788a5" data-readOnly="1" data-bgColor="#3e4043" /><p></p><span></span></li>');

            // Append the file name and file size
            tpl.find('p').html('<i class="filename">' + data.name + '</i>')
                .append('<i>' + formatFileSize(data.size) + '</i>');

            // Add the HTML to the UL element
            tpl.appendTo(ul);

            // Initialize the knob plugin
            tpl.find('input').knob();

            tpl.find('span').hover(
                function(){
                    $("#uploadtip>p").text("click icon to delet this item!");
                    $("#uploadtip").fadeIn();
                }, function(){
                    $("#uploadtip>p").text("click icon to delet this item!");
                    $("#uploadtip").fadeOut();
                }
            )
            // Listen for clicks on the cancel icon
            tpl.find('span').click(function() {
                $.ajax({
                    url: '/upload',
                    type: 'delete',
                    dataType: 'json',
                    data: {
                        'filename': tpl.find(".filename").text()
                    },
                    success: function(res) {
                        log(res)
                        log("delete success");
                        tpl.fadeOut(function() {
                            tpl.remove();
                        });
                    },
                    error: function() {
                        log("异常！");
                        tpl.fadeOut(function() {
                            tpl.remove();
                        });
                    }
                })
                $("#uploadtip").fadeOut();
            });

            return tpl.appendTo(ul);
        }

        // Initialize the jQuery File Upload plugin
        $('#upload').fileupload({

            // This element will accept file drag/drop uploading
            dropZone: $('#drop'),

            // This function is called when a file is added to the queue;
            // either via the browse button, or via drag/drop:
            add: function(e, data) {

                data.context = add2tpl(data.files[0]);
                // Automatically upload the file once it is added to the queue
                var jqXHR = data.submit();
            },

            progress: function(e, data) {

                // Calculate the completion percentage of the upload
                var progress = parseInt(data.loaded / data.total * 100, 10);

                // Update the hidden input field and trigger a change
                // so that the jQuery knob plugin knows to update the dial
                data.context.find('input').val(progress).change();

                if (progress == 100) {
                    data.context.removeClass('working');
                }
            },

            fail: function(e, data) {
                // Something has gone wrong!
                data.context.addClass('error');
            }

        });

        // Prevent the default action when a file is dropped on the window
        $(document).on('drop dragover', function(e) {
            e.preventDefault();
        });

        // Helper function that formats the file sizes
        function formatFileSize(bytes) {
            if (typeof bytes !== 'number') {
                return '';
            }

            if (bytes >= 1000000000) {
                return (bytes / 1000000000).toFixed(2) + ' GB';
            }

            if (bytes >= 1000000) {
                return (bytes / 1000000).toFixed(2) + ' MB';
            }

            return (bytes / 1000).toFixed(2) + ' KB';
            }
        });
    

        var languages = ['en', 'zh-CN', 'zh-TW']
        $("#onesetup").click(function(){
            var softwarename = $("#software-name").val();
            var softwareauthor = $("#software-author").val();
            var softwareemail = $("#software-email").val();
            var softwarecompany = $("#software-company").val();
            var main_progressbar_on = $(".bootstrap-switch-id-main_progressbar").hasClass("bootstrap-switch-on");
            var desktoplink_on = $(".bootstrap-switch-id-desktoplink").hasClass("bootstrap-switch-on");
            
            var language = languages[parseInt($("#Language").val())];
            var files = [];

            if(softwarename.length == 0){
                $("#tipmessage").fadeIn();
                $("#tipmessage>p").html("software name's length must greater than zero!");
                return;
            }

            $.each($(".filename"), function(index, value){
                files.push($(value).text())
            });

            $.ajax({
                url: '/',
                type: 'post',
                dataType: 'json',
                traditional: true,
                data: {
                    'softwarename': softwarename,
                    'softwareauthor': softwareauthor,
                    'softwareemail': softwareemail,
                    'softwarecompany': softwarecompany,
                    'main_progressbar_on': main_progressbar_on,
                    'desktoplink_on': desktoplink_on,
                    'language': language,
                    'background-color': color_hex,
                    'files': files
                },
                success: function(res) {
                    log(res)
                    $("#download>a").attr("href", res.link);
                    $("#download>a").removeClass("disabled");
                    $("#onesetup").addClass("disabled");
                    log("one setup success");
                },
                error: function() {
                    log("异常！");
                }
            })
        })

        if ($('[data-toggle="select"]').length) {
              $('[data-toggle="select"]').select2();
        }
        $('[data-toggle="switch"]').bootstrapSwitch();

        $('[data-toggle="dropdown"]').click(function(){
            $('#mainMenu').fadeToggle();
        })

        $('.dropdown-menu').hover(function(){}, function(){
            $('#mainMenu').fadeOut();
        })
        
        document.getElementById("container").addEventListener('click', function(){
            $('.dropdown-menu').fadeOut();
        })

        $('.bootstrap-switch-id-progressbar').click(function(){
            log($(this).hasClass("bootstrap-switch-on"));
        })

        //监测input输入实时改变事件
        $("#software-name").bind("input propertychange", function(){
            $("#tipmessage").fadeOut();
            if($("#software-name").val().length > 0){
                $("#onesetup").removeClass("disabled");
            }else{
                $("#onesetup").addClass("disabled");
            }
        });


        //存储界面输入值
        var storagekeys = ["software-name", "software-version", "software-author",
            "software-email", "software-company"]

        for (var i = 0; i < storagekeys.length; i++) {
            var id = "#" + storagekeys[i];
            if (storagekeys[i] in localStorage){
                $(id).val(localStorage[storagekeys[i]]);
            }
            $(id).bind("input propertychange",{'index': i, 'id': id}, function(event){
                var i = event.data.index;
                var id = event.data.id;
                localStorage[storagekeys[i]] = $(id).val();
            });
        };

        if ("software-name" in localStorage && $("#software-name").val().length > 0){
            $("#onesetup").removeClass("disabled");
        }


        function startWebSocket() {
            if ("WebSocket" in window) {
                // messageContainer.innerHTML = "WebSocket is supported by your Browser!";
                var ws = new WebSocket("ws://" + location.host + "/ws");
                ws.onopen = function() {
                    // ws.send("Message to send");
                };
                ws.onmessage = function (evt) { 
                    var msg = JSON.parse(evt.data);
                    log(evt.data);
                    if('userCount' in msg){
                        $("#userCount>span").text(msg['userCount']);
                    }
                    if('allCount' in msg){
                        $("#allCount>span").text(msg['allCount']);
                    }
                };
                ws.onclose = function() { 
                    log("Connection is closed...");
                    startWebSocket();
                };
            } else {
                log("WebSocket NOT supported by your Browser!");
            }
        }

        startWebSocket();
});
