$(document).ready(function() {
    $(".fancybox").fancybox({
        'showCloseButton'	: false,
        'showNavArrows'     : true, 
        'helpers'           : { 'title' : { type: 'inside' } }
    });
});

$('.no-thumb').css({
    'height': $('.no-thumb').width() + 'px'
});

$(window).resize(function(){
    $('.no-thumb').css({
        'height': $('.no-thumb').width() + 'px'
    });
});