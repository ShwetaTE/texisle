
var ClockFinal = {
    totalSeconds: sessionStorage.getItem("Totaltimer"),
    start: function () {
        // console.log(totalSeconds)
      if (!this.interval) {
          var self = this;
          function pad(val) { return val > 9 ? val : "0" + val; }
          this.interval = setInterval(function () {
            self.totalSeconds += 1;
            var Totaltimer = self.totalSeconds; // pad(Math.floor(self.totalSeconds / 60 % 60)) + ":" + pad(parseInt(self.totalSeconds % 60));
            // console.log(Totaltimer)
            sessionStorage.setItem("Totaltimer", Totaltimer);
          }, 1000);
      }
    },
  
    reset: function () {
      ClockFinal.totalSeconds = null; 
      clearInterval(this.interval);
      delete this.interval;
      sessionStorage.setItem("Totaltimer", 0);
    },
    pause: function () {
      clearInterval(this.interval);
      delete this.interval;
    },  
    resume: function () {
      this.start();
    },
    restart: function () {
      this.reset();
      ClockFinal.start();
    }
  };

ClockFinal.resume();