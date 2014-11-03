// file: js/require-setup.js
//
// Declare this variable before loading RequireJS JavaScript library
// To config RequireJS after it’s loaded, pass the below object into require.config();

var require = {
    shim : {
    	"flat-ui.min": { "deps" :['jquery'] },
    	"jquery.fileupload": { "deps" :['jquery'] },
    	"jquery.knob": { "deps" :['jquery'] },
        "bootstrap" : { "deps" :['jquery'] }
    },
    paths: {
        "jquery" : "http://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.3.min",
        "bootstrap" :  "https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min"  
    }
};