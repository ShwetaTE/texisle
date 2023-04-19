var settings = {
    "url": urlresource + "/y_stock_data/",
    "method": "GET",
    "timeout": 0,
    "dataType": 'JSON',
};

$.ajax(settings).done(function (response) {
    
    stock = (response.stock_data);
    // document.cookie = "stock="+ JSON.stringify(stock) +";";
    window.localStorage.setItem("stock",JSON.stringify(stock))
    
});