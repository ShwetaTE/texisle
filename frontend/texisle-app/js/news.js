
function newsget_p(chart_type, news_id) {
    // window.alert("alert2!");
    var form = new FormData();
    form.append("chart_type", chart_type);
    // console.log("here")
    var settings = {
        "url": urlresource + "/news_data_index/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "dataType": 'JSON',
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        // console.log(response.data);
        var data = response.data;
        var news_data_element = "";
        if(data.length == 0){
            text = "<br><br<p class='text-muted font-weight-bold title_css'>Curated articles are currently unavailable. Please check back later.</p>";
            $(news_id).append(text);
        }
        else{
            $.each(data, function (key, value) {
                // console.log("33")
                // console.log(value);
                news_data_element =
                '<div class="row" style="width: 100%; padding: 0rem;">'+
                    '<div style="width: 75%; padding: 2% 4%;">'+
                        '<a class="font-weight-bold title_css text-muted">' + value.website + '</a><br>' +
                        '<a onclick ="open_link(\''+ value.link +'\')" class="text-light font-weight-bolder text-hover-primary mb-1 title_css" style="font-size: large;">' + value.title + '</a>' +
                        '<div>' +
                        '<span class="font-weight-bolder title_css">' + value.date + ' ago</span>' +
                        '</div>' +
                    '</div>'+
                    '<div style="width: 25%; padding: 5% 0%;">'+
                        '<img src="' + value.image + '" class="h-70 align-self-center image_css"/>' +
                    '</div>'+
                '</div>'
                $(news_id).append(news_data_element);
            });
        }
        
    });
}

function newsget(chart_type, news_id) {
    // document.getElementById(news_id).innerHTML = "";
    $(news_id).html("");
    // window.alert("alert2!");
    var form = new FormData();
    form.append("chart_type", chart_type);
    // console.log("here")
    var settings = {
        "url": urlresource + "/news_data_updated/",
        // "url": urlresource + "/news_data_updated/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "dataType": 'JSON',
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        // console.log(response.data);
        var data = response.data;
        var news_data_element = "";
        if(data.length == 0){
            text = "<br><br><p class='text-muted font-weight-bold title_css'>Curated articles are currently unavailable. Please check back later.</p>";
            $(news_id).append(text);
        }
        else{
            $.each(data, function (key, value) {
                // console.log("33")
                // console.log(value);
                news_data_element =
                '<div class="row" style="width: 100%; padding: 0rem;">'+
                '<div style="width: 75%; padding: 2% 4%;">'+
                    '<a class="font-weight-bold title_css text-muted">' + value.website + '</a><br>' +
                    '<a href="#" onclick ="open_link(\''+ value.link +'\')" class="text-light font-weight-bolder text-hover-primary mb-1 title_css" style="font-size: large;">' + value.title + '</a>' +
                    '<div>' +
                    '<span class="font-weight-bolder title_css">' + value.date + ' ago</span>' +
                    '</div>' +
                '</div>'+
                '<div style="width: 25%; padding: 5% 0%;">'+
                    '<img src="' + value.image + '" class="h-70 align-self-center image_css"/>' +
                '</div>'+
            '</div>'
                $(news_id).append(news_data_element);
                // console.log(document.getElementById(news_id).innerHTML)
            });
        }  
    });
}

function RecNewsGet(chart_type, news_id) {
    // document.getElementById(news_id).innerHTML = "";
    $(news_id).html("");
    // window.alert("alert2!");
    var form = new FormData();
    form.append("chart_type", chart_type);
    // console.log("here")
    var settings = {
        "url": urlresource + "/rec_news_tabs/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "dataType": 'JSON',
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        // console.log(response.data);
        var data = response.data;
        var news_data_element = "";
        if(data.length == 0){
            console.log("No reccomended news available")
            // text = "<br><br><p class='text-muted font-weight-bold title_css'>Reccomend</p>";
            // $(news_id).append(text);
        }
        else{
            // head_text = "<p class='text-muted font-weight-bold title_css' style='margin: 6px 0px 0px 0px'>★ Reccomended articles</p>"
            // $(news_id).append(head_text);
            $.each(data, function (key, value) {
                // console.log("33")
                // console.log(value);
                news_data_element =
                '<div class="row" style="width: 100%; padding: 0rem;">'+
                '<div style="width: 75%; padding: 2% 4%;">'+
                    '<a class="font-weight-bold title_css text-muted">' + value.website + '</a><br>' +
                    '<a href="#" onclick ="open_link(\''+ value.link +'\')" class="text-light font-weight-bolder text-hover-primary mb-1 title_css" style="font-size: large;">' + value.title + '</a>' +
                    '<div>' +
                    '<span class="font-weight-bolder title_css">' + value.date + ' ago</span>' +
                    '</div>' +
                '</div>'+
                '<div style="width: 25%; padding: 5% 0%;">'+
                    '<img src="' + value.image + '" class="h-70 align-self-center image_css"/>' +
                '</div>'+
            '</div>'
                $(news_id).append(news_data_element);
                // console.log(document.getElementById(news_id).innerHTML)
            });
        }  
    });
}