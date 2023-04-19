$(function() {
    // document.cookie = "email=atri@gmail.com;";
    var email = getCookie("email")
    var x = document.getElementById("email-id");
    x.innerHTML="";
    x.append(email)
    if(email!='')
        get_config(email);
    else{
        // console.log("No email")
        var deviceID = sessionStorage.getItem("deviceID");
        get_emailID(deviceID)
    }    


    
});

function get_emailID(deviceID){
    var form = new FormData();
    form.append("deviceID", deviceID);
    form.append("app", app_type);

    var settings = {
    "url": urlresource + "/get_emailID/",
    "method": "POST",
    "timeout": 0,
    "processData": false,
    "mimeType": "multipart/form-data",
    "dataType": 'JSON',
    "contentType": false,
    "data": form
    };

    $.ajax(settings).done(function (email_res) {
        if(email_res.exist == 1){
            get_config(email_res.emailID)
        }
        else{
            display_div("modal-email")
        }
    });
}

function get_config(email){
    document.cookie = "email="+ email +";";
    var form = new FormData();
    form.append("email", email);

    var settings = {   
    "url": urlresource + "/get_config/",
    "method": "POST",
    "timeout": 0,
    "processData": false,
    "mimeType": "multipart/form-data",
    "dataType": 'JSON',
    "contentType": false,
    "data": form
    };

    $.ajax(settings).done(function (response) {
    console.log(response);
    if(response.exist == 1){
        var config_list = response.chart_list;
        var cbs = document.forms['tickers'].elements['ticker'];
        console.log(config_list);
        for (var i = 0, cbLen = cbs.length; i < cbLen; i++) {
            for(var j = 0; j<config_list.length; j++){
                if(cbs[i].value == config_list[j]){
                    cbs[i].checked = true
                }
            }
        }
        add_email(email)
    }
    else{
        console.log("email registered")
        add_email(email)
    }
    var x = document.getElementById("email-id");
    x.innerHTML="";
    x.append(email)
    
    });
}

function add_email(email){
    var deviceID = sessionStorage.getItem("deviceID");
    var form = new FormData();
    form.append("deviceID", deviceID);
    form.append("app", app_type);
    form.append("emailID", email);

    var settings = {
    "url": urlresource + "/add_emailID/",
    "method": "POST",
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

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
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


function reload_config(){
    close_div("error1");
    close_div("error2");
    close_div("error3");
    close_div("modal-email")
    var email = document.getElementById("email")
    console.log(email.value);
    var check = validateEmail(email.value);
    if(check == true) {
        close_div('error-email')
        clear_selections();
        get_config(email.value);
        display_div('email-confirmed')
    }
    else{
        // console.log("Invalid Email")
        display_div('error-email')
    }
}

function validateEmail(email) 
{
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function clear_selections(){
    var cbs = document.forms['tickers'].elements['ticker'];
    for (var i = 0, cbLen = cbs.length; i < cbLen; i++) {        
        cbs[i].checked = false
    }
}

function reload_config_alt(){
    close_div("error1");
    close_div("error2");
    close_div("error3");
    var email = document.getElementById("modal-email-input")
    console.log(email.value);
    var check = validateEmail(email.value);
    if(check == true) {
        close_div('modal-email')
        clear_selections();
        get_config(email.value);
        display_div('email-confirmed')
        // send_data_mail();
    }
    else{
        // console.log("Invalid Email")
        display_div('modal-error-email')
    }
}

function close_modal(){
    close_div("modal-email")
}
