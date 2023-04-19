function footer_res(res){
    if(res == 1){
        document.getElementById("foot").style.display = 'none';
    }
    else{
        app_end(window.location.pathname)
    }
}

var tab = 1;

function ChangeTab() {
    tab +=1;
    if(tab>5){
        tab = 1;
    }
    // console.log(tab)
    document.getElementById("Tab"+tab).click();
}

function openTab_T(evt, tabname, num) {
    tab = num;
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