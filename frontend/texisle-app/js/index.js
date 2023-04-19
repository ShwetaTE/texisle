document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    // Cordova is now initialized. Have fun!

    console.log('Running cordova-' + cordova.platformId + '@' + cordova.version);
    //document.getElementById('deviceready').classList.add('ready');
    var deviceID = device.uuid;
    sessionStorage.setItem("deviceID", deviceID);
    window.open = cordova.InAppBrowser.open;
    document.addEventListener("pause", onPause, false);
    document.addEventListener("resume", onResume, false);

    // console.log('Received Event: ' + id);

    function onPause() {
        Clock.pause(); 
    }
    
    function onResume() {
        Clock.resume(); 
    }

    checkConnection()
    // ClockFinal.restart();
    // sessionStorage.setItem("Totaltimer", 0);
}

function checkConnection() {
    var networkState = navigator.connection.type;

    var states = {};
    states[Connection.UNKNOWN]  = 1;
    states[Connection.ETHERNET] = 1;
    states[Connection.WIFI]     = 1;
    states[Connection.CELL_2G]  = 1;
    states[Connection.CELL_3G]  = 1;
    states[Connection.CELL_4G]  = 1;
    states[Connection.CELL]     = 1;
    states[Connection.NONE]     = 0;

    // window.alert('Connection type: ' + states[networkState]);

    if(states[networkState] == 0){
        console.log("Oops! You are offline now!");
        window.location = "./offline.html"
    }
}