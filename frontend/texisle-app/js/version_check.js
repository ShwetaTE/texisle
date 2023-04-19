$(document).ready(function(){
    let vr_check = getCookie("vr_check");
    if (vr_check!=1){
        check_version()
    }

    function check_version(){
        // console.log(app_type)
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
            var red_url =response.url;
            var changelog = response.changelog;
            var expiryDate = new Date();
            // expiryDate.setMonth(expiryDate.getMonth() + 1);  //for 1month 
            expiryDate.setTime(expiryDate.getTime()+(15*60*1000));     //for 15min  
            var block_ch = "document.getElementById('version-modal').style.display='none'; document.cookie = 'vr_check=1; expires="+expiryDate+"';"
            // console.log(vr)
            if(vr!=app_version){
                var t= "_system"
                console.log("app outdated...")
                version_modal = 
                    '<div class="modal-pos modal-content">'+
                        '<div>'+
                            '<h2 style="font-weight: bold; color: white; text-align: center; padding: 3%; margin-top: 4px;">App Update</h2>'+
                        '</div>'+
                        '<p style="color: white; text-align: center; font-size: 15px; margin-bottom: 3px;">Pipe Intel v'+vr+' is now available.</p>'+
                        '<p style="color: white; text-align: center; font-size: 15px; margin-bottom: 18px;">Version on your device is v'+app_version+'</p>'+
                        '<p style="font-weight: bold; color: white; text-align: center; font-size: 16px; margin-bottom: 18px;">Whats New?</p>'+
                        '<ul style="color: white; font-size: 15px;margin-left: 16%;margin-right: 7%">'+changelog+'</ul>'+
                        '<div>'+
                            '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">'+
                            '<button href="#" type="button" class="up-btn" onclick ="open_update_link(\''+ red_url +'\')">Update Now</button>'+
                            '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">'+
                            '<button type="button" class="up-btn" onclick="'+block_ch+'">Not Now</button>'+
                        '</div>'+
                    '</div>'
                $('#version-modal').append(version_modal);
                var modal = document.getElementById("version-modal");
                modal.style.display = "block";
            }
            if(vr==app_version){
                document.cookie = 'vr_check=1;';
            }
        });
    }



    function getCookie(cname) {
        let name = cname + "=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }
    
    // function open_update_link(link) {
    //     // localStorage.removeItem("terms")
    //     var deviceID = sessionStorage.getItem("deviceID");
    //     if (deviceID == null) {
    //         deviceID = device.uuid;
    //         sessionStorage.setItem("deviceID", deviceID);
    //     }
    //     var form = new FormData();
    //     form.append("app_type", app_type);
    //     form.append("deviceID", deviceID);
    //     form.append("os", os);

    //     var settings = {
    //         "url": urlresource + "/remove_terms/",
    //         "method": "POST",
    //         "timeout": 0,
    //         "processData": false,
    //         "mimeType": "multipart/form-data",
    //         "contentType": false,
    //         "data": form
    //     };

    //     $.ajax(settings).done(function (response) {
    //         // console.log(response);
    //         var ref = window.open(link, '_system', 'location=no');
    //         ref.show();
    //     });
    // }
});

// style="font-size: 16px; border-top: 1px solid #EBEDF3; text-align: center; font-weight: bold; color: white !important; margin: 8px; margin-bottom: 13px; border: none; cursor: pointer; width: 100%; opacity: 0.9;"