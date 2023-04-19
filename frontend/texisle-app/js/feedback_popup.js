$(document).ready(function () {
    // check_feedback()
});

function check_feedback() {
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID == null) {
        deviceID = device.uuid;
        sessionStorage.setItem("deviceID", deviceID);
    }
    var form = new FormData();
    form.append("deviceID", deviceID);
    form.append("app", app_type);
    var settings = {
        "url": urlresource + "/check_feedback/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "dataType": 'JSON',
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        res = response.status;
        console.log(res)
        if (res != 200){
            console.log(response.Diff)
            if(response.Diff>=3){
                window.location = "./force_feedback.html"
                // show_popup()
            }
        }  
        else{
            document.cookie = 'f_check=1';
        }
    });
}

function show_popup() {
    // var expiryDate = new Date();
    $('#feedback-modal').empty()
    // expiryDate.setTime(expiryDate.getTime() + (150 * 60 * 1000));     //for 15min  
    // var block_ch = "document.getElementById('feedback-modal').style.display='none'; document.cookie = 'f_check=1; expires=" + expiryDate + "';"
    red_url = "feedback.html"
    version_modal =
        '<div class="modal-pos modal-content">' +
        '<div>' +
        // '<h2></h2>'+
        '<h2 style="font-weight: bold; color: white; text-align: center; padding: 3%; margin-top: 4px;">Note</h2>' +
        '</div>' +
        '<p style="font-weight: bold; color: white; text-align: center; font-size: 16px; margin: 7%; text-align: justify; margin-top: 0px;">Thank you for using the app. In order to continue, please provide a feedback. This is to ensure the app is working properly and remains useful for you on daily basis.</p>' +
        '<div>' +
        '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">' +
        '<button href="#" type="button" class="up-btn" onclick ="window.location=\'' + red_url + '\'">Give Feedback</button>' +
        // '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">' +
        // '<button type="button" class="up-btn" onclick="' + block_ch + '">Not Now</button>' +
        '</div>' +
        '</div>'
    $('#feedback-modal').append(version_modal);
    var modal = document.getElementById("feedback-modal");
    modal.style.display = "block";
}

// $(document).ready(function () {

//     let f_check = getCookie("f_check");
//     console.log(f_check);
//     if (f_check != 1) {
//         var t = sessionStorage.getItem("start_time")
//         var someDate = new Date(t);
//         someDate = someDate.getTime();
//         var diff = Math.floor(Date.now() / 1000) - someDate / 1000;
//         console.log(diff)

//         check_feedback()
//     }

//     function check_feedback() {
//         var deviceID = sessionStorage.getItem("deviceID");
//         if (deviceID == null) {
//             deviceID = device.uuid;
//             sessionStorage.setItem("deviceID", deviceID);
//         }
//         var form = new FormData();
//         form.append("deviceID", deviceID);
//         var settings = {
//             "url": urlresource + "/check_feedback/",
//             "method": "POST",
//             "timeout": 0,
//             "processData": false,
//             "dataType": 'JSON',
//             "mimeType": "multipart/form-data",
//             "contentType": false,
//             "data": form
//         };

//         $.ajax(settings).done(function (response) {
//             res = response.status;
//             console.log(res)
//             if (res != 200)
//                 show_popup()
//             else{
//                 document.cookie = 'f_check=1';
//             }
//         });

//     }

//     function show_popup() {
//         if (diff > 60) {
//             var expiryDate = new Date();
//             $('#feedback-modal').empty()
//             expiryDate.setTime(expiryDate.getTime() + (150 * 60 * 1000));     //for 15min  
//             var block_ch = "document.getElementById('feedback-modal').style.display='none'; document.cookie = 'f_check=1; expires=" + expiryDate + "';"
//             red_url = "feedback.html"
//             version_modal =
//                 '<div class="modal-pos modal-content">' +
//                 '<div>' +
//                 '<h2 style="font-weight: bold; color: white; text-align: center; padding: 3%; margin-top: 4px;">Feedback</h2>' +
//                 '</div>' +
//                 '<p style="font-weight: bold; color: white; text-align: center; font-size: 16px; margin-bottom: 18px;">How has been your experience so far?</p>' +
//                 '<div>' +
//                 '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">' +
//                 '<button href="#" type="button" class="up-btn" onclick ="window.location=\'' + red_url + '\'">Give Feedback</button>' +
//                 '<hr style="border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;">' +
//                 '<button type="button" class="up-btn" onclick="' + block_ch + '">Not Now</button>' +
//                 '</div>' +
//                 '</div>'
//             $('#feedback-modal').append(version_modal);
//             var modal = document.getElementById("feedback-modal");
//             modal.style.display = "block";
//         }
//     }

//     function getCookie(cname) {
//         let name = cname + "=";
//         let decodedCookie = decodeURIComponent(document.cookie);
//         let ca = decodedCookie.split(';');
//         for (let i = 0; i < ca.length; i++) {
//             let c = ca[i];
//             while (c.charAt(0) == ' ') {
//                 c = c.substring(1);
//             }
//             if (c.indexOf(name) == 0) {
//                 return c.substring(name.length, c.length);
//             }
//         }
//         return "";
//     }
// });


