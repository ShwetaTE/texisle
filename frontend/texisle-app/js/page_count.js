$(document).ready(function () {
    var path = window.location.pathname;
    var page = path.split("/").pop();
    var current_page = page.substring(0, page.indexOf("."));
    var page_name = convert_page_name(current_page);
    console.log(page_name)

    // var st_time = new Date(sessionStorage.getItem("start_time"));
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID==null){
    deviceID = device.uuid;
    sessionStorage.setItem("deviceID", deviceID);
    }
    // var  diff = ((new Date) - st_time)/1000;
    // console.log("diff ---> "+diff);
    console.log("page opened")
    s_id = sessionStorage.getItem("SessionName");

    if(s_id != null){
        var form = new FormData();
        form.append("session_id", sessionStorage.getItem("SessionName"));
        form.append("app_type", app_type);
        // form.append("timer", sessionStorage.getItem("timer"));
        form.append("page", page_name);
        form.append("deviceID", deviceID);

        var settings = {
            // "url": "http://localhost:8000/texisle-app/app_ended/",
            "url": urlresource + "/page_count/",
            "method": "PUT",
            "timeout": 0,
            "processData": false,
            "mimeType": "multipart/form-data",
            "contentType": false,
            "data": form
        };

        $.ajax(settings).done(function (response) {
            console.log("Click registered");
            // window.open("./landing_page.html","_self")
            // window.location = "./landing_page.html";
        });
    }
    else{
        // window.open("./landing_page.html","_self")
        window.location = "./index.html";
        }
    
});