/**
 * Created by petrosadaman on 28.12.2017.
 */

// scroll listener
$(window).scroll({}, loaddata())



// scroll handler
function loaddata() {
    if( ($(window).scrollTop() + $(window).Height > this.Height) && !busy ) {

        busy = true;

        console.log("loading data")


        $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie("csrftoken") )
           }
        });

        $.ajax({
            url  : "load-data",
            type : "POST",
            data : { temp : temp },
            success : function(json) {
                console.log(json.data)
            },

            error : function (json) {

            }
        });
        busy = false
    }
}