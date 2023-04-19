$(document).ready(function () {

    // console.log("here")

    $( "div.lock-div" )
    .mouseover(function() {
        console.log("in");
        disable_scroll();
    })
    .mouseout(function() {
        console.log("out")
        enable_scroll();
    });

    function disable_scroll() {
        $('body').addClass('stop-scrolling')
        $('body').bind('touchmove', function(e){e.preventDefault()})
    }
    
    function enable_scroll() {
        $('body').removeClass("stop-scrolling");
        $('body').unbind('touchmove');
    }

});
