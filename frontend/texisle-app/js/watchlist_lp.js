$(document).ready(function(){
    var ticker = ['SCRAP', 'HRC', 'COAL', 'IRONORE', 'RMI_index', 'RIO', 'VALE', 'SXC', 'BHP', 'IOM_index', 'TS', 'VKPA', 'X', 'TMST', 'NWPX', 'PMF_index', 'MT', 'PKX', 'NUE', 'STLD', 'RS', 'CLF', 'TX', 'GGB', 'CMC', 'TKADE', 'SZGDE', 'NIPPON', 'JFE', 'SMF_index', 'Baltic', 'ULSD', 'AllGrade', 'CassFreight', 'Truck', 'T_index','Ardmore', 'Arkoma', 'Barnett', 'Cana', 'Niobrara', 'Ford', 'Granite', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston', 'RC_index', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC']
    check_landing_page(ticker)

});


function check_landing_page(index_list) {
    var deviceID = sessionStorage.getItem("deviceID");
    if (deviceID == null) {
        deviceID = device.uuid;
        sessionStorage.setItem("deviceID", deviceID);
    }
    var form = new FormData();
    form.append("app_type", app_type);
    form.append("deviceID", deviceID);

    var settings = {
        "url": urlresource + "/watchlist_config/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "mimeType": "multipart/form-data",
        "dataType": 'JSON',
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        // console.log(response);
        var config_list = response.chart_list;

        for (i = 0; i < index_list.length; i++) {
            if (config_list.includes(index_list[i]) == true) {
                // console.log("#WL_" + index_list[i])
                var v = document.getElementById("WL_" + index_list[i])
                v.style.backgroundColor = "red";
                v.querySelector('ion-icon').setAttribute('name', 'eye-off');
                if (index_list[i] == 'X') {
                    // console.log("#WL_" + index_list[i] + '1')
                    var v = document.getElementById("WL_" + index_list[i] + '1')
                    v.style.backgroundColor = "red";
                    v.querySelector('ion-icon').setAttribute('name', 'eye-off');
                }
            }
        }
    });
}