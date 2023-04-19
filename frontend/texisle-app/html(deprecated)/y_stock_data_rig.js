$(document).ready(function(){

    var settings = {
        "url": urlresource + "/y_stock_data/",
        "method": "GET",
        "timeout": 0,
    };

    $.ajax(settings).done(function (response) {

        document.getElementById("rc_val_current").innerHTML = (response.stock_data.rc_index.current);
        if (response.stock_data.rc_index.data >= 0)
            document.getElementById("rc_val_data").innerHTML = "+" + (response.stock_data.rc_index.data).toFixed(2) + " %";
        else
            document.getElementById("rc_val_data_neg").innerHTML = (response.stock_data.rc_index.data).toFixed(2) + " %";

        document.getElementById("ardmore_val_current").innerHTML = (response.stock_data.Ardmore_data.current);
        if (response.stock_data.Ardmore_data.data >= 0)
            document.getElementById("ardmore_val_data").innerHTML = "+" + (response.stock_data.Ardmore_data.data).toFixed(2) + " %";
        else
            document.getElementById("ardmore_val_data_neg").innerHTML = (response.stock_data.Ardmore_data.data).toFixed(2) + " %";

        document.getElementById("arkoma_val_current").innerHTML = (response.stock_data.Arkoma_data.current);
        if (response.stock_data.Arkoma_data.data >= 0)
            document.getElementById("arkoma_val_data").innerHTML = "+" + (response.stock_data.Arkoma_data.data).toFixed(2) + " %";
        else
            document.getElementById("arkoma_val_data_neg").innerHTML = (response.stock_data.Arkoma_data.data).toFixed(2) + " %";    

        document.getElementById("barnett_val_current").innerHTML = (response.stock_data.Barnett_data.current);
        if (response.stock_data.Barnett_data.data >= 0)
            document.getElementById("barnett_val_data").innerHTML = "+" + (response.stock_data.Barnett_data.data).toFixed(2) + " %";
        else
            document.getElementById("barnett_val_data_neg").innerHTML = (response.stock_data.Barnett_data.data).toFixed(2) + " %";
            
        document.getElementById("cana_val_current").innerHTML = (response.stock_data.Cana_data.current);
        if (response.stock_data.Cana_data.data >= 0)
            document.getElementById("cana_val_data").innerHTML = "+" + (response.stock_data.Cana_data.data).toFixed(2) + " %";
        else
            document.getElementById("cana_val_data_neg").innerHTML = (response.stock_data.Cana_data.data).toFixed(2) + " %";

        document.getElementById("niobrara_val_current").innerHTML = (response.stock_data.Niobrara_data.current);
        if (response.stock_data.Niobrara_data.data >= 0)
            document.getElementById("niobrara_val_data").innerHTML = "+" + (response.stock_data.Niobrara_data.data).toFixed(2) + " %";
        else
            document.getElementById("niobrara_val_data_neg").innerHTML = (response.stock_data.Niobrara_data.data).toFixed(2) + " %";    

        document.getElementById("ford_val_current").innerHTML = (response.stock_data.Ford_data.current);
        if (response.stock_data.Ford_data.data >= 0)
            document.getElementById("ford_val_data").innerHTML = "+" + (response.stock_data.Ford_data.data).toFixed(2) + " %";
        else
            document.getElementById("ford_val_data_neg").innerHTML = (response.stock_data.Ford_data.data).toFixed(2) + " %";    
        
        document.getElementById("granite_val_current").innerHTML = (response.stock_data.Granite_data.current);
        if (response.stock_data.Granite_data.data >= 0)
            document.getElementById("granite_val_data").innerHTML = "+" + (response.stock_data.Granite_data.data).toFixed(2) + " %";
        else
            document.getElementById("granite_val_data_neg").innerHTML = (response.stock_data.Granite_data.data).toFixed(2) + " %";    

        document.getElementById("haynesville_val_current").innerHTML = (response.stock_data.Haynesville_data.current);
        if (response.stock_data.Haynesville_data.data >= 0)
            document.getElementById("haynesville_val_data").innerHTML = "+" + (response.stock_data.Haynesville_data.data).toFixed(2) + " %";
        else
            document.getElementById("haynesville_val_data_neg").innerHTML = (response.stock_data.Haynesville_data.data).toFixed(2) + " %";    

        document.getElementById("marcellus_val_current").innerHTML = (response.stock_data.Marcellus_data.current);
        if (response.stock_data.Marcellus_data.data >= 0)
            document.getElementById("marcellus_val_data").innerHTML = "+" + (response.stock_data.Marcellus_data.data).toFixed(2) + " %";
        else
            document.getElementById("marcellus_val_data_neg").innerHTML = (response.stock_data.Marcellus_data.data).toFixed(2) + " %";    

        document.getElementById("mississippian_val_current").innerHTML = (response.stock_data.Mississippian_data.current);
        if (response.stock_data.Mississippian_data.data >= 0)
            document.getElementById("mississippian_val_data").innerHTML = "+" + (response.stock_data.Mississippian_data.data).toFixed(2) + " %";
        else
            document.getElementById("mississippian_val_data_neg").innerHTML = (response.stock_data.Mississippian_data.data).toFixed(2) + " %";    

        document.getElementById("permian_val_current").innerHTML = (response.stock_data.Permian_data.current);
        if (response.stock_data.Permian_data.data >= 0)
            document.getElementById("permian_val_data").innerHTML = "+" + (response.stock_data.Permian_data.data).toFixed(2) + " %";
        else
            document.getElementById("permian_val_data_neg").innerHTML = (response.stock_data.Permian_data.data).toFixed(2) + " %";    
            
        document.getElementById("utica_val_current").innerHTML = (response.stock_data.Utica_data.current);
        if (response.stock_data.Utica_data.data >= 0)
            document.getElementById("utica_val_data").innerHTML = "+" + (response.stock_data.Utica_data.data).toFixed(2) + " %";
        else
            document.getElementById("utica_val_data_neg").innerHTML = (response.stock_data.Utica_data.data).toFixed(2) + " %";    

        document.getElementById("williston_val_current").innerHTML = (response.stock_data.Williston_data.current);
        if (response.stock_data.Williston_data.data >= 0)
            document.getElementById("williston_val_data").innerHTML = "+" + (response.stock_data.Williston_data.data).toFixed(2) + " %";
        else
            document.getElementById("williston_val_data_neg").innerHTML = (response.stock_data.Williston_data.data).toFixed(2) + " %";    
    });

});