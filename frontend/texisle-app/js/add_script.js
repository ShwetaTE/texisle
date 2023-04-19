$(document).ready(function(){
    function loadScript_chart(url) {
        document.body.appendChild(document.createElement("script")).src = url;
    }

    window.setTimeout(function(){
        // loadScript_chart("js/chart/raw_material_index1.js");
        // loadScript_chart("js/chart/pipe_manufacturing_index1.js");
        // loadScript_chart("js/chart/iron_ore_mining_index1.js");
        // loadScript_chart("js/chart/steel_manufacturing_index1.js");
        // loadScript_chart("js/chart/transport_index1.js");

        loadScript_chart("js/chart/raw_material_index.js");
        loadScript_chart("js/chart/pipe_manufacturing_index.js");
        loadScript_chart("js/chart/iron_ore_mining_index.js");
        loadScript_chart("js/chart/steel_manufacturing_index.js");
        loadScript_chart("js/chart/transport_index.js");
        loadScript_chart("js/chart/rig_count_index.js");
        loadScript_chart("js/chart/well_count_index.js");
        
        // <!-- loadScript_chart("js/chart/fuel_index.js"); -->

        // <!-- Raw material index -->
        loadScript_chart("js/chart/raw_material_index/chart_scrap.js");
        loadScript_chart("js/chart/raw_material_index/chart_hrc.js");
        loadScript_chart("js/chart/raw_material_index/chart_coal.js");
        loadScript_chart("js/chart/raw_material_index/chart_iron.js");

        // <!-- pipe Manufacturing -->
        loadScript_chart("js/chart/pipe_manufacturing/chart_tmst.js");
        loadScript_chart("js/chart/pipe_manufacturing/chart_ts.js");
        loadScript_chart("js/chart/pipe_manufacturing/chart_vkpa.js");
        loadScript_chart("js/chart/pipe_manufacturing/chart_x.js");
        loadScript_chart("js/chart/pipe_manufacturing/chart_nwpx.js");

        // <!-- steel Manufacturing -->
        loadScript_chart("js/chart/steel_manufacturing/chart_clf.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_cmc.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_ggb.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_mt.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_nue.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_pkx.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_rs.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_stld.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_tx.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_x.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_jfe.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_nippon.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_szgde.js");
        loadScript_chart("js/chart/steel_manufacturing/chart_tkade.js");

        // <!-- iron ore -->
        loadScript_chart("js/chart/iron_ore/chart_rio.js");
        loadScript_chart("js/chart/iron_ore/chart_sxc.js");
        loadScript_chart("js/chart/iron_ore/chart_vale.js");
        loadScript_chart("js/chart/iron_ore/chart_bhp.js");
        
        // <!-- fuel 
        // loadScript_chart("js/chart/fuel/chart_hof.js");
        // loadScript_chart("js/chart/fuel/chart_rbf.js"); -->

        // <!-- transportation  -->
        loadScript_chart("js/chart/transportation/chart_baltic.js");
        loadScript_chart("js/chart/transportation/chart_cf.js");
        loadScript_chart("js/chart/transportation/chart_truck.js");
        loadScript_chart("js/chart/transportation/chart_usld.js");
        loadScript_chart("js/chart/transportation/chart_allgrade.js");

        // rig_count
        loadScript_chart("js/chart/rig_count/chart_ardmore.js");
        loadScript_chart("js/chart/rig_count/chart_arkoma.js");
        loadScript_chart("js/chart/rig_count/chart_barnett.js");
        loadScript_chart("js/chart/rig_count/chart_cana.js");
        loadScript_chart("js/chart/rig_count/chart_niobrara.js");
        loadScript_chart("js/chart/rig_count/chart_ford.js");
        loadScript_chart("js/chart/rig_count/chart_granite.js");
        loadScript_chart("js/chart/rig_count/chart_haynesville.js");
        loadScript_chart("js/chart/rig_count/chart_marcellus.js");
        loadScript_chart("js/chart/rig_count/chart_mississippian.js");
        loadScript_chart("js/chart/rig_count/chart_permian.js");
        loadScript_chart("js/chart/rig_count/chart_utica.js");
        loadScript_chart("js/chart/rig_count/chart_williston.js");

        // well count
        loadScript_chart("js/chart/well_count/chart_Anadarko.js");
        loadScript_chart("js/chart/well_count/chart_Appalachia.js");
        loadScript_chart("js/chart/well_count/chart_Bakken.js");
        loadScript_chart("js/chart/well_count/chart_Eagle.js");
        loadScript_chart("js/chart/well_count/chart_Haynesville.js");
        loadScript_chart("js/chart/well_count/chart_Niobrara.js");
        loadScript_chart("js/chart/well_count/chart_Permian.js");

    }, 500);

});