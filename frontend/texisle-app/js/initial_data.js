arr = ["raw material index","steel manufacturing","pipe manufacturing","iron ore mining","transport"]

arr.forEach(element => {
    // console.log(element)
    var form = new FormData();
    form.append("chart", element)
    var settings = {
    "url": urlresource + "/index_data_3/",
    "method": "POST",
    "timeout": 0,
    "dataType": 'JSON',
    "processData": false,
    "mimeType": "multipart/form-data",
    "contentType": false,
    "data": form
    };

    $.ajax(settings).done(function (response) {
        window.localStorage.setItem(element,JSON.stringify(response))
    });
});
// console.timeEnd()

var settings = {
    "url": urlresource + "/y_stock_data/",
    "method": "GET",
    "timeout": 0,
    "dataType": 'JSON',
};

$.ajax(settings).done(function (response) {
    
    // stock = (response.stock_data);
    // document.cookie = "stock="+ JSON.stringify(stock) +";";
    window.localStorage.setItem("stock",JSON.stringify(stock))
    
});


var form = new FormData();
form.append("chart", "rig index")

var settings = {
    "url": urlresource + "/rig_data_3/",
    "method": "POST",
    "timeout": 0,
    "dataType": 'JSON',
    "processData": false,
    "mimeType": "multipart/form-data",
    "contentType": false,
    "data": form
    };

$.ajax(settings).done(function (response) {
    // console.log(response)
    window.localStorage.setItem("rig index",JSON.stringify(response))
});

var form = new FormData();
form.append("chart", "DPR")

var settings = {
    "url": urlresource + "/duc_data_5/",
    "method": "POST",
    "timeout": 0,
    "dataType": 'JSON',
    "processData": false,
    "mimeType": "multipart/form-data",
    "contentType": false,
    "data": form
    };

$.ajax(settings).done(function (response) {
    // console.log(response)
    window.localStorage.setItem("dpr_duc",JSON.stringify(response))
});