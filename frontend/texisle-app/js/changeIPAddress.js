// var urlresource = "https://test-django.texisle-pipeintel.com"; //test server
var app_version = "1.3.15.4"; //test
var app_type = "dev"; //test

// var app_version = "1.3.15.4"   //UAT Apple Test Flight
// var app_type = "uat"         //UAT Apple Test Flight

var urlresource = "http://localhost:8000/texisle-app"; //local

// var urlresource = "https://django.texisle-pipeintel.com"; //production server
// var app_version = "1.3.12"   //prod
// var app_type = "prod"       //prod

//var os = "IOS";
var os = "Android";

var terms_vr = 1;
//////////////////////////////////////////////////////////////////////////////////////
// initial functions
//////////////////////////////////////////////////////////////////////////////////////

function date_range(freq) {
  const today = new Date();
  const priorDate = new Date().setDate(today.getDate() - freq);
  // console.log(priorDate)
  return priorDate;
}

function future_date_range(freq) {
  const today = new Date();
  const futureDate = new Date().setDate(today.getDate() + freq);
  // console.log(futureDate)
  return futureDate;
}

try {
  var stock = JSON.parse(window.localStorage.getItem("stock"));
} catch (err) {
  var settings = {
    url: urlresource + "/y_stock_data/",
    method: "GET",
    timeout: 0,
    dataType: "JSON",
  };

  $.ajax(settings).done(function (response) {
    stock = response.stock_data;
    // document.cookie = "stock="+ JSON.stringify(stock) +";";
    window.localStorage.setItem("stock", JSON.stringify(stock));
    location.reload();
  });
}

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

// ClockFinal.resume();
