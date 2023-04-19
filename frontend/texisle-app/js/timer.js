window.addEventListener(
  "focus",
  function (event) {
    // console.log("window has focus");
    Clock.resume();
    location.reload();
  },
  false
);

window.addEventListener(
  "blur",
  function (event) {
    // console.log("window lost focus");
    Clock.pause();
  },
  false
);
