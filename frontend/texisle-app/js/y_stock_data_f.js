$(document).ready(function(){

    var settings = {
        "url": urlresource + "/y_stock_data/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function (response) {
        console.log(response)
        // console.log(response.stock_data.scrap_data.current);
        document.getElementById("f_val_current").innerHTML = (response.stock_data.fuel.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.fuel.data >= 0)
            document.getElementById("f_val_data").innerHTML = "+" + (response.stock_data.fuel.data).toFixed(2) + " %";
        else
            document.getElementById("f_val_data_neg").innerHTML = (response.stock_data.fuel.data).toFixed(2) + " %";

        document.getElementById("hof_val_current").innerHTML = (response.stock_data.hof_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.hof_data.data >= 0)
            document.getElementById("hof_val_data").innerHTML = "+" + (response.stock_data.hof_data.data).toFixed(2) + " %";
        else
            document.getElementById("hof_val_data_neg").innerHTML = (response.stock_data.hof_data.data).toFixed(2) + " %";

        document.getElementById("rbf_val_current").innerHTML = (response.stock_data.rbf_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.rbf_data.data >= 0)
            document.getElementById("rbf_val_data").innerHTML = "+" + (response.stock_data.rbf_data.data).toFixed(2) + " %";
        else
            document.getElementById("rbf_val_data_neg").innerHTML = (response.stock_data.rbf_data.data).toFixed(2) + " %";    

        // document.getElementById("sxc_val_current").innerHTML = (response.stock_data.sxc_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        // if (response.stock_data.sxc_data.data >= 0)
        //     document.getElementById("sxc_val_data").innerHTML = "+" + (response.stock_data.sxc_data.data).toFixed(2) + " %";
        // else
        //     document.getElementById("sxc_val_data_neg").innerHTML = (response.stock_data.sxc_data.data).toFixed(2) + " %";    

        // document.getElementById("vale_val_current").innerHTML = (response.stock_data.vale_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        // if (response.stock_data.vale_data.data >= 0)
        //     document.getElementById("vale_val_data").innerHTML = "+" + (response.stock_data.vale_data.data).toFixed(2) + " %";
        // else
        //     document.getElementById("vale_val_data_neg").innerHTML = (response.stock_data.vale_data.data).toFixed(2) + " %";    

        // document.getElementById("bhp_val_current").innerHTML = (response.stock_data.bhp_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        // if (response.stock_data.bhp_data.data >= 0)
        //     document.getElementById("bhp_val_data").innerHTML = "+" + (response.stock_data.bhp_data.data).toFixed(2) + " %";
        // else
        //     document.getElementById("bhp_val_data_neg").innerHTML = (response.stock_data.bhp_data.data).toFixed(2) + " %";    
    
    });

});