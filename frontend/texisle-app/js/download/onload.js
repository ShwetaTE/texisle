$(document).ready(function () {
    var email_id = getCookie("email")
    // console.log("hh")
    if (email_id == null || email_id == ""){
        display_div("modal-email")
    }

    function display_div(div_name){
        var x = document.getElementById(div_name);
        x.style.display = "block";
    }
    
    function close_div(div_name){
        var x = document.getElementById(div_name);
        x.style.display = "none";
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
});