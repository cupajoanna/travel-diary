  
console.log('email')
$('#email_search').({
  ajax:{
    url:"/email-json",
    dataType:'json',
    method:'GET',
    data: (params) => {
      return {'search_term': params.term}
    }
  },


  placeholder: "search for email",
  width: "200px"
})
