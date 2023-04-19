$(document).ready(function(){

    var settings = {
        "url": urlresource + "/y_stock_data/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function (response) {
        // console.log(response)
        // console.log(response.stock_data.scrap_data.current);
        document.getElementById("io_val_current").innerHTML = (response.stock_data.iron_ore.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.iron_ore.data >= 0)
            document.getElementById("io_val_data").innerHTML = "+" + (response.stock_data.iron_ore.data).toFixed(2) + " %";
        else
            document.getElementById("io_val_data_neg").innerHTML = (response.stock_data.iron_ore.data).toFixed(2) + " %";

        document.getElementById("rio_val_current").innerHTML = (response.stock_data.rio_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.rio_data.data >= 0)
            document.getElementById("rio_val_data").innerHTML = "+" + (response.stock_data.rio_data.data).toFixed(2) + " %";
        else
            document.getElementById("rio_val_data_neg").innerHTML = (response.stock_data.rio_data.data).toFixed(2) + " %";    

        document.getElementById("sxc_val_current").innerHTML = (response.stock_data.sxc_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.sxc_data.data >= 0)
            document.getElementById("sxc_val_data").innerHTML = "+" + (response.stock_data.sxc_data.data).toFixed(2) + " %";
        else
            document.getElementById("sxc_val_data_neg").innerHTML = (response.stock_data.sxc_data.data).toFixed(2) + " %";    

        document.getElementById("vale_val_current").innerHTML = (response.stock_data.vale_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.vale_data.data >= 0)
            document.getElementById("vale_val_data").innerHTML = "+" + (response.stock_data.vale_data.data).toFixed(2) + " %";
        else
            document.getElementById("vale_val_data_neg").innerHTML = (response.stock_data.vale_data.data).toFixed(2) + " %";    

        document.getElementById("bhp_val_current").innerHTML = (response.stock_data.bhp_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.bhp_data.data >= 0)
            document.getElementById("bhp_val_data").innerHTML = "+" + (response.stock_data.bhp_data.data).toFixed(2) + " %";
        else
            document.getElementById("bhp_val_data_neg").innerHTML = (response.stock_data.bhp_data.data).toFixed(2) + " %";    
    
    });

});