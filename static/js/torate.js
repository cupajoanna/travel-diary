"use strict";


$('.add-to-likes-button').on('click',(evt) => {
    alert("liking entry")
    evt.preventDefault()
    console.log("liking photo")


    var rating_id = evt.target.id
    var entry_id = evt.target.value
    // console.log(photo_id)
    // console.log($(this))
    // console.log(evt.target)

    $.post(`/entries/${entry_id}/like-entry`, (res) => {
        $('#likes-counter').html(res) 
        console.log(res)
    })

});

// const incrementLikes = () => {

//     const likesTotal = $('#likes-counter');

//     let total = Number(likesTotal.html());
//     total += 1;

//     likesTotal.html(total);


// $('.add-to-likes-button').on('click', () => {
//   incrementLikes()
// });



// $('.photo_delete').on('click',(evt) => {
//     alert("deleting photo")
//     evt.preventDefault()

//     var photo_id = evt.target.id
//     // console.log(photo_id)
//     // console.log($(this))
//     // console.log(evt.target)

//     $.post("/delete-photo", {"photo_id": photo_id}, (res) => {

//         evt.target.parentNode.remove() 
//     })


// });
