
var ClockLP = {
    totalSeconds: sessionStorage.getItem("time"),
    start: function () {
      if (!this.interval) {
          var self = this;
          function pad(val) { return val > 9 ? val : "0" + val; }
          this.interval = setInterval(function () {
            self.totalSeconds += 1;
            var timer_lp = self.totalSeconds; // pad(Math.floor(self.totalSeconds / 60 % 60)) + ":" + pad(parseInt(self.totalSeconds % 60));
            // console.log(timer_lp)
            sessionStorage.setItem("timer_lp", timer_lp);
          }, 1000);
      }
    },
  
    reset: function () {
      ClockLP.totalSeconds = null; 
      clearInterval(this.interval);
      delete this.interval;
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
      ClockLP.start();
    }
  };

//   ClockLP.resume();