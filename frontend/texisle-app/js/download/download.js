$(function() {
    var st_date = "";
    var end_date = "";
    // const interval1 = setInterval(function() {
    //     // method to be executed;
    //     var e1 = document.getElementById("error1");
    //     var e2 = document.getElementById("error2");
    //     e1.style.display = "none";
    //     e2.style.display = "none";
    //   }, 3000);

    // const interval2 = setInterval(function() {
    //     // method to be executed;
    //     var l = document.getElementById("loader");
    //     l.style.display = "none";
    //   }, 10000);
     

});


function dropdown(param1, tab) {
    console.log(tab)
    remove_active(tab);
    // $(tab).addClass('active');
    tab.classList.toggle("active");
    var x = document.getElementById(param1);
    // x.classList.toggle("show");
    if (x.style.display == "none") {
        x.style.display = "block";
        close_dd(param1);
    } else {
        x.style.display = "none";
    }
}

function close_dd(param) {
    var list_id = ["tab1", "tab2", "tab3", "tab4", "tab5", "tab6", "tab7"];
    // console.log(list_id);
    list_id = list_id.filter(e => e !== param);
    // console.log(list_id);
    for (var i = 0; i < list_id.length; i++) {
        // console.log(list_id[i]);
        var x = document.getElementById(list_id[i]);
        x.style.display = "none";
    }
}

function remove_active(tab){
    var id = tab.id;
    var list_id = ["inner_card_1", "inner_card_2", "inner_card_3", "inner_card_4", "inner_card_5", "inner_card_6", "inner_card_7"];
    list_id = list_id.filter(item => item !== id)
    console.log(list_id)
    for (var i = 0; i < list_id.length; i++) {
        var element = document.getElementById(list_id[i]);
        element.classList.remove("active");
        // $(list_id[i]).removeClass('active');
    }
}