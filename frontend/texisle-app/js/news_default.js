$(document).ready(function () {
    newsgetAllNews();
    getRecNews();
});

function newsgetAllNews() {
    $.ajax({
        url: urlresource + "/default_news_data/", 
        type: 'GET',
        dataType: 'JSON',
        success: function (response) {
            var data = response.data;
            // console.log(data);
            var news_data_element = "";
            if(data.length == 0){
                text = "<br><br><p class='text-muted font-weight-bold title_css'>Curated articles are currently unavailable. Please check back later.</p>";
                $('#news_datatable').append(text);
            }
            else{
                $.each(data, function (key, value) {
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
                    $('#news_datatable').append(news_data_element);
                });
            }
        },
        cache: false
    }).fail(function () {
        $('#news_datatable').empty()
        text = "";
        text = "<br><br><p class='text-muted font-weight-bold title_css'>Curated articles are currently unavailable. Please check back later.</p><br><div style='color: white; font-size: 2.5em; text-align: center;' onclick='newsgetAllNews()'><ion-icon name='refresh-outline'></ion-icon></div>";
        $('#news_datatable').append(text);
        console.log("err")
    });

}

function getRecNews() {
    $.ajax({
        url: urlresource + "/rec_news_lp/", 
        type: 'GET',
        dataType: 'JSON',
        success: function (response) {
            var data = response.data;
            // console.log(data);
            var news_data_element = "";
            if(data.length == 0){
                console.log("No reccomended news available")
                // text = "<br><br><p class='text-muted font-weight-bold title_css'>Curated articles are currently unavailable. Please check back later.</p>";
                // $('#news_datatable').append(text);
            }
            else{
                // head_text = "<p class='text-muted font-weight-bold title_css' style='margin: 6px 0px 0px 0px'>★ Reccomended articles</p>"
                // $('#rec_news_datatable').append(head_text);
                $.each(data, function (key, value) {
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
                    $('#rec_news_datatable').append(news_data_element);
                });
            }
        },
        cache: false
    }).fail(function () {
        $('#rec_news_datatable').empty()
        // text = "";
        // text = "<br><br><p class='text-muted font-weight-bold title_css'>Curated articles are currently unavailable. Please check back later.</p><br><div style='color: white; font-size: 2.5em; text-align: center;' onclick='newsgetAllNews()'><ion-icon name='refresh-outline'></ion-icon></div>";
        // $('#news_datatable').append(text);
        console.log("err")
    });

}


//////////////////////////////////////////////////////////////////////////////

    // var settings = {
    //     "url": urlresource + "/default_news_data/",
    //     "method": "GET",
    //     "timeout": 0,
    //     "processData": false,
    //     "dataType": 'JSON',
    //     "mimeType": "multipart/form-data",
    //     "contentType": false
    // };
    
    // $.ajax(settings).done(function (response) {
    //     var data = response.data;
    //     // console.log(data);
    //     var news_data_element = "";
    //     if(data.length == 0){
    //         text = "<br><br><p class='text-muted font-weight-bold title_css'>Curated articles are currently unavailable. Please check back later.</p>";
    //         $('#news_datatable').append(text);
    //     }
    //     else{
    //         $.each(data, function (key, value) {
    //             news_data_element =
    //             '<div class="row" style="width: 100%; padding: 0rem;">'+
    //                 '<div style="width: 75%; padding: 2% 4%;">'+
    //                     '<a class="font-weight-bold title_css text-muted">' + value.website + '</a><br>' +
    //                     '<a onclick ="open_link(\''+ value.link +'\')" class="text-light font-weight-bolder text-hover-primary mb-1 title_css" style="font-size: large;">' + value.title + '</a>' +
    //                     '<div>' +
    //                     '<span class="font-weight-bolder title_css">' + value.date + ' ago</span>' +
    //                     '</div>' +
    //                 '</div>'+
    //                 '<div style="width: 25%; padding: 5% 0%;">'+
    //                     '<img src="' + value.image + '" class="h-70 align-self-center image_css"/>' +
    //                 '</div>'+
    //             '</div>'
    //             $('#news_datatable').append(news_data_element);
    //         });
    //     }
    // });

