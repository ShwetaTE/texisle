$(document).ready(function(){
    
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID==null){
        deviceID = device.uuid;
        sessionStorage.setItem("deviceID", deviceID);
    }

    var form = new FormData();
    form.append("app_type", app_type);
    form.append("deviceID", deviceID);
    form.append("app_vr", app_version);
    form.append("terms_vr", terms_vr);
    form.append("os", os);

    var settings = {
    "url": urlresource + "/check_terms/",
    "method": "POST",
    "timeout": 0,
    "processData": false,
    "mimeType": "multipart/form-data",
    "dataType": 'JSON',
    "contentType": false,
    "data": form
    };

    $.ajax(settings).done(function (response) {
        var terms = response.terms;
        if(terms=="N"){
            var x = document.getElementById("accept")
            x.style.display = "block"
        }
        if(terms=="Y"){
            var y = document.getElementById("return")
            y.style.display = "block"
        }
    });

});

function store_info(){
    
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID==null){
        deviceID = device.uuid;
        sessionStorage.setItem("deviceID", deviceID);
    }
    var form = new FormData();
    form.append("app_type", app_type);
    form.append("deviceID", deviceID);
    form.append("app_vr", app_version);
    form.append("os", os);
    form.append("terms_vr", terms_vr);

    var settings = {
    "url": urlresource + "/customer/",
    "method": "POST",
    "timeout": 0,
    "processData": false,
    "mimeType": "multipart/form-data",
    "contentType": false,
    "data": form
    };

    $.ajax(settings).done(function (response) {
        window.location.href = "./landing_page.html";
    });
}