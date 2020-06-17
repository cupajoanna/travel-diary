

"use strict";


      // (function(exports) {
      //   "use strict"; 


        function createEntry(locationName){


          window.location.href = `/create-entry/${locationName}`
          console.log(locationName)
          alert("Creating Entry!")
        }


        function seeEntry(content){


          window.location.href = `/create-entry/${props.content}`
          console.log(props.content)
          alert("Going to your blog entry!")
        }


var map;

  function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: {
        lat: 42.3601,
        lng: -71.0589
      },
      zoom: 3
    });

  $.get("/map-json", function(res){

    console.log(res)


  for (var i = 0; i < res.length;i++){
    addMarker({
              coords: {lat: res[i].user_lat, lng: res[i].user_lng},
              content: '<h1>'+ res[i].city_name + '</h1>'
            });
        }});


 $('#geocode-address').on('click', () => {
    const userAddress = prompt('Enter a location');

const geocoder = new google.maps.Geocoder();
geocoder.geocode({ address: userAddress }, (results, status) => {
 if (status === 'OK') {
// Get the coordinates of the user's location
       const userLocation = results[0].geometry.location;
       const locationName = results[0].formatted_address.split(",")[0]
       console.log(results)

// Create a marker
 const userLocationMarker = new google.maps.Marker({

 position: userLocation,
 map: map

});


var infoWindow = new google.maps.InfoWindow({
content:`<h1> ${locationName} </h1>` +  
    `<button id="locationButton" onclick="createEntry('${locationName}')">Create an entry</button>`

});



console.log(locationName)

userLocationMarker.addListener('click', function(){
infoWindow.open(map, userLocationMarker);


});


        // Zoom in on the geolocated location
map.setCenter(userLocation);
map.setZoom(3);

  } else {
     alert(`Geocode was unsuccessful for the following reason: ${status}`);
    }
});
});



      

function addMarker(props){
      var marker = new google.maps.Marker({
      position: props.coords,
      map:map,
      icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'

    });



      if(props.icon){
        marker.setIcon(props.icon);
      };



      if(props.content){

        var infoWindow = new google.maps.InfoWindow({
        content: `<h1> ${props.content} </h1>` +  
    `<button id="routeToEntry" onclick="seeEntry(${props.content})">see your entry</button>`


      });

      marker.addListener('click', function(){
        infoWindow.open(map, marker);

      })};

      }


    };


