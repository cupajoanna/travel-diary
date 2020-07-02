

"use strict";


      // (function(exports) {
      //   "use strict"; 


        function createEntry(locationName){


          window.location.href = `/create-entry/${locationName}`
          console.log(locationName)
          alert("Creating Entry!")
        };

        function seeEntry(cityId){


          window.location.href = `/route-to-entry/${cityId}`



          console.log(cityId)
          console.log(content)
          alert("Going to your blog entry!")
        };


$('#see-map').on('click',(evt) => {
    evt.preventDefault()
    console.log("looking")


    var user_id = evt.target.value
    // console.log(photo_id)
    // console.log($(this))
    // console.log(evt.target)

    console.log("user_id", user_id)

  $.get(`/users/${user_id}/map-json`, function(res){

    console.log(res)


  for (var i = 0; i < res.length;i++){
    addMarker({
              coords: {lat: res[i].user_lat, lng: res[i].user_lng},
              content: '<h1>'+ res[i].city_name + '</h1>',
              cityId: res[i].city_id 
            });
        }});

});

