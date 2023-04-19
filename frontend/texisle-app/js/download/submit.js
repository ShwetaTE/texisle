var csvFileData = []

function submit() {
    var email_id = getCookie("email")
    console.log(email_id)
    close_div("error1");
    close_div("error2");
    close_div("error3");
    var values = [];
    var cbs = document.forms['tickers'].elements['ticker'];
    for (var i = 0, cbLen = cbs.length; i < cbLen; i++) {
        if (cbs[i].checked) {
            values.push(cbs[i].value);
        }
    }
    var upd_config = 1;
    var upd_selections = document.forms['selection-form'].elements['selection'];
    if(upd_selections.checked == false){
        upd_config = 0;
    }
    else{
        upd_config = 1;
    }
    console.log(values)
    // var dates = document.getElementById("dates")
    // console.log(dates)
    console.log(st_date.format('MM-DD-YYYY'));
    console.log(end_date.format('MM-DD-YYYY'));
    if (values.length == 0) {
        display_div("error2")
    }
    if (email_id == null || email_id == ""){
        // display_div("error3")
        display_div("modal-email")
    }
    else {
        display_div("loader")

        var settings = {
            "url": urlresource + "/web_data/",
            // "url": "https://django.texisle-pipeintel.com/web_data/",
            "method": "POST",
            "timeout": 0,
            "headers": {
                "Content-Type": "application/json"
            },
            "data": JSON.stringify({
                "chart_list": values,
                "start": st_date.format('MM-DD-YYYY'),
                "end": end_date.format('MM-DD-YYYY'),
                "email": email_id,
                "upd_config":upd_config
            }),
        };

        $.ajax(settings).done(function (response) {
            csvFileData = response;
            download_csv_file(values)
            close_div("loader")
        })
        .fail  (function(jqXHR, textStatus, errorThrown) {
            close_div("loader")
            display_div("error1")
        });  
    }
}

function send_data_mail() {
    var email_id = getCookie("email")
    console.log(email_id)
    close_div("error1");
    close_div("error2");
    close_div("error3");
    var values = [];
    var cbs = document.forms['tickers'].elements['ticker'];
    for (var i = 0, cbLen = cbs.length; i < cbLen; i++) {
        if (cbs[i].checked) {
            values.push(cbs[i].value);
        }
    }
    var upd_config = 1;
    var upd_selections = document.forms['selection-form'].elements['selection'];
    if(upd_selections.checked == false){
        upd_config = 0;
    }
    else{
        upd_config = 1;
    }
    console.log(values)
    // var dates = document.getElementById("dates")
    // console.log(dates)
    console.log(st_date.format('MM-DD-YYYY'));
    console.log(end_date.format('MM-DD-YYYY'));
    if (values.length == 0) {
        display_div("error2")
    }
    if (email_id == null || email_id == ""){
        // display_div("error3")
        display_div("modal-email")
    }
    else {
        display_div("loader")

        var settings = {
            "url": urlresource + "/web_data_df/",
            // "url": "https://django.texisle-pipeintel.com/web_data/",
            "method": "POST",
            "timeout": 0,
            "headers": {
                "Content-Type": "application/json"
            },
            "data": JSON.stringify({
                "chart_list": values,
                "start": st_date.format('MM-DD-YYYY'),
                "end": end_date.format('MM-DD-YYYY'),
                "email": email_id,
                "upd_config":upd_config
            }),
        };

        $.ajax(settings).done(function (response) {
            // csvFileData = response;
            // download_csv_file(values)
            close_div("loader")
            console.log(response)
        })
        .fail  (function(jqXHR, textStatus, errorThrown) {
            close_div("loader")
            display_div("error1")
        });  
    }
}

//create a user-defined function to download CSV file   
function download_csv_file(ticker) {

    //define the heading for each row of the data  
    // var csv = 'data,date\n';
    var csv = 'date';
    for(var i = 0; i<ticker.length; i++) {
        temp = ticker[i];
        csv = csv + ',' + temp ;
    }
    csv = csv + '\n';
    // console.log(csv);
    
    //merge the data with CSV  
    csvFileData.forEach(function (row) {
        csv += row.join(',');
        csv += "\n";
    });

    //display the created CSV data on the web browser   
    // document.write(csv);

    var hiddenElement = document.createElement('a');
    hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
    hiddenElement.target = '_blank';

    //provide the name for the CSV file to be downloaded  
    var today = new Date();
    var date = (today.getMonth()+1)+'-'+today.getDate()+'-'+ today.getFullYear();
    hiddenElement.download = 'PipeInel Data '+ date +'.csv';
    hiddenElement.click();
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

function remove_checks(){
    var cbs = document.forms['tickers'].elements['ticker'];
    for (var i = 0, cbLen = cbs.length; i < cbLen; i++) {
        if (cbs[i].checked) {
            cbs[i].checked = false;
        }
    }
}