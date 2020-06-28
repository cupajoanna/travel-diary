

"use strict";


        function seeEntry(cityId){


          window.location.href = `/route-to-entry/${cityId}`
          console.log(cityId)
          console.log(content)
          alert("Going to your blog entry!")
        };



var map;

  function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: {
        lat: 42.3601,
        lng: -71.0589
      },
      zoom: 3
    });





$('.btn btn-primary btn-lg').on('click',(evt) => {
    alert("seeing their map")
    evt.preventDefault()


  $.get(`/users/${user.user_id}/map-json`, function(res){

    console.log(res)


  for (var i = 0; i < res.length;i++){
    addMarker({
              coords: {lat: res[i].user_lat, lng: res[i].user_lng},
              content: '<h1>'+ res[i].city_name + '</h1>',
              cityId: res[i].city_id 
            });
        }})
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
    `<button id="routeToEntry" onclick="seeEntry(${props.cityId})">see your entry</button>`


      });



      marker.addListener('click', function(){
        infoWindow.open(map, marker);

      })};

      }};


