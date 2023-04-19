$(document).ready(function(){

    var settings = {
        "url": urlresource + "/y_stock_data/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function (response) {
        // console.log(response)
        // console.log(response.stock_data.scrap_data.current);
        document.getElementById("t_val_current").innerHTML = (response.stock_data.t_index.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.t_index.data >= 0)
            document.getElementById("t_val_data").innerHTML = "+" + (response.stock_data.t_index.data).toFixed(2) + " %";
        else
            document.getElementById("t_val_data_neg").innerHTML = (response.stock_data.t_index.data).toFixed(2) + " %";

        document.getElementById("usld_val_current").innerHTML = (response.stock_data.usld_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.usld_data.data >= 0)
            document.getElementById("usld_val_data").innerHTML = "+" + (response.stock_data.usld_data.data).toFixed(2) + " %";
        else
            document.getElementById("usld_val_data_neg").innerHTML = (response.stock_data.usld_data.data).toFixed(2) + " %";

        document.getElementById("baltic_val_current").innerHTML = (response.stock_data.baltic_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.baltic_data.data >= 0)
            document.getElementById("baltic_val_data").innerHTML = "+" + (response.stock_data.baltic_data.data).toFixed(2) + " %";
        else
            document.getElementById("baltic_val_data_neg").innerHTML = (response.stock_data.baltic_data.data).toFixed(2) + " %";    

        document.getElementById("truck_val_current").innerHTML = (response.stock_data.truck_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.truck_data.data >= 0)
            document.getElementById("truck_val_data").innerHTML = "+" + (response.stock_data.truck_data.data).toFixed(2) + " %";
        else
            document.getElementById("truck_val_data_neg").innerHTML = (response.stock_data.truck_data.data).toFixed(2) + " %";    

        document.getElementById("cf_val_current").innerHTML = (response.stock_data.cf_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.cf_data.data >= 0)
            document.getElementById("cf_val_data").innerHTML = "+" + (response.stock_data.cf_data.data).toFixed(2) + " %";
        else
            document.getElementById("cf_val_data_neg").innerHTML = (response.stock_data.cf_data.data).toFixed(2) + " %";    

        document.getElementById("ag_val_current").innerHTML = (response.stock_data.ag_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.ag_data.data >= 0)
            document.getElementById("ag_val_data").innerHTML = "+" + (response.stock_data.ag_data.data).toFixed(2) + " %";
        else
            document.getElementById("ag_val_data_neg").innerHTML = (response.stock_data.ag_data.data).toFixed(2) + " %";    
    
    });

});