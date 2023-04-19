function tweet_html_ticker(chart_type, tweet_id) {
    var form = new FormData();
    form.append("tab_name", chart_type);

    var settings = {
        // "url": urlresource + "/tweet_data_ticker/",
        "url": urlresource + "/tweet_data_ticker/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "dataType": 'JSON',
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        $(tweet_id).empty()
        var i = 0;
        var res = response.data
        if(res.length == 0){
            text = "<br><br><p class='text-muted font-weight-bold title_css' style='margin: 0px 9px;'>Curated tweets are currently unavailable. Please check back later.</p>";
            $(tweet_id).append(text);
        }
        else{
            $.each(response.data, function (key, value) {
                tweet_data_element = "";
                    image_url = "";
                    web_preview = "";
                    modal="";
                    if (value.image_url != " "){
                        var id = "myImg"+i ;
                        var modal_content_id = "modalImg"+i;
                        var modal_id = "myModal"+i;
                        image_url = "<div style=' margin-bottom: 2%; text-align: center;'><img onload='load_modal(\""+id+"\", \""+modal_content_id+"\", \""+modal_id+"\", \""+i+"\")' id='"+id+"' src='" + value.image_url + "' style='width: 95%; height: 255px; object-fit: cover;'></div>";
                        modal = 
                        '<div id="'+modal_id+'" class="modal">'+
                        '<span class="close">&times;</span>'+
                        '<img class="modal-content" id="'+modal_content_id+'">'+
                        '<div id="caption"></div>'+
                        '</div>'
                        // load_modal(id, modal_content_id, modal_id, id)
                        i++;
                    }
                    else {
                        if (value.web_url_image != " ") {
                            web_preview = "<div><div class='web-prev' href='#' onclick ='open_link(\""+ value.web_url +"\")'><img class='web-img' src='" + value.web_url_image + "'><div class='d-flex align-items-center flex-row-fluid flex-wrap' style='width: 100%'><div style='width: 10%;'><i class='fas fa-link' style='color: white;'></i></div><div style='width:90%; text-align: initial;'><p style='color: white;'>" + value.web_text + "</p></div></div></div></div>"
                        }
                    }
                    tweet_data_element =
                        "<div class='tweet-block' style='margin: 10px 6px;'>" +
                        "<div class='d-flex align-items-center flex-row-fluid flex-wrap head-block' style='width: 100%;'>" +
                        "<div style='width: 10%;'>" +
                        "<img style='border-radius: 50px; height: 38px; margin-left: 20%;' src='" + value.profile_pic + "'>" +
                        "</div>" +
                        "<div style='width: 80%; padding-left: 7%;'>" +
                        "<a href='#'' onclick ='open_link(\""+ value.author_url +"\")' style='color: white; text-decoration: none;'>" + value.author_name + "</a>" +
                        "</div>" +
                        "<div style='width: 10%;'>" +
                        "<i class='fab fa-twitter' style='color: white;'></i>" +
                        "</div>" +
                        "</div>" +
                        "<blockquote class='twitter-tweet' data-theme='dark'>" +
                        value.html + "<br>" +
                        "<span class='text-muted'>"+ value.date + "</span>" +
                        "</blockquote>" +
                        image_url + web_preview + modal +
                        "<div style='text-align: center;'>" +
                        "<a class='link-tweet' onclick ='open_link(\""+ value.link +"\")'>Link to Tweet</a>" +
                        "</div>" +
                        "</div>" +
                        "<hr style='border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;'></hr>";
    
                $(tweet_id).append(tweet_data_element);
            });
        }     
    });
}

function tweet_html_index(chart_type, tweet_id) {
    var form = new FormData();
    form.append("chart", chart_type);

    var settings = {
        "url": urlresource + "/tweet_data_index/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "dataType": 'JSON',
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        $(tweet_id).empty()
        var i = 0;
        var res = response.data
        if(res.length == 0){
            text = "<br><br><p class='text-muted font-weight-bold title_css' style='margin: 0px 9px;'>Curated tweets are currently unavailable. Please check back later.</p>";
            $(tweet_id).append(text);
        }
        else{
            $.each(response.data, function (key, value) {
                tweet_data_element = "";
                image_url = "";
                web_preview = "";
                modal="";
                if (value.image_url != " "){
                    var id = "myImg"+i ;
                    var modal_content_id = "modalImg"+i;
                    var modal_id = "myModal"+i;
                    image_url = "<div style=' margin-bottom: 2%; text-align: center;'><img onload='load_modal(\""+id+"\", \""+modal_content_id+"\", \""+modal_id+"\", \""+i+"\")' id='"+id+"' src='" + value.image_url + "' style='width: 95%; height: 255px; object-fit: cover;'></div>";
                    modal = 
                    '<div id="'+modal_id+'" class="modal">'+
                    '<span class="close">&times;</span>'+
                    '<img class="modal-content" id="'+modal_content_id+'">'+
                    '<div id="caption"></div>'+
                    '</div>'
                    // load_modal(id, modal_content_id, modal_id, id)
                    i++;
                }
                else {
                    if (value.web_url_image != " ") {
                        web_preview = "<div><div class='web-prev' href='#' onclick ='open_link(\""+ value.web_url +"\")'><img class='web-img' src='" + value.web_url_image + "'><div class='d-flex align-items-center flex-row-fluid flex-wrap' style='width: 100%'><div style='width: 10%;'><i class='fas fa-link' style='color: white;'></i></div><div style='width:90%; text-align: initial;'><p style='color: white;'>" + value.web_text + "</p></div></div></div></div>"
                    }
                }
                tweet_data_element =
                    "<div class='tweet-block' style='margin: 10px 6px;'>" +
                    "<div class='d-flex align-items-center flex-row-fluid flex-wrap head-block' style='width: 100%;'>" +
                    "<div style='width: 10%;'>" +
                    "<img style='border-radius: 50px; height: 38px; margin-left: 20%;' src='" + value.profile_pic + "'>" +
                    "</div>" +
                    "<div style='width: 80%; padding-left: 7%;'>" +
                    "<a href='#'' onclick ='open_link(\""+ value.author_url +"\")' style='color: white; text-decoration: none;'>" + value.author_name + "</a>" +
                    "</div>" +
                    "<div style='width: 10%;'>" +
                    "<i class='fab fa-twitter' style='color: white;'></i>" +
                    "</div>" +
                    "</div>" +
                    "<blockquote class='twitter-tweet' data-theme='dark'>" +
                    value.html + "<br>" +
                    "<span class='text-muted'>"+ value.date + "</span>" +
                    "</blockquote>" +
                    image_url + web_preview + modal +
                    "<div style='text-align: center;'>" +
                    "<a class='link-tweet' onclick ='open_link(\""+ value.link +"\")'>Link to Tweet</a>" +
                    "</div>" +
                    "</div>" +
                    "<hr style='border-top: 1.5px solid #565450; margin-bottom: 0rem; margin-top: 0rem;'></hr>";
        
                    $(tweet_id).append(tweet_data_element);
                });
        }
    });
}
