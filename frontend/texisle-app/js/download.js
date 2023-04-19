function copy() {
    /* Get the text field */
    var copyText = "https://data.texisle-pipeintel.com/"
    navigator.clipboard.writeText(copyText);

    /* Alert the copied text */
    // alert("Copied the text: " + copyText);
  }

function send_email() {
    var email = document.getElementById("email")
    console.log(email.value);
    var check = validateEmail(email.value);
    if(check == true) {
        close_div('error')
        var form = new FormData();
        form.append("receiver_address", email.value);

        var settings = {
        "url": urlresource + "/send_download_link/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
        };

        $.ajax(settings).done(function (response) {
        console.log(response);
        display_div('success');
        });
    }
    else{
        console.log("Invalid Email")
        display_div('error')
    }
    
}

function validateEmail(email) 
    {
        var re = /\S+@\S+\.\S+/;
        return re.test(email);
    }

function display_div(div_name){
    var x = document.getElementById(div_name);
    x.style.display = "block";
}
function close_div(div_name){
    var x = document.getElementById(div_name);
    x.style.display = "none";
}