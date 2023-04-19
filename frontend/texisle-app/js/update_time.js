function update_time(comp, id){
    // console.log("update time")
    $(id+"1").html("");
    $(id+"2").html("");
    $(id+"3").html("");
    $(id+"4").html("");
    $(id+"5").html("");
    $(id+"6").html("");
    var form = new FormData();
    form.append("chart", comp);

    var settings = {
    "url": urlresource + "/up_time/",
    "method": "POST",
    "timeout": 0,
    "processData": false,
    "dataType": 'JSON',
    "mimeType": "multipart/form-data",
    "contentType": false,
    "data": form
    };

    $.ajax(settings).done(function (response) {
        // console.log(response)
        var time = response['time'];
        var up_time = "Last Updated: "+ time;
        $(id+"1").append(up_time);
        $(id+"2").append(up_time);
        $(id+"3").append(up_time);
        $(id+"4").append(up_time);
        $(id+"5").append(up_time);
        $(id+"6").append(up_time);
    });
}