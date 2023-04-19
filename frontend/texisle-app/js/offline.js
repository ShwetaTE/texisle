// console.log("offline page")

window.addEventListener("online", function () {
    console.log("You are online now!");
});

window.addEventListener("offline", function () {
    console.log("Oops! You are offline now!");
    window.location = "./offline.html"
});