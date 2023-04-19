// $(document).ready(function(){

function app_end(path){

    var page = path.split("/").pop();
    var current_page = page.substring(0, page.indexOf("."));
    var page_name = convert_page_name(current_page);
    console.log(page_name)

    var st_time = new Date(sessionStorage.getItem("start_time"));
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID==null){
    deviceID = device.uuid;
    sessionStorage.setItem("deviceID", deviceID);
    }
    var  diff = ((new Date) - st_time)/1000;
    // console.log("diff ---> "+diff);
    console.log("app closed")
    s_id = sessionStorage.getItem("SessionName");

    if(s_id != null){
        var form = new FormData();
        form.append("session_id", sessionStorage.getItem("SessionName"));
        form.append("app_type", app_type);
        form.append("timer", sessionStorage.getItem("timer"));
        form.append("page", page_name);
        form.append("deviceID", deviceID);

        var settings = {
            // "url": "http://localhost:8000/texisle-app/app_ended/",
            "url": urlresource + "/app_ended/",
            "method": "PUT",
            "timeout": 0,
            "processData": false,
            "mimeType": "multipart/form-data",
            "contentType": false,
            "data": form
        };

        $.ajax(settings).done(function (response) {
            console.log(response);
            // window.open("./landing_page.html","_self")
            window.location = "./landing_page.html";
        });
    }
    else{
        // window.open("./landing_page.html","_self")
        window.location = "./landing_page.html";
        }
    
}

function app_tab_change(){
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID==null){
        deviceID = device.uuid;
        sessionStorage.setItem("deviceID", deviceID);
    }
    var s_id = sessionStorage.getItem("SessionName");
    
    if(s_id != null){
        var form = new FormData();
        form.append("session_id", s_id);
        form.append("app_type", app_type);
        form.append("timer", sessionStorage.getItem("timer"));
        form.append("page", "lp");
        form.append("deviceID", deviceID);

        var settings = {
            "url": urlresource + "/app_ended/",
            "method": "PUT",
            "timeout": 0,
            "processData": false,
            "mimeType": "multipart/form-data",
            "contentType": false,
            "data": form
        };

        $.ajax(settings).done(function (response) {
            console.log(response);
        });
    }
    return(1);
}

function app_func_change(page, path){
    console.log("here")
    var path1 = path.split("/").pop();
    var current_page = path1.substring(0, path1.indexOf("."));
    var page_name = convert_page_name(current_page);
    console.log(page_name)

    var st_time = new Date(sessionStorage.getItem("start_time"));
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID==null){
        deviceID = device.uuid;
        sessionStorage.setItem("deviceID", deviceID);
    }
    var  diff = ((new Date) - st_time)/1000;
    // console.log("diff ---> "+diff);
    console.log("app closed")
    s_id = sessionStorage.getItem("SessionName");

    if(s_id != null){
        var form = new FormData();
        form.append("session_id", sessionStorage.getItem("SessionName"));
        form.append("app_type", app_type);
        form.append("timer", sessionStorage.getItem("timer"));
        form.append("page", page_name); 
        form.append("deviceID", deviceID);

        var settings = {
            "url": urlresource + "/app_ended/",
            "method": "PUT",
            "timeout": 0,
            "processData": false,
            "mimeType": "multipart/form-data",
            "contentType": false,
            "data": form
        };

        $.ajax(settings).done(function (response) {
            console.log(response);
            // window.open("./"+page,"_self")
            window.location = "./"+page;
        });
    }
    else{
        // window.open("./"+page,"_self")
        window.location = "./"+page;
    }
}

function convert_page_name(page){
    var page_name = ""
    if(page == "landing_page"){
        page_name = "lp";   
        return(page_name);
    }
    else if(page == "pipe_manufacturing"){
        page_name = "pmf";
        return(page_name);
    }
    else if(page == "raw_material"){
        page_name = "rmi";
        return(page_name);
    }
    else if(page == "iron_ore"){
        page_name = "iom";
        return(page_name);
    }
    else if(page == "transportation"){
        page_name = "t";
        return(page_name);
    }
    else if(page == "steel_manufacturing"){
        page_name = "smf";
        return(page_name);
    }
    else if(page == "rig_count"){
        page_name = "rc";
        return(page_name);
    }
    else if(page == "well_count"){
        page_name = "wc";
        return(page_name);
    }
    else{
        page_name = page;
        return(page_name);
    }
}
 
// });