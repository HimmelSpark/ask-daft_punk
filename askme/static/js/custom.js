/**
 * Created by petrosadaman on 11.12.2017.
 */

function like(user, qID, positive) {
            $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie('csrftoken') )
           }
        });

        // like
        if (positive) {
            $.ajax({
                url : "like",
                type : "POST",
                data : { user: user, question: qID, positive: positive },
                success : function(json) {
                    console.log('Positive Success')
                    var button = document.getElementById('like'+qID)
                    console.log(json.likecount)
                    button.innerText = "(+" + json.likecount + ")"
                    button.isDisabled = true
                },

                error : function (json) {
                    console.log(json.ErrorMSG)
                }
            });
        }
        //dislike
        else {
            $.ajax({
                url: "like",
                type: "POST",
                data: { user: user, question: qID, positive: positive },
                success: function (json) {
                    console.log('Negative Success')
                    button = document.getElementById('dislike'+qID)
                    button.innerText = "(-" + json.discount + ")"
                },

                error: function (json) {
                    console.log(json.ErrorMSG)
                }
            })
        }
};


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function() {

    $('.modal1').click( function(event){
        event.preventDefault();
        $('#overlay1').fadeIn(400, // анимируем показ обложки
            function(){ // далее показываем мод. окно
                $('#modal_form1')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
        });
    });


    $('.modal2').click( function(event){
        event.preventDefault();
        $('#overlay2').fadeIn(400, // анимируем показ обложки
            function(){ // далее показываем мод. окно
                $('#modal_form2')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
        });
    });


    // закрытие модального окна
    $('#modal_close1, #overlay1').click( function(){
        $('#modal_form1')
            .animate({opacity: 0, top: '45%'}, 200,  // уменьшаем прозрачность
                function(){ // пoсле aнимaции
                    $(this).css('display', 'none'); // скрываем окно
                    $('#overlay1').fadeOut(400); // скрывaем пoдлoжку
                }
            );
    });


    // закрытие модального окна
    $('#modal_close2, #overlay2').click( function(){
        $('#modal_form2')
            .animate({opacity: 0, top: '45%'}, 200,  // уменьшаем прозрачность
                function(){ // пoсле aнимaции
                    $(this).css('display', 'none'); // скрываем окно
                    $('#overlay2').fadeOut(400); // скрывaем пoдлoжку
                }
            );
    });

});


function logvalid(form) {
    var text_fields = form.getElementsByTagName('input');
    var validated = true;

    for( var i = 0; i < text_fields.length; ++i ) {

        if( text_fields[i].type === 'password' && text_fields[i].value.length < 8 ) {
            validated = false;
            alert('Too few symbols. 8 required.')
            return validated;
        }
    }

    return validated;
}

function regvalid(form) {
    var text_fields = form.getElementsByTagName('input');
    var validated = true;
    var passwords = [];

    for( var i = 0; i < text_fields.length; ++i ) {

        if( text_fields[i].type === 'password' ) {

            if( text_fields[i].value.length < 8 ) {
                validated = false;
                alert('Too few symbols. 8 required.');
                return validated;
            }

            passwords.push(text_fields[i]);

        }
    }

    if( passwords[0].value !== passwords[1].value ) {

        validated = false;
        alert('Password fields did not match!');
        passwords[0].value = passwords[1].value = '';
        return validated;
    }

    return validated;
}