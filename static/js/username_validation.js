  
console.log('username')
$('#username_search').select2({
  ajax:{
    url:"/username-json",
    dataType:'json',
    method:'GET',
    data: (params) => {
      return {'search_term': params.term}
    }
  },


  placeholder: "search for username",
  width: "200px"
})
