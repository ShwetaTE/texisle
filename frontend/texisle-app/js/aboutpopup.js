function aboutfunction() {
    // console.log("show")
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
    var popup2 = document.getElementById("blocker");
    popup2.classList.toggle("show");
  }

  function hidePopup() {
    // console.log("hide")
    var popup = document.getElementById("myPopup");
    popup.classList.remove('show');
    var popup2 = document.getElementById("blocker");
    popup2.classList.remove("show");
  }