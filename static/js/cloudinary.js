


var CLOUDINARY_URL = 'https://api.cloudinary.com/v1_1/dopcdckl3/upload';
var CLOUDINARY_UPLOAD_PRESET = 'zsjjyozh';

// var imgPreview = document.getElementByID('img-preview');
var fileUpload = document.getElementById('image-upload');

fileUpload.addEventListener('change', function(event){

    var file = event.target.files[0];
    var formData = new formData();
    formData.append('file', file);
    forData.append('upload_preset', CLOUDINARY_UPLOAD_PRESET)

    axios({
        url: CLOUDINARY_URL,
        method: 'POST',
        headers: {
            'content-Type': 'application/x-www-form-urlencoded'

        },
        data: formData
    }).then(function(res) {
        console.log(res);

    }).catch(function(err) {
        console.error(err);

    });

});
