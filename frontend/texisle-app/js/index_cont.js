$(document).ready(function(){
    window.setTimeout(function(){
        if(app_tab_change() == true){
            var deviceID = sessionStorage.getItem("deviceID");
            if (deviceID==null){
            deviceID = device.uuid;
            sessionStorage.setItem("deviceID", deviceID);
            }
            var form = new FormData();
            form.append("app_type", app_type);
            form.append("deviceID", deviceID);
            form.append("app_vr", app_version);
            form.append("terms_vr", terms_vr);
            form.append("os", os);

            var settings = {
            "url": urlresource + "/check_terms/",
            "method": "POST",
            "timeout": 0,
            "processData": false,
            "mimeType": "multipart/form-data",
            "dataType": 'JSON',
            "contentType": false,
            "data": form
            };

            $.ajax(settings).done(function (response) {
                var terms = response.terms;
                console.log(terms)
                if (terms == 'Y') {
                    var settings = {
                        "url": urlresource + "/y_stock_data/",
                        "method": "GET",
                        "timeout": 0,
                        "dataType": 'JSON',
                    };
                    
                    $.ajax(settings).done(function (response) {
                        var stock = (response.stock_data);
                        window.localStorage.setItem("stock",JSON.stringify(stock));
                        window.open('./landing_page.html', '_self');
                    });
                }
                else if (terms == 'N') {
                    var settings = {
                        "url": urlresource + "/y_stock_data/",
                        "method": "GET",
                        "timeout": 0,
                        "dataType": 'JSON',
                    };
                    
                    $.ajax(settings).done(function (response) {
                        var stock = (response.stock_data);
                        window.localStorage.setItem("stock",JSON.stringify(stock));
                        
                        window.open('./terms.html', '_self');
                    });
                }

            });
        }
    
    }, 100);
});