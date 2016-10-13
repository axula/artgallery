(function($) {
    $(document).ready(function() {
        var link = $('.field-thumbnail a').attr("href");
        $('.field-thumbnail a').html("<img id='post-thumb' src=" + link + ">");
        $('#post-thumb').css("height", "100px");
        
        $('#id_thumbnail').change(function(){
            console.log('Step1');
            readURL(this);
        });
    });
})(django.jQuery);

function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#post-thumb').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}