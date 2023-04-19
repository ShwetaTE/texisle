$(document).ready(function () {

    var settings = {
        "url": urlresource + "/y_stock_data/",
        // "url": urlresource + "/y_stock_data/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function (response) {
        // console.log(response);
        document.getElementById("rmi_val_current").innerHTML = (response.stock_data.raw_material_index.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.raw_material_index.data >= 0)
            document.getElementById("rmi_val_data").innerHTML = "+" + (response.stock_data.raw_material_index.data).toFixed(2) + " %";
        else
            document.getElementById("rmi_val_data_neg").innerHTML = (response.stock_data.raw_material_index.data).toFixed(2) + " %";
             
        document.getElementById("coal_val_current").innerHTML = (response.stock_data.coal_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.coal_data.data >= 0)
            document.getElementById("coal_val_data").innerHTML = "+" + (response.stock_data.coal_data.data).toFixed(2) + " %";
        else
            document.getElementById("coal_val_data_neg").innerHTML = (response.stock_data.coal_data.data).toFixed(2) + " %";

        document.getElementById("scrap_val_current").innerHTML = (response.stock_data.scrap_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.scrap_data.data >= 0)
            document.getElementById("scrap_val_data").innerHTML = "+" + (response.stock_data.scrap_data.data).toFixed(2) + " %";
        else
            document.getElementById("scrap_val_data_neg").innerHTML = (response.stock_data.scrap_data.data).toFixed(2) + " %";

        document.getElementById("hrc_val_current").innerHTML = (response.stock_data.hrc_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.hrc_data.data >= 0)
            document.getElementById("hrc_val_data").innerHTML = "+" + (response.stock_data.hrc_data.data).toFixed(2) + " %";
        else
            document.getElementById("hrc_val_data_neg").innerHTML = (response.stock_data.hrc_data.data).toFixed(2) + " %";

        document.getElementById("iron_val_current").innerHTML = (response.stock_data.iron_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.iron_data.data >= 0)
            document.getElementById("iron_val_data").innerHTML = "+" + (response.stock_data.iron_data.data).toFixed(2) + " %";
        else
            document.getElementById("iron_val_data_neg").innerHTML = (response.stock_data.iron_data.data).toFixed(2) + " %";
    });
});