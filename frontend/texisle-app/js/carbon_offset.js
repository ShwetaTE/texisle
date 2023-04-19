function calc(){
    var val1 = document.forms[0].ProdType.value;
    var val2 = document.forms[1].OD.value;
    var val3 = parseFloat(document.getElementById('PPF').value)
    var val4 = document.getElementById('quantity').value
    console.log(val1)
    console.log(val2)
    console.log(val3)
    console.log(val4)
    if(val1 == "OCTG"){
        if(val2 == "" || val4 == "" ){
            // console.log("not valid")
            display_div('error')
        }
        else{
            // console.log("Valid")
            close_div('error')
            calculation(val1, val2, val3, val4)
            // $("#final-value").text(final_val);
        }
    }
    if(val1 == "LinePipe"){
        if(val2 == "" || val3 == "" || val4 == "" ){
            // console.log("not valid")
            display_div('error')
        }
        else{
            if(val3 < 0.109  || val3 > 2.00){
                display_div('error2')
            }
            else{
            // console.log("Valid")
            close_div('error2')
            close_div('error')
            calculation(val1, val2, val3, val4)
            // $("#final-value").text(final_val);
            }
        }
    }
    if(val1 == ""){
        // console.log("not valid")
        display_div('error')
    }
}

function display_div(div_name){
    var x = document.getElementById(div_name);
    x.style.display = "block";
}
function close_div(div_name){
    var x = document.getElementById(div_name);
    x.style.display = "none";
}

function calculation(val1, val2, val3, val4){
    display_div("loader")
    var result
    var form = new FormData();
    form.append("product", val1);
    form.append("quantity", val4);
    form.append("weight", val2);
    form.append("ppf", val3);

    var settings = {
    "url": urlresource + "/carbon_offset_calc/",
    "method": "POST",
    "timeout": 0,
    "processData": false,
    "mimeType": "multipart/form-data",
    "dataType": 'JSON',
    "contentType": false,
    "data": form
    };

    $.ajax(settings).done(function (response) {
        result = response.result;
        console.log(result);
        $("#final-value").text(result);
        close_div("loader")
    });
}

function disable(){
    console.log("here")
    var val1 = document.forms[0].ProdType.value;
    console.log(val1)
    if (val1 == "OCTG"){
        ppf_list("OCTG")
        $('#val3-text').html("");
        var temp = "Pounds Per Foot (PPF)"
        $('#val3-text').append(temp);
        var x = document.getElementById('PPF')
        x.max = 169.0;
        x.min = 2.4;
        var y = document.getElementById('val3-input')
        y.style.padding = "0px 5px";
        // x.disabled = true;
        // x.placeholder = "Disabled"
    }
    else{
        ppf_list("PipeLine")
        $('#val3-text').html("");
        var temp = "Wall Thickness<span style='color: red;'>*</span>"
        $('#val3-text').append(temp);
        var x = document.getElementById('PPF')
        x.max = 2.00;
        x.min = 0.109;
        var y = document.getElementById('val3-input')
        y.style.padding = "0px 5px";
        // x.disabled = false;
        // x.placeholder = "Type in Input"
    }
}

function ppf_list(req) {
    $('#val3').html("");
    var wallThickness = [0.109, 0.133, 0.147, 0.154, 0.156, 0.179, 0.188, 0.191, 0.200, 0.203, 0.216, 0.217, 0.218, 0.219, 0.237, 0.250, 0.277, 0.280, 0.281, 0.294, 0.300, 0.307, 0.308, 0.312, 0.322, 0.330, 0.337, 0.344, 0.358, 0.365, 0.375, 0.382, 0.400, 0.406, 0.429, 0.432, 0.436, 0.438, 0.460, 0.500, 0.515, 0.531, 0.552, 0.562, 0.594, 0.600, 0.618, 0.625, 0.652, 0.656, 0.674, 0.687, 0.688, 0.741, 0.750, 0.844, 0.877, 0.906, 1.00, 1.031, 1.125, 1.250, 1.500, 1.750, 2.00]
    var ppf = [2.4,2.76,3.02,3.25,4.5,4.7,5.95,6.5,7.9,8.7,9.3,9.5,10.5,11.5,11.6,12.6,12.75,12.95,13.0,13.5,14.0,15.1,15.5,16.5,17.0,18.0,18.1,19.7,20.0,21.4,21.8,23.0,23.2,24.0,24.1,24.2,26.0,26.4,26.7,26.8,28.0,29.0,29.7,32.0,32.3,32.6,32.75,33.7,35.0,35.3,36.0,38.0,39.0,40.0,40.5,41.0,42.0,42.7,42.8,43.1,43.5,44.0,45.3,45.5,46.1,46.4,47.0,47.1,48.0,49.0,50.1,51.0,51.2,53.5,53.6,54.0,54.5,55.3,57.1,58.4,59.2,60.0,60.7,61.0,64.9,65.0,65.7,68.0,70.3,71.0,71.1,71.8,72.0,73.2,75.0,75.6,79.2,80.7,84.0,85.3,86.0,87.5,88.2,94.0,94.5,95.0,97.0,106.0,106.5,109.0,117.5,118.0,133.0,169.0]
    if(req == "PipeLine") {
        var dropdown = ""
        for(var i = 0; i < wallThickness.length; i++) {
            dropdown = dropdown + "<option value='" + wallThickness[i] + "'>"
        }
        // console.log(dropdown)
        $('#val3').append(dropdown);
    }
    if(req == "OCTG") {
        var dropdown = ""
        for(var i = 0; i < ppf.length; i++) {
            dropdown = dropdown + "<option value='" + ppf[i] + "'>"
        }
        // console.log(dropdown)
        $('#val3').append(dropdown);
    }
}