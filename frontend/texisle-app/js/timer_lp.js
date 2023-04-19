var time = Math.floor(Date.now() /1000)

window.addEventListener("focus", function(event) { 
    // console.log("window has focus"); 
    Clock.resume(); 
    // console.log(time)
    var diff = Math.floor(Date.now() /1000) - time;
    console.log(diff)
    if (diff > 30) {
        location.reload()
        }
    if(time == null || time == "" || isNaN(time) || typeof time === 'undefined'){
        window.location.href = "./index.html";
    }
    }, false);

window.addEventListener("blur", function(event) { 
    // console.log("window lost focus"); 
    Clock.pause(); 
    time = Math.floor(Date.now() /1000)
    }, false);
