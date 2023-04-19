
var Clock = {
    totalSeconds: sessionStorage.getItem("time"),
    start: function () {
      if (!this.interval) {
          var self = this;
          function pad(val) { return val > 9 ? val : "0" + val; }
          this.interval = setInterval(function () {
            self.totalSeconds += 1;
            var time = self.totalSeconds; // pad(Math.floor(self.totalSeconds / 60 % 60)) + ":" + pad(parseInt(self.totalSeconds % 60));
            // console.log(time)
            sessionStorage.setItem("timer", time);
          }, 1000);
      }
    },
  
    reset: function () {
      Clock.totalSeconds = null; 
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
      Clock.start();
    }
  };

  Clock.resume();