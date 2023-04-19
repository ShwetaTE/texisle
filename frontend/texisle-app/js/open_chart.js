function openTab_about(evt, tabname) {
  let i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  // console.log(evt)
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabname).style.display = "block";
  // console.log(evt.currentTarget)
  evt.currentTarget.className += " active";
  // document.getElementById(default_tab).click();
}

function openTab(evt, tabname, chart_name, default_tab) {
  let i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  // console.log(tabcontent)
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  // console.log(tabname)
  // console.log(document.getElementById(tabname).style.display)
  document.getElementById(tabname).style.display = "block";
  // console.log(document.getElementById(tabname).style.display)
  evt.currentTarget.className += " active";
  load_js_file(chart_name);
  chart_count(chart_name);
  // console.log(default_tab)
  document.getElementById(default_tab).click();
}

function openinnerTab(evt, tabname) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("innertabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks1");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabname).style.display = "block";
  evt.currentTarget.className += " active";
}

function load_js_file(tab) {
  // console.log("here   ", tab)
  if (tab == "index_rmi") {
    loadScript("js/rmi_chart/chart3.js");
    update_time("raw_material_index", "#rmi_upt_");
    RecNewsGet("raw material index", "#rmi_rec_news_datatable");
    newsget_p("raw material index", "#rmi_news_datatable");
    loadScript("js/rmi_chart/chart2.js");
    loadScript("js/rmi_chart/chart1.js");
    loadScript("js/rmi_chart/chart4.js");
    loadScript("js/rmi_chart/chart5.js");
    loadScript("js/rmi_chart/chart6.js");
    tweet_html_index("raw material index", "#rmi_tweet_datatable");
  }
  if (tab == "index_pm") {
    loadScript("js/pm_chart/chart3.js");
    update_time("pipe_manufacturing", "#pm_upt_");
    RecNewsGet("pipe manufacturing", "#pm_rec_news_datatable");
    newsget_p("pipe manufacturing", "#pm_news_datatable");
    loadScript("js/pm_chart/chart2.js");
    loadScript("js/pm_chart/chart1.js");
    loadScript("js/pm_chart/chart4.js");
    loadScript("js/pm_chart/chart5.js");
    loadScript("js/pm_chart/chart6.js");
    tweet_html_index("pipe manufacturing", "#pm_tweet_datatable");
  }
  if (tab == "index_io") {
    loadScript("js/io_chart/chart3.js");
    update_time("iron_ore", "#io_upt_");
    RecNewsGet("iron ore mining", "#io_rec_news_datatable");
    newsget_p("iron ore mining", "#io_news_datatable");
    loadScript("js/io_chart/chart2.js");
    loadScript("js/io_chart/chart1.js");
    loadScript("js/io_chart/chart4.js");
    loadScript("js/io_chart/chart5.js");
    loadScript("js/io_chart/chart6.js");
    tweet_html_index("iron ore mining", "#io_tweet_datatable");
  }
  if (tab == "index_smf") {
    loadScript("js/smf_chart/chart3.js");
    update_time("steel_manufacturing", "#smf_upt_");
    RecNewsGet("steel manufacturing", "#smf_rec_news_datatable");
    newsget_p("steel manufacturing", "#smf_news_datatable");
    loadScript("js/smf_chart/chart2.js");
    loadScript("js/smf_chart/chart1.js");
    loadScript("js/smf_chart/chart4.js");
    loadScript("js/smf_chart/chart5.js");
    loadScript("js/smf_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#smf_tweet_datatable");
  }
  if (tab == "index_f") {
    loadScript("js/f_chart/chart3.js");
    update_time("fuel", "#f_upt_");
    RecNewsGet("fuel", "#f_rec_news_datatable");
    newsget_p("fuel", "#f_news_datatable");
    loadScript("js/f_chart/chart2.js");
    loadScript("js/f_chart/chart1.js");
    loadScript("js/f_chart/chart4.js");
    loadScript("js/f_chart/chart5.js");
    loadScript("js/f_chart/chart6.js");
    tweet_html_index("fuel", "#f_tweet_datatable");
  }
  if (tab == "index_t") {
    loadScript("js/t_chart/chart3.js");
    update_time("transportation", "#t_upt_");
    RecNewsGet("transportation", "#t_rec_news_datatable");
    newsget_p("fuel", "#t_news_datatable");
    loadScript("js/t_chart/chart2.js");
    loadScript("js/t_chart/chart1.js");
    loadScript("js/t_chart/chart4.js");
    loadScript("js/t_chart/chart5.js");
    loadScript("js/t_chart/chart6.js");
    tweet_html_index("fuel", "#t_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "index_rc") {
    loadScript("js/rig_chart/chart3.js");
    update_time("rig_count", "#rc_upt_");
    RecNewsGet("RC_index", "#rc_rec_news_datatable");
    newsget_p("fuel", "#rc_news_datatable");
    loadScript("js/rig_chart/chart2.js");
    loadScript("js/rig_chart/chart1.js");
    loadScript("js/rig_chart/chart4.js");
    loadScript("js/rig_chart/chart5.js");
    loadScript("js/rig_chart/chart6.js");
    tweet_html_index("fuel", "#t_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "index_dpr") {
    loadScript("js/well_count/dpr_chart/chart3.js");
    update_time("well_count", "#dpr_upt_");
    RecNewsGet("DPR_DUC", "#dpr_rec_news_datatable");
    newsget_p("fuel", "#dpr_news_datatable");
    loadScript("js/well_count/dpr_chart/chart2.js");
    loadScript("js/well_count/dpr_chart/chart1.js");
    loadScript("js/well_count/dpr_chart/chart4.js");
    loadScript("js/well_count/dpr_chart/chart5.js");
    loadScript("js/well_count/dpr_chart/chart6.js");
    tweet_html_index("fuel", "#t_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }

  // RMI
  if (tab == "scrap") {
    loadScript("js/scrap/chart_3.js");
    update_time("scrap", "#scrap_upt_");
    RecNewsGet("Scrap", "#scrap_rec_news_datatable");
    newsget("Scrap", "#scrap_news_datatable");
    loadScript("js/scrap/chart_1.js");
    loadScript("js/scrap/chart_2.js");
    loadScript("js/scrap/chart_5.js");
    loadScript("js/scrap/chart_6.js");
    loadScript("js/scrap/chart_4.js");
    tweet_html_ticker("Scrap", "#scrap_tweet_datatable");
  }
  if (tab == "hrc") {
    loadScript("js/hrc/chart_3.js");
    update_time("hrc", "#hrc_upt_");
    RecNewsGet("HRC", "#hrc_rec_news_datatable");
    newsget("HRC", "#hrc_news_datatable");
    loadScript("js/hrc/chart_4.js");
    loadScript("js/hrc/chart_2.js");
    loadScript("js/hrc/chart_5.js");
    loadScript("js/hrc/chart_6.js");
    loadScript("js/hrc/chart_1.js");
    tweet_html_ticker("HRC", "#hrc_tweet_datatable");
  }
  if (tab == "iron") {
    loadScript("js/iron_chart/chart_3.js");
    update_time("iron", "#iron_upt_");
    RecNewsGet("iron", "#iron_rec_news_datatable");
    newsget("iron", "#iron_news_datatable");
    loadScript("js/iron_chart/chart_2.js");
    loadScript("js/iron_chart/chart_1.js");
    loadScript("js/iron_chart/chart_4.js");
    loadScript("js/iron_chart/chart_5.js");
    loadScript("js/iron_chart/chart_6.js");
    tweet_html_ticker("iron", "#iron_tweet_datatable");
  }
  if (tab == "coal") {
    loadScript("js/coal_chart/chart3.js");
    update_time("MFFH22.NYM", "#coal_upt_");
    RecNewsGet("coal", "#coal_rec_news_datatable");
    newsget("coal", "#coal_news_datatable");
    loadScript("js/coal_chart/chart2.js");
    loadScript("js/coal_chart/chart1.js");
    loadScript("js/coal_chart/chart4.js");
    loadScript("js/coal_chart/chart5.js");
    loadScript("js/coal_chart/chart6.js");
    tweet_html_ticker("coal", "#coal_tweet_datatable");
  }

  // Pipe Manufacturing
  if (tab == "ts") {
    loadScript("js/ts_chart/chart3.js");
    update_time("TS", "#ts_upt_");
    RecNewsGet("TS", "#ts_rec_news_datatable");
    newsget("TS", "#ts_news_datatable");
    loadScript("js/ts_chart/chart2.js");
    loadScript("js/ts_chart/chart1_ts.js");
    loadScript("js/ts_chart/chart4.js");
    loadScript("js/ts_chart/chart5.js");
    loadScript("js/ts_chart/chart6.js");
    tweet_html_ticker("TS", "#ts_tweet_datatable");
  }
  if (tab == "vkpa") {
    loadScript("js/vkpa_chart/chart3.js");
    update_time("VK.PA", "#vkpa_upt_");
    RecNewsGet("VK.PA", "#vkpa_rec_news_datatable");
    newsget("vkpa", "#vkpa_news_datatable");
    loadScript("js/vkpa_chart/chart2.js");
    loadScript("js/vkpa_chart/chart1_vkpa.js");
    loadScript("js/vkpa_chart/chart4.js");
    loadScript("js/vkpa_chart/chart5.js");
    loadScript("js/vkpa_chart/chart6.js");
    tweet_html_ticker("vkpa", "#vkpa_tweet_datatable");
  }
  if (tab == "x") {
    loadScript("js/x_chart/chart3.js");
    update_time("X", "#x_upt_");
    RecNewsGet("X", "#x_rec_news_datatable");
    newsget("X", "#x_news_datatable");
    loadScript("js/x_chart/chart2.js");
    loadScript("js/x_chart/chart1_x.js");
    loadScript("js/x_chart/chart4.js");
    loadScript("js/x_chart/chart5.js");
    loadScript("js/x_chart/chart6.js");
    tweet_html_ticker("X", "#x_tweet_datatable");
  }
  if (tab == "tmst") {
    loadScript("js/tmst_chart/chart3.js");
    update_time("TMST", "#tmst_upt_");
    RecNewsGet("TMST", "#tmst_rec_news_datatable");
    newsget("TMST", "#tmst_news_datatable");
    loadScript("js/tmst_chart/chart2.js");
    loadScript("js/tmst_chart/chart1_tmst.js");
    loadScript("js/tmst_chart/chart4.js");
    loadScript("js/tmst_chart/chart5.js");
    loadScript("js/tmst_chart/chart6.js");
    tweet_html_ticker("TMST", "#tmst_tweet_datatable");
  }
  if (tab == "nwpx") {
    loadScript("js/nwpx_chart/chart3.js");
    update_time("NWPX", "#nwpx_upt_");
    RecNewsGet("NWPX", "#nwpx_rec_news_datatable");
    newsget("nwpx", "#nwpx_news_datatable");
    loadScript("js/nwpx_chart/chart2.js");
    loadScript("js/nwpx_chart/chart1_nwpx.js");
    loadScript("js/nwpx_chart/chart4.js");
    loadScript("js/nwpx_chart/chart5.js");
    loadScript("js/nwpx_chart/chart6.js");
    tweet_html_ticker("nwpx", "#nwpx_tweet_datatable");
  }

  // Steel Manufacturing
  if (tab == "mt") {
    loadScript("js/mt_chart/chart3.js");
    update_time("MT", "#mt_upt_");
    RecNewsGet("MT", "#mt_rec_news_datatable");
    newsget("MT", "#mt_news_datatable");
    loadScript("js/mt_chart/chart2.js");
    loadScript("js/mt_chart/chart1_mt.js");
    loadScript("js/mt_chart/chart4.js");
    loadScript("js/mt_chart/chart5.js");
    loadScript("js/mt_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#mt_tweet_datatable");
  }
  if (tab == "pkx") {
    loadScript("js/pkx_chart/chart3.js");
    update_time("PKX", "#pkx_upt_");
    RecNewsGet("PKX", "#pkx_rec_news_datatable");
    newsget("PKX", "#pkx_news_datatable");
    loadScript("js/pkx_chart/chart2.js");
    loadScript("js/pkx_chart/chart1_pkx.js");
    loadScript("js/pkx_chart/chart4.js");
    loadScript("js/pkx_chart/chart5.js");
    loadScript("js/pkx_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#pkx_tweet_datatable");
  }
  if (tab == "nue") {
    loadScript("js/nue_chart/chart3.js");
    update_time("NUE", "#nue_upt_");
    RecNewsGet("NUE", "#nue_rec_news_datatable");
    newsget("NUE", "#nue_news_datatable");
    loadScript("js/nue_chart/chart2.js");
    loadScript("js/nue_chart/chart1_nue.js");
    loadScript("js/nue_chart/chart4.js");
    loadScript("js/nue_chart/chart5.js");
    loadScript("js/nue_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#nue_tweet_datatable");
  }
  if (tab == "stld") {
    loadScript("js/stld_chart/chart3.js");
    update_time("STLD", "#stld_upt_");
    RecNewsGet("STLD", "#stld_rec_news_datatable");
    newsget("STLD", "#stld_news_datatable");
    loadScript("js/stld_chart/chart2.js");
    loadScript("js/stld_chart/chart1_stld.js");
    loadScript("js/stld_chart/chart4.js");
    loadScript("js/stld_chart/chart5.js");
    loadScript("js/stld_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#stld_tweet_datatable");
  }
  if (tab == "rs") {
    loadScript("js/rs_chart/chart3.js");
    update_time("RS", "#rs_upt_");
    RecNewsGet("RS", "#rs_rec_news_datatable");
    newsget("RS", "#rs_news_datatable");
    loadScript("js/rs_chart/chart2.js");
    loadScript("js/rs_chart/chart1_chart.js");
    loadScript("js/rs_chart/chart4.js");
    loadScript("js/rs_chart/chart5.js");
    loadScript("js/rs_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#rs_tweet_datatable");
  }
  if (tab == "tx") {
    loadScript("js/tx_chart/chart3.js");
    update_time("TX", "#tx_upt_");
    RecNewsGet("TX", "#tx_rec_news_datatable");
    newsget("TX", "#tx_news_datatable");
    loadScript("js/tx_chart/chart2.js");
    loadScript("js/tx_chart/chart1_tx.js");
    loadScript("js/tx_chart/chart4.js");
    loadScript("js/tx_chart/chart5.js");
    loadScript("js/tx_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#tx_tweet_datatable");
  }
  if (tab == "clf") {
    loadScript("js/clf_chart/chart3.js");
    update_time("CLF", "#clf_upt_");
    RecNewsGet("CLF", "#clf_rec_news_datatable");
    newsget("CLF", "#clf_news_datatable");
    loadScript("js/clf_chart/chart2.js");
    loadScript("js/clf_chart/chart1_clf.js");
    loadScript("js/clf_chart/chart4.js");
    loadScript("js/clf_chart/chart5.js");
    loadScript("js/clf_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#clf_tweet_datatable");
  }
  if (tab == "ggb") {
    loadScript("js/ggb_chart/chart3.js");
    update_time("GGB", "#ggb_upt_");
    RecNewsGet("GGB", "#ggb_rec_news_datatable");
    newsget("GGB", "#ggb_news_datatable");
    loadScript("js/ggb_chart/chart2.js");
    loadScript("js/ggb_chart/chart1_ggb.js");
    loadScript("js/ggb_chart/chart4.js");
    loadScript("js/ggb_chart/chart5.js");
    loadScript("js/ggb_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#ggb_tweet_datatable");
  }
  if (tab == "cmc") {
    loadScript("js/cmc_chart/chart3.js");
    update_time("CMC", "#cmc_upt_");
    RecNewsGet("CMC", "#cmc_rec_news_datatable");
    newsget("CMC", "#cmc_news_datatable");
    loadScript("js/cmc_chart/chart2.js");
    loadScript("js/cmc_chart/chart1_cmc.js");
    loadScript("js/cmc_chart/chart4.js");
    loadScript("js/cmc_chart/chart5.js");
    loadScript("js/cmc_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#cmc_tweet_datatable");
  }
  if (tab == "tkade") {
    loadScript("js/tkade_chart/chart3.js");
    update_time("TKA.DE", "#tkade_upt_");
    RecNewsGet("TKA.DE", "#tkade_rec_news_datatable");
    newsget("tkade", "#tkade_news_datatable");
    loadScript("js/tkade_chart/chart2.js");
    loadScript("js/tkade_chart/chart1_tkade.js");
    loadScript("js/tkade_chart/chart4.js");
    loadScript("js/tkade_chart/chart5.js");
    loadScript("js/tkade_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#tkade_tweet_datatable");
  }
  if (tab == "szgde") {
    loadScript("js/szgde_chart/chart3.js");
    update_time("SZG.DE", "#szgde_upt_");
    RecNewsGet("SZG.DE", "#szgde_rec_news_datatable");
    newsget("szgde", "#szgde_news_datatable");
    loadScript("js/szgde_chart/chart2.js");
    loadScript("js/szgde_chart/chart1_szgde.js");
    loadScript("js/szgde_chart/chart4.js");
    loadScript("js/szgde_chart/chart5.js");
    loadScript("js/szgde_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#szgde_tweet_datatable");
  }
  if (tab == "nippon") {
    loadScript("js/nippon_chart/chart3.js");
    update_time("5401.T", "#nippon_upt_");
    RecNewsGet("Nippon", "#nippon_rec_news_datatable");
    newsget("nippon", "#nippon_news_datatable");
    loadScript("js/nippon_chart/chart2.js");
    loadScript("js/nippon_chart/chart1_np.js");
    loadScript("js/nippon_chart/chart4.js");
    loadScript("js/nippon_chart/chart5.js");
    loadScript("js/nippon_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#nippon_tweet_datatable");
  }
  if (tab == "jfe") {
    loadScript("js/jfe_chart/chart3.js");
    update_time("5411.T", "#jfe_upt_");
    RecNewsGet("JFE", "#jfe_rec_news_datatable");
    newsget("jfe", "#jfe_news_datatable");
    loadScript("js/jfe_chart/chart2.js");
    loadScript("js/jfe_chart/chart1_jfe.js");
    loadScript("js/jfe_chart/chart4.js");
    loadScript("js/jfe_chart/chart5.js");
    loadScript("js/jfe_chart/chart6.js");
    tweet_html_index("steel manufacturing", "#jfe_tweet_datatable");
  }

  // Mining Companies
  if (tab == "rio") {
    loadScript("js/rio_chart/chart3.js");
    update_time("RIO", "#rio_upt_");
    RecNewsGet("RIO", "#rio_rec_news_datatable");
    newsget("RIO", "#rio_news_datatable");
    loadScript("js/rio_chart/chart2.js");
    loadScript("js/rio_chart/chart1_rio.js");
    loadScript("js/rio_chart/chart4.js");
    loadScript("js/rio_chart/chart5.js");
    loadScript("js/rio_chart/chart6.js");
    tweet_html_index("iron ore mining", "#rio_tweet_datatable");
  }
  if (tab == "vale") {
    loadScript("js/vale_chart/chart3.js");
    update_time("VALE", "#vale_upt_");
    RecNewsGet("VALE", "#vale_rec_news_datatable");
    newsget("VALE", "#vale_news_datatable");
    loadScript("js/vale_chart/chart2.js");
    loadScript("js/vale_chart/chart1_vale.js");
    loadScript("js/vale_chart/chart4.js");
    loadScript("js/vale_chart/chart5.js");
    loadScript("js/vale_chart/chart6.js");
    tweet_html_index("iron ore mining", "#vale_tweet_datatable");
  }
  if (tab == "sxc") {
    loadScript("js/sxc_chart/chart3.js");
    update_time("SXC", "#sxc_upt_");
    RecNewsGet("SXC", "#sxc_rec_news_datatable");
    newsget("SXC", "#sxc_news_datatable");
    loadScript("js/sxc_chart/chart2.js");
    loadScript("js/sxc_chart/chart1_sxc.js");
    loadScript("js/sxc_chart/chart4.js");
    loadScript("js/sxc_chart/chart5.js");
    loadScript("js/sxc_chart/chart6.js");
    tweet_html_index("iron ore mining", "#sxc_tweet_datatable");
  }
  if (tab == "bhp") {
    loadScript("js/bhp_chart/chart3.js");
    update_time("BHP", "#bhp_upt_");
    RecNewsGet("BHP", "#bhp_rec_news_datatable");
    newsget("bhp", "#bhp_news_datatable");
    loadScript("js/bhp_chart/chart2.js");
    loadScript("js/bhp_chart/chart1_bhp.js");
    loadScript("js/bhp_chart/chart4.js");
    loadScript("js/bhp_chart/chart5.js");
    loadScript("js/bhp_chart/chart6.js");
    tweet_html_index("iron ore mining", "#bhp_tweet_datatable");
  }

  // Fuel
  if (tab == "hof") {
    loadScript("js/hof_chart/chart3.js");
    update_time("HO=F", "#hof_upt_");
    newsget("HO=F", "#hof_news_datatable");
    loadScript("js/hof_chart/chart2.js");
    loadScript("js/hof_chart/chart1.js");
    loadScript("js/hof_chart/chart4.js");
    loadScript("js/hof_chart/chart5.js");
    loadScript("js/hof_chart/chart6.js");
    tweet_html_ticker("HO=F", "#hof_tweet_datatable");
  }
  if (tab == "rbf") {
    loadScript("js/rbf_chart/chart3.js");
    update_time("RB=F", "#rbf_upt_");
    newsget("RB=F", "#rbf_news_datatable");
    loadScript("js/rbf_chart/chart2.js");
    loadScript("js/rbf_chart/chart1.js");
    loadScript("js/rbf_chart/chart4.js");
    loadScript("js/rbf_chart/chart5.js");
    loadScript("js/rbf_chart/chart6.js");
    tweet_html_ticker("RB=F", "#rbf_tweet_datatable");
  }

  // Transportation
  if (tab == "baltic") {
    loadScript("js/baltic_chart/chart_3.js");
    update_time("baltic", "#baltic_upt_");
    RecNewsGet("BADI", "#baltic_rec_news_datatable");
    newsget_p("fuel", "#baltic_news_datatable");
    loadScript("js/baltic_chart/chart_2.js");
    loadScript("js/baltic_chart/chart_1.js");
    loadScript("js/baltic_chart/chart_4.js");
    loadScript("js/baltic_chart/chart_5.js");
    loadScript("js/baltic_chart/chart_6.js");
    tweet_html_index("fuel", "#baltic_tweet_datatable");
  }
  if (tab == "usld") {
    loadScript("js/usld_chart/chart_3.js");
    update_time("ulsd", "#usld_upt_");
    RecNewsGet("ULSD", "#usld_rec_news_datatable");
    newsget_p("fuel", "#usld_news_datatable");
    loadScript("js/usld_chart/chart_2.js");
    loadScript("js/usld_chart/chart_1.js");
    loadScript("js/usld_chart/chart_4.js");
    loadScript("js/usld_chart/chart_5.js");
    loadScript("js/usld_chart/chart_6.js");
    tweet_html_index("fuel", "#usld_tweet_datatable");
  }
  if (tab == "truck") {
    loadScript("js/truck_chart/chart_3.js");
    update_time("truck", "#truck_upt_");
    RecNewsGet("Truck", "#truck_rec_news_datatable");
    newsget_p("fuel", "#truck_news_datatable");
    loadScript("js/truck_chart/chart_2.js");
    loadScript("js/truck_chart/chart_1.js");
    loadScript("js/truck_chart/chart_4.js");
    loadScript("js/truck_chart/chart_5.js");
    loadScript("js/truck_chart/chart_6.js");
    tweet_html_index("fuel", "#truck_tweet_datatable");
  }
  if (tab == "CassFreight") {
    loadScript("js/CassFreight_chart/chart_3.js");
    update_time("CassFreight", "#CassFreight_upt_");
    RecNewsGet("CassFreight", "#CassFreight_rec_news_datatable");
    newsget_p("fuel", "#CassFreight_news_datatable");
    loadScript("js/CassFreight_chart/chart_2.js");
    loadScript("js/CassFreight_chart/chart_1.js");
    loadScript("js/CassFreight_chart/chart_4.js");
    loadScript("js/CassFreight_chart/chart_5.js");
    loadScript("js/CassFreight_chart/chart_6.js");
    tweet_html_index("fuel", "#CassFreight_tweet_datatable");
  }
  if (tab == "AllGrade") {
    loadScript("js/AllGrade_chart/chart_3.js");
    update_time("All-Grade", "#AllGrade_upt_");
    RecNewsGet("AllGrade", "#AllGrade_rec_news_datatable");
    newsget_p("fuel", "#AllGrade_news_datatable");
    loadScript("js/AllGrade_chart/chart_2.js");
    loadScript("js/AllGrade_chart/chart_1.js");
    loadScript("js/AllGrade_chart/chart_4.js");
    loadScript("js/AllGrade_chart/chart_5.js");
    loadScript("js/AllGrade_chart/chart_6.js");
    tweet_html_index("fuel", "#AllGrade_tweet_datatable");
  }

  // Rig Count
  if (tab == "ardmore") {
    loadScript("js/ardmore_chart/chart3.js");
    update_time("rig_count", "#ardmore_upt_");
    RecNewsGet("Ardmore", "#ardmore_rec_news_datatable");
    newsget_p("fuel", "#ardmore_news_datatable");
    loadScript("js/ardmore_chart/chart2.js");
    loadScript("js/ardmore_chart/chart1.js");
    loadScript("js/ardmore_chart/chart4.js");
    loadScript("js/ardmore_chart/chart5.js");
    loadScript("js/ardmore_chart/chart6.js");
    tweet_html_index("fuel", "#ardmore_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "arkoma") {
    loadScript("js/arkoma_chart/chart3.js");
    update_time("rig_count", "#arkoma_upt_");
    RecNewsGet("Arkoma", "#arkoma_rec_news_datatable");
    newsget_p("fuel", "#arkoma_news_datatable");
    loadScript("js/arkoma_chart/chart2.js");
    loadScript("js/arkoma_chart/chart1.js");
    loadScript("js/arkoma_chart/chart4.js");
    loadScript("js/arkoma_chart/chart5.js");
    loadScript("js/arkoma_chart/chart6.js");
    tweet_html_index("fuel", "#arkoma_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "barnett") {
    loadScript("js/barnett_chart/chart3.js");
    update_time("rig_count", "#barnett_upt_");
    RecNewsGet("Barnett", "#barnett_rec_news_datatable");
    newsget_p("fuel", "#barnett_news_datatable");
    loadScript("js/barnett_chart/chart2.js");
    loadScript("js/barnett_chart/chart1.js");
    loadScript("js/barnett_chart/chart4.js");
    loadScript("js/barnett_chart/chart5.js");
    loadScript("js/barnett_chart/chart6.js");
    tweet_html_index("fuel", "#barnett_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "cana") {
    loadScript("js/cana_chart/chart3.js");
    update_time("rig_count", "#cana_upt_");
    RecNewsGet("Cana", "#cana_rec_news_datatable");
    newsget_p("fuel", "#cana_news_datatable");
    loadScript("js/cana_chart/chart2.js");
    loadScript("js/cana_chart/chart1.js");
    loadScript("js/cana_chart/chart4.js");
    loadScript("js/cana_chart/chart5.js");
    loadScript("js/cana_chart/chart6.js");
    tweet_html_index("fuel", "#cana_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "niobrara") {
    loadScript("js/niobrara_chart/chart3.js");
    update_time("rig_count", "#niobrara_upt_");
    RecNewsGet("Niobrara", "#niobrara_rec_news_datatable");
    newsget_p("fuel", "#niobrara_news_datatable");
    loadScript("js/niobrara_chart/chart2.js");
    loadScript("js/niobrara_chart/chart1.js");
    loadScript("js/niobrara_chart/chart4.js");
    loadScript("js/niobrara_chart/chart5.js");
    loadScript("js/niobrara_chart/chart6.js");
    tweet_html_index("fuel", "#niobrara_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "ford") {
    loadScript("js/ford_chart/chart3.js");
    update_time("rig_count", "#ford_upt_");
    RecNewsGet("F ord", "#ford_rec_news_datatable");
    newsget_p("fuel", "#ford_news_datatable");
    loadScript("js/ford_chart/chart2.js");
    loadScript("js/ford_chart/chart1.js");
    loadScript("js/ford_chart/chart4.js");
    loadScript("js/ford_chart/chart5.js");
    loadScript("js/ford_chart/chart6.js");
    tweet_html_index("fuel", "#ford_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "granite") {
    loadScript("js/granite_chart/chart3.js");
    update_time("rig_count", "#granite_upt_");
    RecNewsGet("Granite", "#granite_rec_news_datatable");
    newsget_p("fuel", "#granite_news_datatable");
    loadScript("js/granite_chart/chart2.js");
    loadScript("js/granite_chart/chart1.js");
    loadScript("js/granite_chart/chart4.js");
    loadScript("js/granite_chart/chart5.js");
    loadScript("js/granite_chart/chart6.js");
    tweet_html_index("fuel", "#granite_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "haynesville") {
    loadScript("js/haynesville_chart/chart3.js");
    update_time("rig_count", "#haynesville_upt_");
    RecNewsGet("Haynesville", "#haynesville_rec_news_datatable");
    newsget_p("fuel", "#haynesville_news_datatable");
    loadScript("js/haynesville_chart/chart2.js");
    loadScript("js/haynesville_chart/chart1.js");
    loadScript("js/haynesville_chart/chart4.js");
    loadScript("js/haynesville_chart/chart5.js");
    loadScript("js/haynesville_chart/chart6.js");
    tweet_html_index("fuel", "#haynesville_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "marcellus") {
    loadScript("js/marcellus_chart/chart3.js");
    update_time("rig_count", "#marcellus_upt_");
    RecNewsGet("Marcellus", "#marcellus_rec_news_datatable");
    newsget_p("fuel", "#marcellus_news_datatable");
    loadScript("js/marcellus_chart/chart2.js");
    loadScript("js/marcellus_chart/chart1.js");
    loadScript("js/marcellus_chart/chart4.js");
    loadScript("js/marcellus_chart/chart5.js");
    loadScript("js/marcellus_chart/chart6.js");
    tweet_html_index("fuel", "#marcellus_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "mississippian") {
    loadScript("js/mississippian_chart/chart3.js");
    update_time("rig_count", "#mississippian_upt_");
    RecNewsGet("Mississippian", "#mississippian_rec_news_datatable");
    newsget_p("fuel", "#mississippian_news_datatable");
    loadScript("js/mississippian_chart/chart2.js");
    loadScript("js/mississippian_chart/chart1.js");
    loadScript("js/mississippian_chart/chart4.js");
    loadScript("js/mississippian_chart/chart5.js");
    loadScript("js/mississippian_chart/chart6.js");
    tweet_html_index("fuel", "#mississippian_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "permian") {
    loadScript("js/permian_chart/chart3.js");
    update_time("rig_count", "#permian_upt_");
    RecNewsGet("Permian", "#permian_rec_news_datatable");
    newsget_p("fuel", "#permian_news_datatable");
    loadScript("js/permian_chart/chart2.js");
    loadScript("js/permian_chart/chart1.js");
    loadScript("js/permian_chart/chart4.js");
    loadScript("js/permian_chart/chart5.js");
    loadScript("js/permian_chart/chart6.js");
    tweet_html_index("fuel", "#permian_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "utica") {
    loadScript("js/utica_chart/chart3.js");
    update_time("rig_count", "#utica_upt_");
    RecNewsGet("Utica", "#utica_rec_news_datatable");
    newsget_p("fuel", "#utica_news_datatable");
    loadScript("js/utica_chart/chart2.js");
    loadScript("js/utica_chart/chart1.js");
    loadScript("js/utica_chart/chart4.js");
    loadScript("js/utica_chart/chart5.js");
    loadScript("js/utica_chart/chart6.js");
    tweet_html_index("fuel", "#utica_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "williston") {
    loadScript("js/williston_chart/chart3.js");
    update_time("rig_count", "#williston_upt_");
    RecNewsGet("Williston", "#williston_rec_news_datatable");
    newsget_p("fuel", "#williston_news_datatable");
    loadScript("js/williston_chart/chart2.js");
    loadScript("js/williston_chart/chart1.js");
    loadScript("js/williston_chart/chart4.js");
    loadScript("js/williston_chart/chart5.js");
    loadScript("js/williston_chart/chart6.js");
    tweet_html_index("fuel", "#williston_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }

  // Well Count
  if (tab == "Anadarko_DUC") {
    loadScript("js/well_count/Anadarko_chart/chart3.js");
    update_time("well_count", "#Anadarko_upt_");
    RecNewsGet("Anadarko_DUC", "#Anadarko_rec_news_datatable");
    newsget_p("fuel", "#Anadarko_news_datatable");
    loadScript("js/well_count/Anadarko_chart/chart2.js");
    loadScript("js/well_count/Anadarko_chart/chart1.js");
    loadScript("js/well_count/Anadarko_chart/chart4.js");
    loadScript("js/well_count/Anadarko_chart/chart5.js");
    loadScript("js/well_count/Anadarko_chart/chart6.js");
    tweet_html_index("fuel", "#Anadarko_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "Appalachia_DUC") {
    loadScript("js/well_count/Appalachia_chart/chart3.js");
    update_time("well_count", "#Appalachia_upt_");
    RecNewsGet("Appalachia_DUC", "#Appalachia_rec_news_datatable");
    newsget_p("fuel", "#Appalachia_news_datatable");
    loadScript("js/well_count/Appalachia_chart/chart2.js");
    loadScript("js/well_count/Appalachia_chart/chart1.js");
    loadScript("js/well_count/Appalachia_chart/chart4.js");
    loadScript("js/well_count/Appalachia_chart/chart5.js");
    loadScript("js/well_count/Appalachia_chart/chart6.js");
    tweet_html_index("fuel", "#Appalachia_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "Bakken_DUC") {
    loadScript("js/well_count/Bakken_chart/chart3.js");
    update_time("well_count", "#Bakken_upt_");
    RecNewsGet("Bakken_DUC", "#Bakken_rec_news_datatable");
    newsget_p("fuel", "#Bakken_news_datatable");
    loadScript("js/well_count/Bakken_chart/chart2.js");
    loadScript("js/well_count/Bakken_chart/chart1.js");
    loadScript("js/well_count/Bakken_chart/chart4.js");
    loadScript("js/well_count/Bakken_chart/chart5.js");
    loadScript("js/well_count/Bakken_chart/chart6.js");
    tweet_html_index("fuel", "#Bakken_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "Eagle_DUC") {
    loadScript("js/well_count/Eagle_chart/chart3.js");
    update_time("well_count", "#Eagle_upt_");
    RecNewsGet("Eagle_DUC", "#Eagle_rec_news_datatable");
    newsget_p("fuel", "#Eagle_news_datatable");
    loadScript("js/well_count/Eagle_chart/chart2.js");
    loadScript("js/well_count/Eagle_chart/chart1.js");
    loadScript("js/well_count/Eagle_chart/chart4.js");
    loadScript("js/well_count/Eagle_chart/chart5.js");
    loadScript("js/well_count/Eagle_chart/chart6.js");
    tweet_html_index("fuel", "#Eagle_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "Haynesville_DUC") {
    loadScript("js/well_count/Haynesville_chart/chart3.js");
    update_time("well_count", "#Haynesville_upt_");
    RecNewsGet("Haynesville_DUC", "#Haynesville_rec_news_datatable");
    newsget_p("fuel", "#Haynesville_news_datatable");
    loadScript("js/well_count/Haynesville_chart/chart2.js");
    loadScript("js/well_count/Haynesville_chart/chart1.js");
    loadScript("js/well_count/Haynesville_chart/chart4.js");
    loadScript("js/well_count/Haynesville_chart/chart5.js");
    loadScript("js/well_count/Haynesville_chart/chart6.js");
    tweet_html_index("fuel", "#Haynesville_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "Niobrara_DUC") {
    loadScript("js/well_count/Niobrara_chart/chart3.js");
    update_time("well_count", "#Niobrara_upt_");
    RecNewsGet("Niobrara_DUC", "#Niobrara_rec_news_datatable");
    newsget_p("fuel", "#Niobrara_news_datatable");
    loadScript("js/well_count/Niobrara_chart/chart2.js");
    loadScript("js/well_count/Niobrara_chart/chart1.js");
    loadScript("js/well_count/Niobrara_chart/chart4.js");
    loadScript("js/well_count/Niobrara_chart/chart5.js");
    loadScript("js/well_count/Niobrara_chart/chart6.js");
    tweet_html_index("fuel", "#Niobrara_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
  if (tab == "Permian_DUC") {
    loadScript("js/well_count/Permian_chart/chart3.js");
    update_time("well_count", "#Permian_upt_");
    RecNewsGet("Permian_DUC", "#Permian_rec_news_datatable");
    newsget_p("fuel", "#Permian_news_datatable");
    loadScript("js/well_count/Permian_chart/chart2.js");
    loadScript("js/well_count/Permian_chart/chart1.js");
    loadScript("js/well_count/Permian_chart/chart4.js");
    loadScript("js/well_count/Permian_chart/chart5.js");
    loadScript("js/well_count/Permian_chart/chart6.js");
    tweet_html_index("fuel", "#Permian_tweet_datatable");
    // tweet_html_index('transportation', '#t_tweet_datatable')
  }
}

function loadScript(url) {
  document.body.appendChild(document.createElement("script")).src = url;
}

function chart_count(chart) {
  var deviceID = sessionStorage.getItem("deviceID");
  if (deviceID == null) {
    deviceID = device.uuid;
    sessionStorage.setItem("deviceID", deviceID);
  }
  var form = new FormData();
  form.append("chart", chart);
  form.append("app", app_type);
  form.append("deviceID", deviceID);
  form.append("session_id", sessionStorage.getItem("SessionName"));

  var settings = {
    url: urlresource + "/update_chart_count/",
    method: "POST",
    timeout: 0,
    processData: false,
    mimeType: "multipart/form-data",
    contentType: false,
    data: form,
  };

  $.ajax(settings).done(function (response) {});
}
