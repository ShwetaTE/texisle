$(document).ready(function(){

    var nav_id = document.getElementById('nav-id')
    // console.log(nav_id)
    if(os == 'Android'){
        nav_id.classList.add("navbar-android");
    }
    if(os == 'IOS'){
        nav_id.classList.add("navbar-ios");
    }

    var lp = "landing_page.html";
    var wl = "watchlist.html"
    var co = "carbon_offset.html"
    var fp = "feedback.html"
    var m = "more.html"
    var d = "download_page.html"
    if(os == "IOS") {
        var navbar = 
        '<div class="navigation">'+
            '<ul>'+
                '<li id="home_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+lp+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon name="home-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">Home</span>'+
                    '</a>'+
                '</li>'+
                '<li id="watchlist_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+wl+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon name="eye-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">Watchlist</span>'+
                    '</a>'+
                '</li>'+
                // '<li id="co2_id" class="list">'+
                //     '<a href="#" onclick="app_func_change(\''+co+'\', \''+window.location.pathname+'\')">'+
                //         '<span class="bar"></span>'+
                //         '<span class="icon">'+
                //             '<ion-icon name="flame-outline"></ion-icon>'+
                //         '</span>'+
                //         // '<span class="text">CO<sub>2</sub>&nbspOffset</span>'+
                //         '<span class="text">Carbon Offset</span>'+
                //     '</a>'+
                // '</li>'+
                '<li id="data_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+d+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon class="more_icon-pad" name="analytics-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">Data</sub></span>'+
                    '</a>'+
                '</li>'+
                '<li id="feedback_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+fp+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon name="chatbubbles-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">Feedback</sub></span>'+
                    '</a>'+
                '</li>'+
                '<li id="more_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+m+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon name="menu-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">More</sub></span>'+
                    '</a>'+
                '</li>'+
            '</ul>'+
        '</div>'
    }
    if(os == "Android") {
        var navbar = 
        '<div class="navigation-android">'+
            '<ul>'+
                '<li id="home_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+lp+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon name="home-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">Home</span>'+
                    '</a>'+
                '</li>'+
                '<li id="watchlist_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+wl+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon name="eye-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">Watchlist</span>'+
                    '</a>'+
                '</li>'+
                // '<li id="co2_id" class="list">'+
                //     '<a href="#" onclick="app_func_change(\''+co+'\', \''+window.location.pathname+'\')">'+
                //         '<span class="bar"></span>'+
                //         '<span class="icon">'+
                //             '<ion-icon name="flame-outline"></ion-icon>'+
                //         '</span>'+
                //         // '<span class="text">CO<sub>2</sub>&nbspOffset</span>'+
                //         '<span class="text">Carbon Offset</span>'+
                //     '</a>'+
                // '</li>'+
                '<li id="data_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+d+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon class="more_icon-pad" name="analytics-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">Data</sub></span>'+
                    '</a>'+
                '</li>'+
                '<li id="feedback_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+fp+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon name="chatbubbles-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">Feedback</sub></span>'+
                    '</a>'+
                '</li>'+
                '<li id="more_id" class="list">'+
                    '<a href="#" onclick="app_func_change(\''+m+'\', \''+window.location.pathname+'\')">'+
                    '<span class="bar"></span>'+
                        '<span class="icon">'+
                            '<ion-icon name="menu-outline"></ion-icon>'+
                        '</span>'+
                        '<span class="text">More</sub></span>'+
                    '</a>'+
                '</li>'+
            '</ul>'+
        '</div>'
    }
    
    $('#nav-id').append(navbar);

    const list = document.querySelectorAll('.list');
    function activeLink() {
        list.forEach((item) =>
            item.classList.remove('active'));
        this.classList.add('active')
        // console.log(this)
    }
    list.forEach((item) =>
        item.addEventListener('click', activeLink));

    var path = window.location.pathname;
    var path1 = path.split("/").pop();
    var current_page = path1.substring(0, path1.indexOf("."));
    // console.log(current_page)
    if(current_page == "landing_page"){
        var x = document.getElementById("home_id")
        x.classList.add('active')
    }
    if(current_page == "carbon_offset"){
        var x = document.getElementById("co2_id")
        x.classList.add('active')
    }
    if(current_page == "watchlist"){
        var x = document.getElementById("watchlist_id")
        x.classList.add('active')
    }
    if(current_page == "feedback"){
        var x = document.getElementById("feedback_id")
        x.classList.add('active')
    }
    if(current_page == "more"){
        var x = document.getElementById("more_id")
        x.classList.add('active')
    }
    if(current_page == "download_page"){
        var x = document.getElementById("data_id")
        x.classList.add('active')
    }

});


