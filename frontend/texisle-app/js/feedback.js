
var rating = null;

function update_rating(val) {
    rating = val;
    console.log(rating);
}

function submit_feedback() {
    var x = document.getElementById("error")
    x.style.display = "none"
    var x = document.getElementById("success")
    x.style.display = "none"

    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("PhNo").value;
    var comment = document.getElementById("comment").value;

    // console.log(name)
    // console.log(email)
    // console.log(phone)
    // console.log(comment)
    // console.log(rating)
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID == null) {
        deviceID = device.uuid;
        sessionStorage.setItem("deviceID", deviceID);
    }

    if (name == '' || email == '' || comment == '' || rating == null) {
        var x = document.getElementById("error")
        x.style.display = "block"
    }
    else {
        document.getElementById("feedback-btn").disabled = true;
        // console.log("ok")

        var form = new FormData();
        form.append("app_type", app_type);
        form.append("deviceID", deviceID);
        form.append("name", name);
        form.append("email", email);
        form.append("phone", phone);
        form.append("comment", comment);
        form.append("rating", rating);

        var settings = {
            "url": urlresource + "/feedback_data/",
            "method": "POST",
            "timeout": 0,
            "processData": false,
            "mimeType": "multipart/form-data",
            "contentType": false,
            "data": form
        };

        $.ajax(settings).done(function (response) {
            console.log(response);
            var x = document.getElementById("success")
            x.style.display = "block"
            document.getElementById("feedback-btn").style.backgroundColor = "#5e5e5e"

            window.setTimeout(function(){
                window.location = "./landing_page.html"
                // location.reload();
            },3000);
        });
    }
}