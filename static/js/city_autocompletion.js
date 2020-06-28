  
// $('#city_search_bar').select2({
//   ajax:{
//     url:"/cities-json"
//     dataType:'json',
//     method:'GET',
//     data: (params) => {
//       return {'search_term': params.term}
//     }
//   },


//   placeholder: "search for city",
//   width: ""
// })

// -----

var substringMatcher = function(strs) {

  return function findMatches(q, cb) {

    var matches, substringRegex;

    // an array that will be populated with substring matches
    matches = [];

    // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, 'i');

    // iterate through the pool of strings and for any string that
    // contains the substring `q`, add it to the `matches` array
    $.each(strs, function(i, str) {
      if (substrRegex.test(str)) {
        matches.push(str);
      }
    });

    cb(matches);
  };
};



$.get("/cities-json", function(res){

console.log(res)


console.log( $('#city_search_bar .typeahead'))

    $('#city_search_bar .typeahead').typeahead({
      hint: true,
      highlight: true,
      minLength: 1
    },
    {
      name: 'cities',
      source: substringMatcher(res)
    });

});



