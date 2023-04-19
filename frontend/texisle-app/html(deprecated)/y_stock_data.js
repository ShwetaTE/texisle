$(document).ready(function(){
    try{
        // var stock = []
        try{
            var stock = JSON.parse(window.localStorage.getItem("stock"));
        }
        catch(err){
            console.log(err)
            var settings = {
                "url": urlresource + "/y_stock_data/",
                "method": "GET",
                "timeout": 0,
                "dataType": 'JSON',
            };
            
            $.ajax(settings).done(function (response) {
                
                var stock = (response);
                // document.cookie = "stock="+ JSON.stringify(stock) +";";
                window.localStorage.setItem("stock",JSON.stringify(stock));
                location.reload();
                
            });
        }
        console.log(stock)

        document.getElementById("rmi_val_current1").innerHTML = (stock.raw_material_index.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.raw_material_index.data >= 0)
            document.getElementById("rmi_val_data1").innerHTML = "+" + (stock.raw_material_index.data).toFixed(2) + " %";
        else
            document.getElementById("rmi_val_data_neg1").innerHTML = (stock.raw_material_index.data).toFixed(2) + " %";
                        
        document.getElementById("pm_val_current1").innerHTML = (stock.pipe_manufacturing.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.pipe_manufacturing.data >= 0)
            document.getElementById("pm_val_data1").innerHTML = "+" + (stock.pipe_manufacturing.data).toFixed(2) + " %";
        else
            document.getElementById("pm_val_data_neg1").innerHTML = (stock.pipe_manufacturing.data).toFixed(2) + " %";

        document.getElementById("smf_val_current1").innerHTML = (stock.steel_manufacturing.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.steel_manufacturing.data >= 0)
            document.getElementById("smf_val_data1").innerHTML = "+" + (stock.steel_manufacturing.data).toFixed(2) + " %";
        else
            document.getElementById("smf_val_data_neg1").innerHTML = (stock.steel_manufacturing.data).toFixed(2) + " %";
        
        document.getElementById("io_val_current1").innerHTML = (stock.iron_ore.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.iron_ore.data >= 0)
            document.getElementById("io_val_data1").innerHTML = "+" + (stock.iron_ore.data).toFixed(2) + " %";
        else
            document.getElementById("io_val_data_neg1").innerHTML = (stock.iron_ore.data).toFixed(2) + " %";

        document.getElementById("t_val_current1").innerHTML = (stock.t_index.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.t_index.data >= 0)
            document.getElementById("t_val_data1").innerHTML = "+" + (stock.t_index.data).toFixed(2) + " %";
        else
            document.getElementById("t_val_data_neg1").innerHTML = (stock.t_index.data).toFixed(2) + " %";
    
        document.getElementById("rc_val_current1").innerHTML = (stock.rc_index.current);
        if (stock.rc_index.data >= 0)
            document.getElementById("rc_val_data1").innerHTML = "+" + (stock.rc_index.data).toFixed(2) + " %";
        else
            document.getElementById("rc_val_data_neg1").innerHTML = (stock.rc_index.data).toFixed(2) + " %";
    
        document.getElementById("dpr_duc_val_current1").innerHTML = (stock.DPR_DUC.current);
        if (stock.DPR_DUC.data >= 0)
            document.getElementById("dpr_duc_val_data1").innerHTML = "+" + (stock.DPR_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("dpr_duc_val_data_neg1").innerHTML = (stock.DPR_DUC.data).toFixed(2) + " %";



        document.getElementById("rmi_val_current").innerHTML = (stock.raw_material_index.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.raw_material_index.data >= 0)
            document.getElementById("rmi_val_data").innerHTML = "+" + (stock.raw_material_index.data).toFixed(2) + " %";
        else
            document.getElementById("rmi_val_data_neg").innerHTML = (stock.raw_material_index.data).toFixed(2) + " %";
                        
        document.getElementById("pm_val_current").innerHTML = (stock.pipe_manufacturing.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.pipe_manufacturing.data >= 0)
            document.getElementById("pm_val_data").innerHTML = "+" + (stock.pipe_manufacturing.data).toFixed(2) + " %";
        else
            document.getElementById("pm_val_data_neg").innerHTML = (stock.pipe_manufacturing.data).toFixed(2) + " %";

        document.getElementById("smf_val_current").innerHTML = (stock.steel_manufacturing.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.steel_manufacturing.data >= 0)
            document.getElementById("smf_val_data").innerHTML = "+" + (stock.steel_manufacturing.data).toFixed(2) + " %";
        else
            document.getElementById("smf_val_data_neg").innerHTML = (stock.steel_manufacturing.data).toFixed(2) + " %";
        
        document.getElementById("io_val_current").innerHTML = (stock.iron_ore.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.iron_ore.data >= 0)
            document.getElementById("io_val_data").innerHTML = "+" + (stock.iron_ore.data).toFixed(2) + " %";
        else
            document.getElementById("io_val_data_neg").innerHTML = (stock.iron_ore.data).toFixed(2) + " %";

        document.getElementById("scrap_val_current").innerHTML = (stock.scrap_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.scrap_data.data >= 0)
            document.getElementById("scrap_val_data").innerHTML = "+" + (stock.scrap_data.data).toFixed(2) + " %";
        else
            document.getElementById("scrap_val_data_neg").innerHTML = (stock.scrap_data.data).toFixed(2) + " %";

        document.getElementById("hrc_val_current").innerHTML = (stock.hrc_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.hrc_data.data >= 0)
            document.getElementById("hrc_val_data").innerHTML = "+" + (stock.hrc_data.data).toFixed(2) + " %";
        else
            document.getElementById("hrc_val_data_neg").innerHTML = (stock.hrc_data.data).toFixed(2) + " %";

        document.getElementById("iron_val_current").innerHTML = (stock.iron_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.iron_data.data >= 0)
            document.getElementById("iron_val_data").innerHTML = "+" + (stock.iron_data.data).toFixed(2) + " %";
        else
            document.getElementById("iron_val_data_neg").innerHTML = (stock.iron_data.data).toFixed(2) + " %";
    
        document.getElementById("coal_val_current").innerHTML = (stock.coal_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.coal_data.data >= 0)
            document.getElementById("coal_val_data").innerHTML = "+" + (stock.coal_data.data).toFixed(2) + " %";
        else
            document.getElementById("coal_val_data_neg").innerHTML = (stock.coal_data.data).toFixed(2) + " %";

        document.getElementById("ts_val_current").innerHTML = (stock.ts_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.ts_data.data >= 0)
            document.getElementById("ts_val_data").innerHTML = "+" + (stock.ts_data.data).toFixed(2) + " %";
        else
            document.getElementById("ts_val_data_neg").innerHTML = (stock.ts_data.data).toFixed(2) + " %";
        
        document.getElementById("vkpa_val_current").innerHTML = (stock.vkpa_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.vkpa_data.data >= 0)
            document.getElementById("vkpa_val_data").innerHTML = "+" + (stock.vkpa_data.data).toFixed(2) + " %";
        else
            document.getElementById("vkpa_val_data_neg").innerHTML = (stock.vkpa_data.data).toFixed(2) + " %";
        
        document.getElementById("x_val_current").innerHTML = (stock.x_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.x_data.data >= 0)
            document.getElementById("x_val_data").innerHTML = "+" + (stock.x_data.data).toFixed(2) + " %";
        else
            document.getElementById("x_val_data_neg").innerHTML = (stock.x_data.data).toFixed(2) + " %";
        
        document.getElementById("tmst_val_current").innerHTML = (stock.tmst_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.tmst_data.data >= 0)
            document.getElementById("tmst_val_data").innerHTML = "+" + (stock.tmst_data.data).toFixed(2) + " %";
        else
            document.getElementById("tmst_val_data_neg").innerHTML = (stock.tmst_data.data).toFixed(2) + " %";    

        document.getElementById("mt_val_current").innerHTML = (stock.mt_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.mt_data.data >= 0)
            document.getElementById("mt_val_data").innerHTML = "+" + (stock.mt_data.data).toFixed(2) + " %";
        else
            document.getElementById("mt_val_data_neg").innerHTML = (stock.mt_data.data).toFixed(2) + " %";    

        document.getElementById("pkx_val_current").innerHTML = (stock.pkx_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.pkx_data.data >= 0)
            document.getElementById("pkx_val_data").innerHTML = "+" + (stock.pkx_data.data).toFixed(2) + " %";
        else
            document.getElementById("pkx_val_data_neg").innerHTML = (stock.pkx_data.data).toFixed(2) + " %";    

        document.getElementById("nue_val_current").innerHTML = (stock.nue_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.nue_data.data >= 0)
            document.getElementById("nue_val_data").innerHTML = "+" + (stock.nue_data.data).toFixed(2) + " %";
        else
            document.getElementById("nue_val_data_neg").innerHTML = (stock.nue_data.data).toFixed(2) + " %";    

        document.getElementById("stld_val_current").innerHTML = (stock.stld_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.stld_data.data >= 0)
            document.getElementById("stld_val_data").innerHTML = "+" + (stock.stld_data.data).toFixed(2) + " %";
        else
            document.getElementById("stld_val_data_neg").innerHTML = (stock.stld_data.data).toFixed(2) + " %";

        document.getElementById("rs_val_current").innerHTML = (stock.rs_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.rs_data.data >= 0)
            document.getElementById("rs_val_data").innerHTML = "+" + (stock.rs_data.data).toFixed(2) + " %";
        else
            document.getElementById("rs_val_data_neg").innerHTML = (stock.rs_data.data).toFixed(2) + " %";
                
        document.getElementById("clf_val_current").innerHTML = (stock.clf_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.clf_data.data >= 0)
            document.getElementById("clf_val_data").innerHTML = "+" + (stock.clf_data.data).toFixed(2) + " %";
        else
            document.getElementById("clf_val_data_neg").innerHTML = (stock.clf_data.data).toFixed(2) + " %";

        document.getElementById("tx_val_current").innerHTML = (stock.tx_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.tx_data.data >= 0)
            document.getElementById("tx_val_data").innerHTML = "+" + (stock.tx_data.data).toFixed(2) + " %";
        else
            document.getElementById("tx_val_data_neg").innerHTML = (stock.tx_data.data).toFixed(2) + " %";
        
        document.getElementById("ggb_val_current").innerHTML = (stock.ggb_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.ggb_data.data >= 0)
            document.getElementById("ggb_val_data").innerHTML = "+" + (stock.ggb_data.data).toFixed(2) + " %";
        else
            document.getElementById("ggb_val_data_neg").innerHTML = (stock.ggb_data.data).toFixed(2) + " %";
        
        document.getElementById("x_val_current_2").innerHTML = (stock.x_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.x_data.data >= 0)
            document.getElementById("x_val_data_2").innerHTML = "+" + (stock.x_data.data).toFixed(2) + " %";
        else
            document.getElementById("x_val_data_neg_2").innerHTML = (stock.x_data.data).toFixed(2) + " %";
        
        document.getElementById("cmc_val_current").innerHTML = (stock.cmc_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.cmc_data.data >= 0)
            document.getElementById("cmc_val_data").innerHTML = "+" + (stock.cmc_data.data).toFixed(2) + " %";
        else
            document.getElementById("cmc_val_data_neg").innerHTML = (stock.cmc_data.data).toFixed(2) + " %";
        
        document.getElementById("rio_val_current").innerHTML = (stock.rio_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.rio_data.data >= 0)
            document.getElementById("rio_val_data").innerHTML = "+" + (stock.rio_data.data).toFixed(2) + " %";
        else
            document.getElementById("rio_val_data_neg").innerHTML = (stock.rio_data.data).toFixed(2) + " %";    
        
        document.getElementById("vale_val_current").innerHTML = (stock.vale_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.vale_data.data >= 0)
            document.getElementById("vale_val_data").innerHTML = "+" + (stock.vale_data.data).toFixed(2) + " %";
        else
            document.getElementById("vale_val_data_neg").innerHTML = (stock.vale_data.data).toFixed(2) + " %";
            
        document.getElementById("sxc_val_current").innerHTML = (stock.sxc_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.sxc_data.data >= 0)
            document.getElementById("sxc_val_data").innerHTML = "+" + (stock.sxc_data.data).toFixed(2) + " %";
        else
            document.getElementById("sxc_val_data_neg").innerHTML = (stock.sxc_data.data).toFixed(2) + " %";    

        document.getElementById("bhp_val_current").innerHTML = (stock.bhp_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.bhp_data.data >= 0)
            document.getElementById("bhp_val_data").innerHTML = "+" + (stock.bhp_data.data).toFixed(2) + " %";
        else
            document.getElementById("bhp_val_data_neg").innerHTML = (stock.bhp_data.data).toFixed(2) + " %";    

        document.getElementById("nwpx_val_current").innerHTML = (stock.nwpx_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.nwpx_data.data >= 0)
            document.getElementById("nwpx_val_data").innerHTML = "+" + (stock.nwpx_data.data).toFixed(2) + " %";
        else
            document.getElementById("nwpx_val_data_neg").innerHTML = (stock.nwpx_data.data).toFixed(2) + " %";
        
        document.getElementById("tkade_val_current").innerHTML = (stock.tkade_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.tkade_data.data >= 0)
            document.getElementById("tkade_val_data").innerHTML = "+" + (stock.tkade_data.data).toFixed(2) + " %";
        else
            document.getElementById("tkade_val_data_neg").innerHTML = (stock.tkade_data.data).toFixed(2) + " %";
        
        document.getElementById("szgde_val_current").innerHTML = (stock.szgde_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.szgde_data.data >= 0)
            document.getElementById("szgde_val_data").innerHTML = "+" + (stock.szgde_data.data).toFixed(2) + " %";
        else
            document.getElementById("szgde_val_data_neg").innerHTML = (stock.szgde_data.data).toFixed(2) + " %";
        
        document.getElementById("nippon_val_current").innerHTML = (stock.nippon_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.nippon_data.data >= 0)
            document.getElementById("nippon_val_data").innerHTML = "+" + (stock.nippon_data.data).toFixed(2) + " %";
        else
            document.getElementById("nippon_val_data_neg").innerHTML = (stock.nippon_data.data).toFixed(2) + " %";
        
        document.getElementById("jfe_val_current").innerHTML = (stock.jfe_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.jfe_data.data >= 0)
            document.getElementById("jfe_val_data").innerHTML = "+" + (stock.jfe_data.data).toFixed(2) + " %";
        else
            document.getElementById("jfe_val_data_neg").innerHTML = (stock.jfe_data.data).toFixed(2) + " %";
        
        document.getElementById("usld_val_current").innerHTML = (stock.usld_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.usld_data.data >= 0)
            document.getElementById("usld_val_data").innerHTML = "+" + (stock.usld_data.data).toFixed(2) + " %";
        else
            document.getElementById("usld_val_data_neg").innerHTML = (stock.usld_data.data).toFixed(2) + " %";

        document.getElementById("baltic_val_current").innerHTML = (stock.baltic_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.baltic_data.data >= 0)
            document.getElementById("baltic_val_data").innerHTML = "+" + (stock.baltic_data.data).toFixed(2) + " %";
        else
            document.getElementById("baltic_val_data_neg").innerHTML = (stock.baltic_data.data).toFixed(2) + " %";    

        document.getElementById("truck_val_current").innerHTML = (stock.truck_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.truck_data.data >= 0)
            document.getElementById("truck_val_data").innerHTML = "+" + (stock.truck_data.data).toFixed(2) + " %";
        else
            document.getElementById("truck_val_data_neg").innerHTML = (stock.truck_data.data).toFixed(2) + " %";    

        document.getElementById("cf_val_current").innerHTML = (stock.cf_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.cf_data.data >= 0)
            document.getElementById("cf_val_data").innerHTML = "+" + (stock.cf_data.data).toFixed(2) + " %";
        else
            document.getElementById("cf_val_data_neg").innerHTML = (stock.cf_data.data).toFixed(2) + " %";
        
        document.getElementById("t_val_current").innerHTML = (stock.t_index.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.t_index.data >= 0)
            document.getElementById("t_val_data").innerHTML = "+" + (stock.t_index.data).toFixed(2) + " %";
        else
            document.getElementById("t_val_data_neg").innerHTML = (stock.t_index.data).toFixed(2) + " %";
            
        document.getElementById("ag_val_current").innerHTML = (stock.ag_data.current).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
        if (stock.ag_data.data >= 0)
            document.getElementById("ag_val_data").innerHTML = "+" + (stock.ag_data.data).toFixed(2) + " %";
        else
            document.getElementById("ag_val_data_neg").innerHTML = (stock.ag_data.data).toFixed(2) + " %";




        document.getElementById("rc_val_current").innerHTML = (stock.rc_index.current);
        if (stock.rc_index.data >= 0)
            document.getElementById("rc_val_data").innerHTML = "+" + (stock.rc_index.data).toFixed(2) + " %";
        else
            document.getElementById("rc_val_data_neg").innerHTML = (stock.rc_index.data).toFixed(2) + " %";

        document.getElementById("ardmore_val_current").innerHTML = (stock.Ardmore_data.current);
        if (stock.Ardmore_data.data >= 0)
            document.getElementById("ardmore_val_data").innerHTML = "+" + (stock.Ardmore_data.data).toFixed(2) + " %";
        else
            document.getElementById("ardmore_val_data_neg").innerHTML = (stock.Ardmore_data.data).toFixed(2) + " %";

        document.getElementById("arkoma_val_current").innerHTML = (stock.Arkoma_data.current);
        if (stock.Arkoma_data.data >= 0)
            document.getElementById("arkoma_val_data").innerHTML = "+" + (stock.Arkoma_data.data).toFixed(2) + " %";
        else
            document.getElementById("arkoma_val_data_neg").innerHTML = (stock.Arkoma_data.data).toFixed(2) + " %";    

        document.getElementById("barnett_val_current").innerHTML = (stock.Barnett_data.current);
        if (stock.Barnett_data.data >= 0)
            document.getElementById("barnett_val_data").innerHTML = "+" + (stock.Barnett_data.data).toFixed(2) + " %";
        else
            document.getElementById("barnett_val_data_neg").innerHTML = (stock.Barnett_data.data).toFixed(2) + " %";    

        document.getElementById("cana_val_current").innerHTML = (stock.Cana_data.current);
        if (stock.Cana_data.data >= 0)
            document.getElementById("cana_val_data").innerHTML = "+" + (stock.Cana_data.data).toFixed(2) + " %";
        else
            document.getElementById("cana_val_data_neg").innerHTML = (stock.Cana_data.data).toFixed(2) + " %";
    
        document.getElementById("niobrara_val_current").innerHTML = (stock.Niobrara_data.current);
        if (stock.Niobrara_data.data >= 0)
            document.getElementById("niobrara_val_data").innerHTML = "+" + (stock.Niobrara_data.data).toFixed(2) + " %";
        else
            document.getElementById("niobrara_val_data_neg").innerHTML = (stock.Niobrara_data.data).toFixed(2) + " %";    

        document.getElementById("ford_val_current").innerHTML = (stock.Ford_data.current);
        if (stock.Ford_data.data >= 0)
            document.getElementById("ford_val_data").innerHTML = "+" + (stock.Ford_data.data).toFixed(2) + " %";
        else
            document.getElementById("ford_val_data_neg").innerHTML = (stock.Ford_data.data).toFixed(2) + " %";    
        
        document.getElementById("granite_val_current").innerHTML = (stock.Granite_data.current);
        if (stock.Granite_data.data >= 0)
            document.getElementById("granite_val_data").innerHTML = "+" + (stock.Granite_data.data).toFixed(2) + " %";
        else
            document.getElementById("granite_val_data_neg").innerHTML = (stock.Granite_data.data).toFixed(2) + " %";    

        document.getElementById("haynesville_val_current").innerHTML = (stock.Haynesville_data.current);
        if (stock.Haynesville_data.data >= 0)
            document.getElementById("haynesville_val_data").innerHTML = "+" + (stock.Haynesville_data.data).toFixed(2) + " %";
        else
            document.getElementById("haynesville_val_data_neg").innerHTML = (stock.Haynesville_data.data).toFixed(2) + " %";    

        document.getElementById("marcellus_val_current").innerHTML = (stock.Marcellus_data.current);
        if (stock.Marcellus_data.data >= 0)
            document.getElementById("marcellus_val_data").innerHTML = "+" + (stock.Marcellus_data.data).toFixed(2) + " %";
        else
            document.getElementById("marcellus_val_data_neg").innerHTML = (stock.Marcellus_data.data).toFixed(2) + " %";    

        document.getElementById("mississippian_val_current").innerHTML = (stock.Mississippian_data.current);
        if (stock.Mississippian_data.data >= 0)
            document.getElementById("mississippian_val_data").innerHTML = "+" + (stock.Mississippian_data.data).toFixed(2) + " %";
        else
            document.getElementById("mississippian_val_data_neg").innerHTML = (stock.Mississippian_data.data).toFixed(2) + " %";    

        document.getElementById("permian_val_current").innerHTML = (stock.Permian_data.current);
        if (stock.Permian_data.data >= 0)
            document.getElementById("permian_val_data").innerHTML = "+" + (stock.Permian_data.data).toFixed(2) + " %";
        else
            document.getElementById("permian_val_data_neg").innerHTML = (stock.Permian_data.data).toFixed(2) + " %";    
            
        document.getElementById("utica_val_current").innerHTML = (stock.Utica_data.current);
        if (stock.Utica_data.data >= 0)
            document.getElementById("utica_val_data").innerHTML = "+" + (stock.Utica_data.data).toFixed(2) + " %";
        else
            document.getElementById("utica_val_data_neg").innerHTML = (stock.Utica_data.data).toFixed(2) + " %";    

        document.getElementById("williston_val_current").innerHTML = (stock.Williston_data.current);
        if (stock.Williston_data.data >= 0)
            document.getElementById("williston_val_data").innerHTML = "+" + (stock.Williston_data.data).toFixed(2) + " %";
        else
            document.getElementById("williston_val_data_neg").innerHTML = (stock.Williston_data.data).toFixed(2) + " %";
            
        document.getElementById("dpr_duc_val_current").innerHTML = (stock.DPR_DUC.current);
        if (stock.DPR_DUC.data >= 0)
            document.getElementById("dpr_duc_val_data").innerHTML = "+" + (stock.DPR_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("dpr_duc_val_data_neg").innerHTML = (stock.DPR_DUC.data).toFixed(2) + " %";

        document.getElementById("Anadarko_duc_val_current").innerHTML = (stock.Anadarko_DUC.current);
        if (stock.Anadarko_DUC.data >= 0)
            document.getElementById("Anadarko_duc_val_data").innerHTML = "+" + (stock.Anadarko_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Anadarko_duc_val_data_neg").innerHTML = (stock.Anadarko_DUC.data).toFixed(2) + " %";

        document.getElementById("Appalachia_duc_val_current").innerHTML = (stock.Appalachia_DUC.current);
        if (stock.Appalachia_DUC.data >= 0)
            document.getElementById("Appalachia_duc_val_data").innerHTML = "+" + (stock.Appalachia_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Appalachia_duc_val_data_neg").innerHTML = (stock.Appalachia_DUC.data).toFixed(2) + " %";

        document.getElementById("Bakken_duc_val_current").innerHTML = (stock.Bakken_DUC.current);
        if (stock.Bakken_DUC.data >= 0)
            document.getElementById("Bakken_duc_val_data").innerHTML = "+" + (stock.Bakken_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Bakken_duc_val_data_neg").innerHTML = (stock.Bakken_DUC.data).toFixed(2) + " %";

        document.getElementById("Eagle_duc_val_current").innerHTML = (stock.Eagle_DUC.current);
        if (stock.Eagle_DUC.data >= 0)
            document.getElementById("Eagle_duc_val_data").innerHTML = "+" + (stock.Eagle_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Eagle_duc_val_data_neg").innerHTML = (stock.Eagle_DUC.data).toFixed(2) + " %";

        document.getElementById("Haynesville_duc_val_current").innerHTML = (stock.Haynesville_DUC.current);
        if (stock.Haynesville_DUC.data >= 0)
            document.getElementById("Haynesville_duc_val_data").innerHTML = "+" + (stock.Haynesville_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Haynesville_duc_val_data_neg").innerHTML = (stock.Haynesville_DUC.data).toFixed(2) + " %";

        document.getElementById("Niobrara_duc_val_current").innerHTML = (stock.Niobrara_DUC.current);
        if (stock.Niobrara_DUC.data >= 0)
            document.getElementById("Niobrara_duc_val_data").innerHTML = "+" + (stock.Niobrara_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Niobrara_duc_val_data_neg").innerHTML = (stock.Niobrara_DUC.data).toFixed(2) + " %";

        document.getElementById("Permian_duc_val_current").innerHTML = (stock.Permian_DUC.current);
        if (stock.Permian_DUC.data >= 0)
            document.getElementById("Permian_duc_val_data").innerHTML = "+" + (stock.Permian_DUC.data).toFixed(2) + " %";
        else
            document.getElementById("Permian_duc_val_data_neg").innerHTML = (stock.Permian_DUC.data).toFixed(2) + " %";
    
    }
    catch(err){
        console.log(err);
        err_pop();
        // err_pop_1(err);
    }
            

});