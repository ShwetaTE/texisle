function save_watchlist_setting() {
    var temp = document.getElementById("up_msg");
    temp.style.display = 'none';
    var deviceID = sessionStorage.getItem("deviceID");
            if (deviceID==null){
            deviceID = device.uuid;
            sessionStorage.setItem("deviceID", deviceID);
            }
    var values = [];
    var cbs = document.forms['tickers'].elements['ticker'];
    for (var i = 0, cbLen = cbs.length; i < cbLen; i++) {
        if (cbs[i].checked) {
            values.push(cbs[i].value);
        }
    }
    // console.log(values)
    var deviceID = sessionStorage.getItem("deviceID");
            if (deviceID==null){
            deviceID = device.uuid;
            sessionStorage.setItem("deviceID", deviceID);
            }
    var settings = {
        "url": urlresource + "/add_watchlist/",
        "method": "POST",
        "timeout": 0,
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false, "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "chart_list": values,
            "deviceID": deviceID,
            "app_type": app_type
        }),
    };

    $.ajax(settings).done(function (response) {
        // console.log(response);
        temp.style.display = 'block';
    });
}


function create_divs(config_list) {
    // console.log(config_list)
    if(config_list.length == 0){
        var ticker_div = "<br><br<p class='text-muted font-weight-bold title_css'>No tickers are added to the watchlist.</p>";
        $("#watchlistDiv").append(ticker_div);
    }
    else{
        var settings = {
            "url": urlresource + "/y_stock_data/",
            "method": "GET",
            "timeout": 0,
            "dataType": 'JSON',
        };
    
        $.ajax(settings).done(function (response) {
            stock = (response.stock_data);
            $.each(config_list, function (key, value) {
                var ticker = ['SCRAP', 'HRC', 'COAL', 'IRONORE', 'RMI_index', 'RIO', 'VALE', 'SXC', 'BHP', 'IOM_index', 'TS', 'VKPA', 'X', 'TMST', 'NWPX', 'PMF_index', 'MT', 'PKX', 'NUE', 'STLD', 'RS', 'CLF', 'TX', 'GGB', 'CMC', 'TKADE', 'SZGDE', 'NIPPON', 'JFE', 'SMF_index', 'Baltic', 'ULSD', 'AllGrade', 'CassFreight', 'Truck', 'T_index', 'Ardmore', 'Arkoma', 'Barnett', 'Cana', 'Niobrara', 'Ford', 'Granite', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston', 'RC_index', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC']
                let index = ticker.indexOf(value);
                var ticker_name = ['SCRAP', 'HRC', 'Coal', 'IronOre', 'Raw Materials', 'XNYS: RIO', 'XNYS: VALE', 'XNYS: SXC', 'XNYS: BHP', 'Mining Companies', 'XNYS: TS', 'XPAR: VK.PA', 'XNYS: X', 'XNYS: TMST', 'XNAS: NWPX', 'Pipe Manufacturing', 'XNYS: MT', 'XNYS: PKX', 'XNYS: NUE', 'XNYS: STLD', 'XNYS: RS', 'XNYS: CLF', 'XNYS: TX', 'XNYS: GGB', 'XNYS: CMC', 'XETR: TKA.DE', 'XETR: SZG.DE', 'XTKS: Nippon', 'XTKS: JFE', 'Steel Manufacturing', 'BADI', 'ULSD', 'All Grdes', 'CassFreight', 'Truck', 'Transportation', 'Ardmore Woodford', 'Arkoma Woodford', 'Barnett', 'Cana Woodford', 'DJ-Niobrara', 'Eagle Ford', 'Granite Wash', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston', 'US&nbspTotal', 'Anadarko', 'Appalachia', 'Bakken', 'Eagle Ford', 'Haynesville', 'Niobrara', 'Permian', 'DPR Regions']
                var ticker_full_name = ['Scrap: Spot & Future', 'Hot Rolled Coil: Spot & Future', 'Coal: Spot & Future', 'Iron Ore: Spot & Future', '', 'RIO TINTO PLC', 'Vale SA', 'SUNCOKE ENERGY, INC.', 'BHP Group', '', 'Tenaris SA', 'Vallourec SA', 'UNITED STATES STEEL CORPORATION', 'TIMKENSTEEL CORPORATION', 'Northwest Pipe Company', '', 'ArcelorMittal SA', 'POSCO', 'NUCOR CORPORATION', 'STEEL DYNAMICS, INC.', 'RELIANCE STEEL & ALUMINUM CO.', 'CLEVELAND-CLIFFS INC.', 'Ternium SA', 'Gerdau SA', 'COMMERCIAL METALS COMPANY', 'Thyssenkrupp AG', 'Salzgitter AG', 'Nippon Steel Corporation', 'JFE Holdings, Inc.', '', 'Baltic Dry Index', 'U.S. Ultra-Low Sulfur No 2 Diesel', 'All Grade: Gasoline', 'CassFreight Index', 'Truck transportation', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count', 'Rig Count',    'Well Count', 'Well Count', 'Well Count', 'Well Count', 'Well Count', 'Well Count', 'Well Count', 'Well Count']
                var container_name = ["1_1", "1_2", "1_3", "1_4", "_raw_material_index", "4_1", "4_2", "4_3", "4_4", "_iron_ore_mining_index", "2_1", "2_2", "2_3", "2_4", "2_5", "_pipe_manufacturing_index", "3_1", "3_2", "3_3", "3_4", "3_5", "3_6", "3_7", "3_8", "3_10", "3_12", "3_13", "3_14", "3_15", "_steel_manufacturing_index", "5_2", "5_1", "5_5", "5_4", "5_3", "_transport_index", "6_1", "6_2", "6_3", "6_4", "6_5", "6_6", "6_7", "6_8", "6_9", "6_10", "6_11", "6_12", "6_13", "_rc_index", "_7_1", "_7_2", "_7_3", "_7_4", "_7_5", "_7_6", "_7_7", "_dpr_index"]
                var script_name = ["raw_material_index/chart_scrap.js", "raw_material_index/chart_hrc.js", "raw_material_index/chart_coal.js", "raw_material_index/chart_iron.js", "raw_material_index.js", "iron_ore/chart_rio.js", "iron_ore/chart_vale.js", "iron_ore/chart_sxc.js", "iron_ore/chart_bhp.js", "iron_ore_mining_index.js", "pipe_manufacturing/chart_ts.js", "pipe_manufacturing/chart_vkpa.js", "pipe_manufacturing/chart_x.js", "pipe_manufacturing/chart_tmst.js", "pipe_manufacturing/chart_nwpx.js", "pipe_manufacturing_index.js", "steel_manufacturing/chart_mt.js", "steel_manufacturing/chart_pkx.js", "steel_manufacturing/chart_nue.js", "steel_manufacturing/chart_stld.js", "steel_manufacturing/chart_rs.js", "steel_manufacturing/chart_clf.js", "steel_manufacturing/chart_tx.js", "steel_manufacturing/chart_ggb.js", "steel_manufacturing/chart_cmc.js", "steel_manufacturing/chart_tkade.js", "steel_manufacturing/chart_szgde.js", "steel_manufacturing/chart_nippon.js", "steel_manufacturing/chart_jfe.js", "steel_manufacturing_index.js", "transportation/chart_baltic.js", "transportation/chart_usld.js", "transportation/chart_allgrade.js", "transportation/chart_cf.js", "transportation/chart_truck.js", "transport_index.js", "rig_count/chart_ardmore.js", "rig_count/chart_arkoma.js", "rig_count/chart_barnett.js", "rig_count/chart_cana.js", "rig_count/chart_niobrara.js", "rig_count/chart_ford.js", "rig_count/chart_granite.js", "rig_count/chart_haynesville.js", "rig_count/chart_marcellus.js", "rig_count/chart_mississippian.js", "rig_count/chart_permian.js", "rig_count/chart_utica.js", "rig_count/chart_williston.js", "rig_count_index.js", "well_count/chart_Anadarko.js", "well_count/chart_Appalachia.js", "well_count/chart_Bakken.js", "well_count/chart_Eagle.js", "well_count/chart_Haynesville.js", "well_count/chart_Niobrara.js", "well_count/chart_Permian.js", "well_count_index.js"]
                var spot_name = ['scrap', 'hrc', 'coal', 'iron', 'rmi', 'rio', 'vale', 'sxc', 'bhp', 'io', 'ts', 'vkpa', 'x', 'tmst', 'nwpx', 'pm', 'mt', 'pkx', 'nue', 'stld', 'rs', 'clf', 'tx', 'ggb', 'cmc', 'tkade', 'szgde', 'nippon', 'jfe', 'smf', 'baltic', 'usld', 'ag', 'cf', 'truck', 't', 'ardmore', 'arkoma', 'barnett', 'cana', 'niobrara', 'ford', 'granite', 'haynesville', 'marcellus', 'mississippian', 'permian', 'utica', 'williston', 'rc', 'Anadarko_duc', 'Appalachia_duc', 'Bakken_duc', 'Eagle_duc', 'Haynesville_duc', 'Niobrara_duc', 'Permian_duc', 'dpr_duc']
                
                // console.log(ticker[index])
                // console.log(ticker_name[index])
                // console.log(ticker_full_name[index])
                // console.log(container_name[index])
                // console.log(spot_name[index])

                int_ticker = ['Ardmore', 'Arkoma', 'Barnett', 'Cana', 'Niobrara', 'Ford', 'Granite', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston', 'RC_index', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC']
                if(int_ticker.includes(value)==true){
                    spot_string = '<span id="' + spot_name[index] + '_val_current" class="spot_val_int"></span><br>';
                }
                else {
                    spot_string = '<span id="' + spot_name[index] + '_val_current" class="spot_val"></span><br>';
                }

                var ticker_div =
                    '<div onclick="openLink(\''+ value +'\')" class="d-flex align-items-center flex-row-fluid flex-wrap style="width: 100%;">' +
                    '<div class="flex-grow-0 me-2" style="width: 42%;">' +
                    '<a class="text-white text-hover-primary font-weight-bolder" style="font-size: medium;">' + ticker_name[index] + '</a><br>' +
                    '<span class="text-muted font-weight-bold">' + ticker_full_name[index] + '</span>' +
                    '</div>' +
                    '<span style="width: 30%;">' +
                    '<figure class="highcharts-figure">' +
                    '<div id="container' + container_name[index] + '"></div>' +
                    '</figure>' +
                    '</span>' +
                    '<span class="pl-7 py-2" style="width: 28%;">' +
                    // '<span id="' + spot_name[index] + '_val_current" class="spot_val"></span><br>' +
                    spot_string +
                    '<div class="boxed_red">' +
                    '<span id="' + spot_name[index] + '_val_data_neg" class="spot_diff"></span>' +
                    '</div>' +
                    '<div class="boxed_green">' +
                    '<span id="' + spot_name[index] + '_val_data" class="spot_diff"></span>' +
                    '</div>' +
                    '</span>' +
                    '</div>' +
                    '<hr style="border-top: 0.5px solid #565450;margin-bottom: 0rem;margin-top: 0rem;margin-left: -3%; margin-right: -3%;"></hr>'
    
                $("#watchlistDiv").append(ticker_div);
    
                stock_data_watchlist(stock, index);
    
                loadScript("js/chart/" + script_name[index])
    
            });
        });
    }

}

function loadScript(url) {
    document.body.appendChild(document.createElement("script")).src = url;
}

function stock_data_watchlist(stock, index) {
    var spot_name = ['scrap', 'hrc', 'coal', 'iron', 'rmi', 'rio', 'vale', 'sxc', 'bhp', 'io', 'ts', 'vkpa', 'x', 'tmst', 'nwpx', 'pm', 'mt', 'pkx', 'nue', 'stld', 'rs', 'clf', 'tx', 'ggb', 'cmc', 'tkade', 'szgde', 'nippon', 'jfe', 'smf', 'baltic', 'usld', 'ag', 'cf', 'truck', 't', 'ardmore', 'arkoma', 'barnett', 'cana', 'niobrara', 'ford', 'granite', 'haynesville', 'marcellus', 'mississippian', 'permian', 'utica', 'williston', 'rc', 'Anadarko_duc', 'Appalachia_duc', 'Bakken_duc', 'Eagle_duc', 'Haynesville_duc', 'Niobrara_duc', 'Permian_duc', 'dpr_duc']
    var list = ['scrap_data', 'hrc_data', 'coal_data', 'iron_data', 'raw_material_index', 'rio_data', 'vale_data', 'sxc_data', 'bhp_data', 'iron_ore', 'ts_data', 'vkpa_data', 'x_data', 'tmst_data', 'nwpx_data', 'pipe_manufacturing', 'mt_data', 'pkx_data', 'nue_data', 'stld_data', 'rs_data', 'clf_data', 'tx_data', 'ggb_data', 'cmc_data', 'tkade_data', 'szgde_data', 'nippon_data', 'jfe_data', 'steel_manufacturing', 'baltic_data', 'usld_data', 'ag_data', 'cf_data', 'truck_data', 't_index', 'Ardmore_data', 'Arkoma_data', 'Barnett_data', 'Cana_data', 'Niobrara_data', 'Ford_data', 'Granite_data', 'Haynesville_data', 'Marcellus_data', 'Mississippian_data', 'Permian_data', 'Utica_data', 'Williston_data', 'rc_index', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC'  ]
    var data_name = list[index]
    // console.log(index)
    // console.log(data_name)
    int_ticker = ['Ardmore_data', 'Arkoma_data', 'Barnett_data', 'Cana_data', 'Niobrara_data', 'Ford_data', 'Granite_data', 'Haynesville_data', 'Marcellus_data', 'Mississippian_data', 'Permian_data', 'Utica_data', 'Williston_data', 'rc_index', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC']
    if(int_ticker.includes(data_name)==true){
        document.getElementById(spot_name[index] + "_val_current").innerHTML = (stock[data_name]["current"]);
        if (stock[data_name]["data"] >= 0)
            document.getElementById(spot_name[index] + "_val_data").innerHTML = "+" + (stock[data_name]["data"]);
        else
            document.getElementById(spot_name[index] + "_val_data_neg").innerHTML = (stock[data_name]["data"]);

    }
    else {
            
        document.getElementById(spot_name[index] + "_val_current").innerHTML = (stock[data_name]["current"]).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        if (stock[data_name]["data"] >= 0)
            document.getElementById(spot_name[index] + "_val_data").innerHTML = "+" + (stock[data_name]["data"]).toFixed(2) + " %";
        else
            document.getElementById(spot_name[index] + "_val_data_neg").innerHTML = (stock[data_name]["data"]).toFixed(2) + " %";
    }
}

function add_to_watchlist(x, chart){
    // console.log(typeof(x))
    var deviceID = sessionStorage.getItem("deviceID");
            if (deviceID==null){
            deviceID = device.uuid;
            sessionStorage.setItem("deviceID", deviceID);
            }
    var form = new FormData();
    form.append("app_type", app_type);
    form.append("deviceID", deviceID);
    form.append("chart", chart);

    var settings = {
    "url": urlresource +"/update_watchlist/",
    "method": "POST",
    "timeout": 0,
    "processData": false,
    "mimeType": "multipart/form-data",
    "contentType": false,
    "data": form
    };

    $.ajax(settings).done(function (response) {
        // console.log(response);
        x.classList.toggle('fa-eye');
        x.classList.toggle('fa-eye-slash');

    });
}

function check_each_page(index_list){
    var deviceID = sessionStorage.getItem("deviceID");
            if (deviceID==null){
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
            console.log(response);
            var config_list = response.chart_list;
			
			for(i = 0; i < index_list.length; i++){
				if(config_list.includes(index_list[i])==true){
					console.log("#WL_"+index_list[i])
					var v = document.getElementById("WL_"+index_list[i])
					v.classList.toggle('fa-eye');
					v.classList.toggle('fa-eye-slash');
				}	
			}
        });
}