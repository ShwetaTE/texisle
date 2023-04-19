$(document).ready(function(){

    var settings = {
        "url": urlresource + "/y_stock_data/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function (response) {
        console.log(response)
        // console.log(response.stock_data.scrap_data.current);
        document.getElementById("pm_val_current").innerHTML = (response.stock_data.pipe_manufacturing.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.pipe_manufacturing.data >= 0)
            document.getElementById("pm_val_data").innerHTML = "+" + (response.stock_data.pipe_manufacturing.data).toFixed(2) + " %";
        else
            document.getElementById("pm_val_data_neg").innerHTML = (response.stock_data.pipe_manufacturing.data).toFixed(2) + " %";

        document.getElementById("x_val_current").innerHTML = (response.stock_data.x_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.x_data.data >= 0)
            document.getElementById("x_val_data").innerHTML = "+" + (response.stock_data.x_data.data).toFixed(2) + " %";
        else
            document.getElementById("x_val_data_neg").innerHTML = (response.stock_data.x_data.data).toFixed(2) + " %";
        
        document.getElementById("ts_val_current").innerHTML = (response.stock_data.ts_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.ts_data.data >= 0)
            document.getElementById("ts_val_data").innerHTML = "+" + (response.stock_data.ts_data.data).toFixed(2) + " %";
        else
            document.getElementById("ts_val_data_neg").innerHTML = (response.stock_data.ts_data.data).toFixed(2) + " %";
        
        document.getElementById("vkpa_val_current").innerHTML = (response.stock_data.vkpa_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.vkpa_data.data >= 0)
            document.getElementById("vkpa_val_data").innerHTML = "+" + (response.stock_data.vkpa_data.data).toFixed(2) + " %";
        else
            document.getElementById("vkpa_val_data_neg").innerHTML = (response.stock_data.vkpa_data.data).toFixed(2) + " %";
    
        document.getElementById("tmst_val_current").innerHTML = (response.stock_data.tmst_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.tmst_data.data >= 0)
            document.getElementById("tmst_val_data").innerHTML = "+" + (response.stock_data.tmst_data.data).toFixed(2) + " %";
        else
            document.getElementById("tmst_val_data_neg").innerHTML = (response.stock_data.tmst_data.data).toFixed(2) + " %";    
    
        document.getElementById("nwpx_val_current").innerHTML = (response.stock_data.nwpx_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.nwpx_data.data >= 0)
            document.getElementById("nwpx_val_data").innerHTML = "+" + (response.stock_data.nwpx_data.data).toFixed(2) + " %";
        else
            document.getElementById("nwpx_val_data_neg").innerHTML = (response.stock_data.nwpx_data.data).toFixed(2) + " %";
        
    });

});