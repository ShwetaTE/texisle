$(document).ready(function(){
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID==null){
        deviceID = device.uuid;
        sessionStorage.setItem("deviceID", deviceID);
    }
    var form = new FormData();
    // form.append("app", "test"); //test app
    form.append("app", app_type); //production app
    form.append("app_vr", app_version);
    form.append("deviceID", deviceID);
    form.append("os", os);

    var settings = {
    "url": urlresource + "/version_check/",
    "method": "POST",
    "timeout": 0,
    "processData": false,
    "dataType": 'JSON',
    "mimeType": "multipart/form-data",
    "contentType": false,
    "data": form
    };
    $.ajax(settings).done(function (response) {
        // console.log(response);
        var vr = response.version;
        if(vr==app_version){
            document.cookie = 'vr_check=1;';
        }
        else{
            document.cookie = 'vr_check=0;';
        }
    });
});