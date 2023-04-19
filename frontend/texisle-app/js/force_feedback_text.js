var form = new FormData();
form.append("app", app_type);
form.append("title", "feedback");

var settings = {
  "url": urlresource + "/message/",
  "method": "POST",
  "timeout": 0,
  "processData": false,
  "dataType": 'JSON',
  "mimeType": "multipart/form-data",
  "contentType": false,
  "data": form
};

$.ajax(settings).done(function (response) {
//   console.log(response.message);
  $('#feedback-msg').append(response.message);
});