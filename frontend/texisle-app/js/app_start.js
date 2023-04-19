var st_time = new Date();
console.log(st_time);

var uuid = uuidv4();
sessionStorage.setItem("SessionName", uuid);
sessionStorage.setItem("start_time", st_time);


// sessionStorage.setItem("deviceID", "web1");

function uuidv4() {
    return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
      (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
  }

