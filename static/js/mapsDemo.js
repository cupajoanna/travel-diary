

"use strict";


      // (function(exports) {
      //   "use strict"; 



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
            content:'<h1>'+ locationName + '</h1>' +  
                '<button id="locationButton">Create an entry</button>'

          });



            console.log(locationName)

          userLocationMarker.addListener('click', function(){
            infoWindow.open(map, userLocationMarker);

          $('#locationButton').click(function(){
            window.location.href = `/create-entry?city_name={locationName}`
            alert("hello")
          
           })
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
            content: props.content
          });

          marker.addListener('click', function(){
            infoWindow.open(map, marker);

          })};

          }


        };


  
         
          // addMarker({
          //             coords: {lat: 42.8584, lng: -70.9300},
          //             content: '<h1> Amesbury, MA </h1>'

          //           });
          // addMarker({coords: {lat: 42.7762, lng: -71.0773},
          //             content: '<h1> Manchester, MA </h1>'
          //           });

        // loop through markers

//       var markers = [
// {
//           coords: {lat: 42.4668, lng: -70.9495},
//           content: '<h1> Lynn, MA </h1>'
//         },
// {
//           coords: {lat: 42.8584, lng: -70.9300},
//           content: '<h1> Amesbury, MA </h1>'
//         },
// {
//           coords: {lat: 42.4668, lng: -70.9495},
//           content: '<h1> Lynn, MA </h1>'
//         }



// ];

// for (var i = 0; i < markers.length;i++){
//   addMarker(markers[i]);
// }


// function addMarker(props){
// var marker = new google.maps.Marker({
// position: props.coords,
// map:map,
// icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'

// });



        //jinja

          
          // {% for city in user_cities %}

          // {{ city.geo_lat}}
          // {{ city.geo_lng }}

          // console_log(city.geo_lat)
          // console_log(city.geo_lng)

          // {% endfor %}

      //   exports.initMap = initMap;
      // });

      // ((this.window = this.window || {}))


