

  $.get("/map-json", function(res){

    console.log(res)


  for (var i = 0; i < res.length;i++){
    addMarker({
              coords: {lat: res[i].user_lat, lng: res[i].user_lng},
              content: '<h1>'+ res[i].city_name + '</h1>',
              cityId: res[i].city_id 
            });
        }});