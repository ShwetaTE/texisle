$(document).ready(function(){

    var settings = {
        "url": urlresource + "/y_stock_data/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function (response) {
        console.log(response)
        // console.log(response.stock_data.scrap_data.current);
        document.getElementById("smf_val_current").innerHTML = (response.stock_data.steel_manufacturing.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.steel_manufacturing.data >= 0)
            document.getElementById("smf_val_data").innerHTML = "+" + (response.stock_data.steel_manufacturing.data).toFixed(2) + " %";
        else
            document.getElementById("smf_val_data_neg").innerHTML = (response.stock_data.steel_manufacturing.data).toFixed(2) + " %";

        document.getElementById("stld_val_current").innerHTML = (response.stock_data.stld_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.stld_data.data >= 0)
            document.getElementById("stld_val_data").innerHTML = "+" + (response.stock_data.stld_data.data).toFixed(2) + " %";
        else
            document.getElementById("stld_val_data_neg").innerHTML = (response.stock_data.stld_data.data).toFixed(2) + " %";

        document.getElementById("rs_val_current").innerHTML = (response.stock_data.rs_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.rs_data.data >= 0)
            document.getElementById("rs_val_data").innerHTML = "+" + (response.stock_data.rs_data.data).toFixed(2) + " %";
        else
            document.getElementById("rs_val_data_neg").innerHTML = (response.stock_data.rs_data.data).toFixed(2) + " %";

        document.getElementById("clf_val_current").innerHTML = (response.stock_data.clf_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.clf_data.data >= 0)
            document.getElementById("clf_val_data").innerHTML = "+" + (response.stock_data.clf_data.data).toFixed(2) + " %";
        else
            document.getElementById("clf_val_data_neg").innerHTML = (response.stock_data.clf_data.data).toFixed(2) + " %";

        document.getElementById("tx_val_current").innerHTML = (response.stock_data.tx_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.tx_data.data >= 0)
            document.getElementById("tx_val_data").innerHTML = "+" + (response.stock_data.tx_data.data).toFixed(2) + " %";
        else
            document.getElementById("tx_val_data_neg").innerHTML = (response.stock_data.tx_data.data).toFixed(2) + " %";
        
        document.getElementById("ggb_val_current").innerHTML = (response.stock_data.ggb_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.ggb_data.data >= 0)
            document.getElementById("ggb_val_data").innerHTML = "+" + (response.stock_data.ggb_data.data).toFixed(2) + " %";
        else
            document.getElementById("ggb_val_data_neg").innerHTML = (response.stock_data.ggb_data.data).toFixed(2) + " %";
        
        document.getElementById("x_val_current").innerHTML = (response.stock_data.x_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.x_data.data >= 0)
            document.getElementById("x_val_data").innerHTML = "+" + (response.stock_data.x_data.data).toFixed(2) + " %";
        else
            document.getElementById("x_val_data_neg").innerHTML = (response.stock_data.x_data.data).toFixed(2) + " %";
        
        document.getElementById("cmc_val_current").innerHTML = (response.stock_data.cmc_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.cmc_data.data >= 0)
            document.getElementById("cmc_val_data").innerHTML = "+" + (response.stock_data.cmc_data.data).toFixed(2) + " %";
        else
            document.getElementById("cmc_val_data_neg").innerHTML = (response.stock_data.cmc_data.data).toFixed(2) + " %";
        
        document.getElementById("mt_val_current").innerHTML = (response.stock_data.mt_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.mt_data.data >= 0)
            document.getElementById("mt_val_data").innerHTML = "+" + (response.stock_data.mt_data.data).toFixed(2) + " %";
        else
            document.getElementById("mt_val_data_neg").innerHTML = (response.stock_data.mt_data.data).toFixed(2) + " %";
        
        document.getElementById("nue_val_current").innerHTML = (response.stock_data.nue_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
            if (response.stock_data.nue_data.data >= 0)
                document.getElementById("nue_val_data").innerHTML = "+" + (response.stock_data.nue_data.data).toFixed(2) + " %";
            else
                document.getElementById("nue_val_data_neg").innerHTML = (response.stock_data.nue_data.data).toFixed(2) + " %";
        
        document.getElementById("pkx_val_current").innerHTML = (response.stock_data.pkx_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.pkx_data.data >= 0)
            document.getElementById("pkx_val_data").innerHTML = "+" + (response.stock_data.pkx_data.data).toFixed(2) + " %";
        else
            document.getElementById("pkx_val_data_neg").innerHTML = (response.stock_data.pkx_data.data).toFixed(2) + " %";
        
        document.getElementById("tkade_val_current").innerHTML = (response.stock_data.tkade_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.tkade_data.data >= 0)
            document.getElementById("tkade_val_data").innerHTML = "+" + (response.stock_data.tkade_data.data).toFixed(2) + " %";
        else
            document.getElementById("tkade_val_data_neg").innerHTML = (response.stock_data.tkade_data.data).toFixed(2) + " %";
        
        document.getElementById("szgde_val_current").innerHTML = (response.stock_data.szgde_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.szgde_data.data >= 0)
            document.getElementById("szgde_val_data").innerHTML = "+" + (response.stock_data.szgde_data.data).toFixed(2) + " %";
        else
            document.getElementById("szgde_val_data_neg").innerHTML = (response.stock_data.szgde_data.data).toFixed(2) + " %";
        
        document.getElementById("nippon_val_current").innerHTML = (response.stock_data.nippon_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.nippon_data.data >= 0)
            document.getElementById("nippon_val_data").innerHTML = "+" + (response.stock_data.nippon_data.data).toFixed(2) + " %";
        else
            document.getElementById("nippon_val_data_neg").innerHTML = (response.stock_data.nippon_data.data).toFixed(2) + " %";
        
        document.getElementById("jfe_val_current").innerHTML = (response.stock_data.jfe_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (response.stock_data.jfe_data.data >= 0)
            document.getElementById("jfe_val_data").innerHTML = "+" + (response.stock_data.jfe_data.data).toFixed(2) + " %";
        else
            document.getElementById("jfe_val_data_neg").innerHTML = (response.stock_data.jfe_data.data).toFixed(2) + " %";
        
    });

});