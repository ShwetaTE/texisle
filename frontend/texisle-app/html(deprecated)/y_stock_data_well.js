$(document).ready(function(){

    var settings = {
        "url": urlresource + "/y_stock_data/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function (response) {

        console.log(response)

        document.getElementById("dpr_duc_val_current").innerHTML = (response.stock_data.DPR_DUC.current);
        if (response.stock_data.DPR_DUC.data >= 0)
            document.getElementById("dpr_duc_val_data").innerHTML = "+" + (response.stock_data.DPR_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("dpr_duc_val_data_neg").innerHTML = (response.stock_data.DPR_DUC.data).toFixed(2) + " %";

        document.getElementById("Anadarko_duc_val_current").innerHTML = (response.stock_data.Anadarko_DUC.current);
        if (response.stock_data.Anadarko_DUC.data >= 0)
            document.getElementById("Anadarko_duc_val_data").innerHTML = "+" + (response.stock_data.Anadarko_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Anadarko_duc_val_data_neg").innerHTML = (response.stock_data.Anadarko_DUC.data).toFixed(2) + " %";

        document.getElementById("Appalachia_duc_val_current").innerHTML = (response.stock_data.Appalachia_DUC.current);
        if (response.stock_data.Appalachia_DUC.data >= 0)
            document.getElementById("Appalachia_duc_val_data").innerHTML = "+" + (response.stock_data.Appalachia_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Appalachia_duc_val_data_neg").innerHTML = (response.stock_data.Appalachia_DUC.data).toFixed(2) + " %";

        document.getElementById("Bakken_duc_val_current").innerHTML = (response.stock_data.Bakken_DUC.current);
        if (response.stock_data.Bakken_DUC.data >= 0)
            document.getElementById("Bakken_duc_val_data").innerHTML = "+" + (response.stock_data.Bakken_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Bakken_duc_val_data_neg").innerHTML = (response.stock_data.Bakken_DUC.data).toFixed(2) + " %";

        document.getElementById("Eagle_duc_val_current").innerHTML = (response.stock_data.Eagle_DUC.current);
        if (response.stock_data.Eagle_DUC.data >= 0)
            document.getElementById("Eagle_duc_val_data").innerHTML = "+" + (response.stock_data.Eagle_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Eagle_duc_val_data_neg").innerHTML = (response.stock_data.Eagle_DUC.data).toFixed(2) + " %";

        document.getElementById("Haynesville_duc_val_current").innerHTML = (response.stock_data.Haynesville_DUC.current);
        if (response.stock_data.Haynesville_DUC.data >= 0)
            document.getElementById("Haynesville_duc_val_data").innerHTML = "+" + (response.stock_data.Haynesville_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Haynesville_duc_val_data_neg").innerHTML = (response.stock_data.Haynesville_DUC.data).toFixed(2) + " %";

        document.getElementById("Niobrara_duc_val_current").innerHTML = (response.stock_data.Niobrara_DUC.current);
        if (response.stock_data.Niobrara_DUC.data >= 0)
            document.getElementById("Niobrara_duc_val_data").innerHTML = "+" + (response.stock_data.Niobrara_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Niobrara_duc_val_data_neg").innerHTML = (response.stock_data.Niobrara_DUC.data).toFixed(2) + " %";

        document.getElementById("Permian_duc_val_current").innerHTML = (response.stock_data.Permian_DUC.current);
        if (response.stock_data.Permian_DUC.data >= 0)
            document.getElementById("Permian_duc_val_data").innerHTML = "+" + (response.stock_data.Permian_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Permian_duc_val_data_neg").innerHTML = (response.stock_data.Permian_DUC.data).toFixed(2) + " %";

    });

});