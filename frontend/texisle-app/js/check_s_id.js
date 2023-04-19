$(document).ready(function(){
    s_id = sessionStorage.getItem("SessionName");
    var deviceID = sessionStorage.getItem("deviceID");
            if (deviceID==null){
            deviceID = device.uuid;
            sessionStorage.setItem("deviceID", deviceID);
            }
    // console.log(s_id);
    if(s_id == null || deviceID == null){
        window.location.href = "./index.html";
    }


});