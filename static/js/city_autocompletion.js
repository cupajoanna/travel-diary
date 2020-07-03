  
console.log('hello')
$('#city_search').select2({
  ajax:{
    url:"/cities-json",
    dataType:'json',
    method:'GET',
    data: (params) => {
      return {'search_term': params.term}
    }
  },


  placeholder: "search for city",
  width: "200px"
})
