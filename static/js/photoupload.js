
"use strict";





$('#file_submit').on('click',(evt) => {
    console.log("loading")
    evt.preventDefault()

    if ( $('#image-upload').val()) {
        $('#form').submit()
    }

    else
        { 
        $('#form').attr( "enctype", "" )
        $('#form').submit()
    }
});


$('.photo_delete').on('click',(evt) => {
    alert("deleting photo")
    evt.preventDefault()

    var photo_id = evt.target.id
    // console.log(photo_id)
    // console.log($(this))
    // console.log(evt.target)

    $.post("/delete-photo", {"photo_id": photo_id}, (res) => {

        evt.target.parentNode.remove() 
    })


});

