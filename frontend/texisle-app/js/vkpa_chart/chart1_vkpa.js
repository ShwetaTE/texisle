$(function () {
  Highcharts.setOptions({
    lang: {
      numericSymbols: null,
      thousandsSep: ",",
    },
    global: {
      timezoneOffset: 33,
    },
  });

  var form = new FormData();
  form.append("chart", "vk.pa");
  let interval = 60;
  country = "x";
  const local = Intl.DateTimeFormat().resolvedOptions().timeZone.split("/");
  if (local[0] == "America") {
    interval = 5;
    country = "America";
  }
  console.log("heey");
  // if ((local[0] != "America" && local[1] == "Tokyo") || local[1] == "Paris")
  //   interval = 5;
  var settings = {
    url: urlresource + `/y_data_ts_1/${interval}/${country}`,
    method: "POST",
    timeout: 0,
    dataType: "JSON",
    processData: false,
    mimeType: "multipart/form-data",
    contentType: false,
    data: form,
  };

  //console.log(data,"-----------")
  $.ajax(settings).done(function (response) {
    // console.log(response);
    // var data = response[0];
    // console.log(response);
    let startpoint = [];
    let endpoint = [];
    let tickpoint = [];
    if (response[1].length) {
      // console.log(response[1]);
      response[1].forEach((el, i) => {
        console.log(el[0]);
        // console.log(new Date(el[0] + " " + "GMT+0000").valueOf());
        response[1][i][0] = Number(
          new Date(el[0] + " " + "GMT+0000").valueOf()
        );
        // console.log(el[0] + " " + "GMT+0000");
      });
    }
    // console.log(response);
    // console.log(data);
    var data = response[1];
    // console.log(data);
    if (response.length) {
      // console.log(response[1]);
      response[0].forEach((el, index) => {
        const date = new Date(el).getDate();
        tickpoint.push(date);
        const lastDate = new Date(response[0][index - 1]);
        if (index !== 0 && Math.abs(date - lastDate.getDate()) > 1) {
          // console.log(lastDate.valueOf());
          startDate = new Date(lastDate.valueOf() + 3600 * 1000 * 24);
          endDate = new Date(el);
          startpoint.push({
            date: startDate.getDate(),
            month: startDate.getMonth(),
            year: startDate.getFullYear(),
          });
          // console.log(new Date(el).valueOf());
          endpoint.push({
            date: endDate.getDate(),
            month: endDate.getMonth(),
            year: endDate.getFullYear(),
          });
          // console.log(startpoint, endpoint);
        }
        console.log("STATRT", startpoint, endpoint);
      });
      // console.log(tickpoint);
    }
    // console.log("data", data);
    Highcharts.chart("container_vkpa_1", {
      chart: {
        // spacingTop: 0,
        // width: 375,
        height: 280,
        backgroundColor: "#1C1C1E",
        style: {
          fontFamily: "'Unica One', sans-serif",
        },
        plotBorderColor: "#606063",
        events: {
          load: function () {
            // console.log(this);
            var firstValue = this.series[0].processedYData[0];
            var endValue =
              this.series[0].processedYData[
                this.series[0].processedYData.length - 1
              ];
            var val_diff = endValue - firstValue;
            // console.log(this.series[0].color)
            if (val_diff < 0) {
              this.series[0].update({
                color: "#E62E2D",
                fillColor: "#e62d2d46",
              });
            }
          },
        },
      },
      title: {
        text: "",
      },
      tooltip: {
        distance: 0,
        outside: true,
        positioner: function (labelWidth, labelHeight, point) {
          return { x: 150, y: 189 };
        },
        formatter: function () {
          var y = this.y.toFixed(2);
          var ts = this.x;
          //ts = (ts+(tzone_diff*60000));

          const loc = Intl.DateTimeFormat().resolvedOptions().timeZone;
          var date = new Date(ts).toLocaleString("en-US", { timeZone: loc });
          var convDate = new Date(date);
          var day = convDate.getDate();
          var month = convDate.getMonth();
          var year = convDate.getFullYear();
          var hour = convDate.getHours();
          var notation = "AM";
          if (hour < 12) {
            notation = "AM";
          }
          if (hour >= 12) {
            notation = "PM";
            hour = hour == 12 ? 12 : hour - 12;
          }

          var minute = convDate.getMinutes();
          var seconds = convDate.getSeconds();
          if (minute < 10) {
            minute = `0${minute}`;
          }
          if (seconds < 10) {
            seconds = `0${seconds}`;
          }
          var d = new Date(year, month, day, hour, minute);
          var month_name = d.toLocaleString("default", { month: "short" });
          var x =
            month_name +
            " " +
            day +
            ", " +
            year +
            " " +
            hour +
            ":" +
            minute +
            " " +
            notation;
          // console.log(x)
          input = "<b>" + x + "<b><br><br>" + "<b> $ " + y + "</b>";
          return [input];
        },
        shadow: false,
        borderWidth: 0,
        backgroundColor: "#1c1c1e00",
        style: {
          color: "white",
        },
      },
      credits: {
        enabled: false,
      },
      xAxis: {
        crosshair: {
          width: 0.5,
          color: "#9bb556",
        },
        type: "datetime",

        labels: {
          formatter() {
            // console.log(this.value);
            const date = new Date(this.value);
            // const weekday = date.toLocaleString("en-US", {
            //   weekday: "short",
            // });
            // console.log(weekday, this.value);
            return Highcharts.dateFormat("%e", this.value);
            // return weekday;
          },
          style: {
            color: "#FFFFFF",
            fontWeight: "bold",
            fontSize: 15,
          },
        },

        tickInterval: 24 * 3600 * 1000,
        startOfWeek: 0,
        // type: 'datetime',
        // dateTimeLabelFormats: {
        //   day: "%e",
        // },
        gridLineColor: "#242424",
        gridLineWidth: 1.5,
        // tickPositioner: function () {
        //   var position = [];
        //   // console.log(this);
        //   var date = new Date(this.tickPositions[2]);
        //   console.log("datttte", date.toUTCString());
        //   position = this.tickPositions.filter((el, index) => {
        //     const date = new Date(el).getDate();
        //     return tickpoint.includes(date);
        //   });
        //   position.forEach((el) => {
        //     console.log(new Date(el));
        //   });
        //   return position;
        // },
        breaks: [
          {
            from: Date.UTC(
              startpoint[0]?.year,
              startpoint[0]?.month,
              startpoint[0]?.date,
              0
            ),
            to: Date.UTC(
              endpoint[0]?.year,
              endpoint[0]?.month,
              endpoint[0]?.date,
              0
            ),
            breakSize: 0,
          },
          {
            from: Date.UTC(
              startpoint[1]?.year,
              startpoint[1]?.month,
              startpoint[1]?.date,
              0
            ),
            to: Date.UTC(
              endpoint[1]?.year,
              endpoint[1]?.month,
              endpoint[1]?.date,
              0
            ),
            breakSize: 0,
          },
          {
            from: Date.UTC(2023, 1, 21, 15, 01),
            to: Date.UTC(2023, 1, 21, 23, 59),
            breakSize: 0,
            repeat: 3600 * 1000 * 24,
          },
          {
            from: Date.UTC(2023, 1, 21, 1, 1),
            to: Date.UTC(2023, 1, 21, 6, 59),
            repeat: 3600 * 1000 * 24,
          },
          {
            from: data[1][data[1].length - 1][0] + 1000,
            to: data[1][data[1].length - 1][0] + 24 * 3600 * 1000, //hours*seconds*milliseconds
            breakSize: 0,
          },
        ],
      },
      yAxis: {
        labels: {
          format: "{value:,.0f}",
          style: {
            color: "#FFFFFF",
            fontWeight: "bold",
            align: "right",
            fontSize: 15,
          },
        },
        title: {
          text: "",
          style: {
            color: "#FFFFFF",
            fontWeight: "bold",
          },
        },
        gridLineColor: "#242424",
        gridLineWidth: 1.5,
      },
      legend: {
        enabled: false,
      },
      plotOptions: {
        area: {
          fillColor: "#a59a001c",
          linearGradient: {
            x1: 0,
            y1: 1,
            x2: 0,
            y2: 0,
          },
          stops: [
            [0, Highcharts.getOptions().colors[1]],
            [
              1,
              Highcharts.color(Highcharts.getOptions().colors[2])
                .setOpacity(0)
                .get("rgba"),
            ],
          ],
          marker: {
            radius: 1,
          },
          lineWidth: 2.5,
          states: {
            hover: {
              lineWidth: 2.5,
            },
          },
          threshold: null,
        },
      },

      series: [
        {
          type: "area",
          name: "Spot Price",
          data: data,
          color: "#9bb556",
          // lineColor: '#70843A',
          lineWidth: 2.5,
        },
      ],
    });
  });
});
