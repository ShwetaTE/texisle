$(function () {
    Highcharts.setOptions({
        lang: {
            numericSymbols: null,
            thousandsSep: ','
        }
    });

    var form = new FormData();
    form.append("chart", "utica");

    var settings = {
        "url": urlresource + "/rig_data_3/",
        "method": "POST",
        "timeout": 0,
        "dataType": 'JSON',
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
    };

    $.ajax(settings).done(function (response) {
        //console.log(response);
        var data = response
        // console.log(data);
        Highcharts.chart('container6_12', {
            chart: {
              width: 100 ,
              height: 70,
              backgroundColor: '#ff000000',
              style: {
                  fontFamily: '\'Unica One\', sans-serif'
              },
              plotBorderColor: '#606063',
            events: {
              load: function() {
                diff = stock.Utica_data.data;
                if(diff < 0){
                  this.series[0].update({
                    color: '#E62E2D',
                    fillColor: '#e62d2d46'
                  })
                }
              }
            }  
            },
            title: {
          text: ''
        },
        tooltip: {
          distance: 0,
          outside: true,
          positioner: function (labelWidth, labelHeight, point) {
            return { x: 150, y: 189 };
          },
          formatter: function () {
            var y = (this.y).toFixed(2);
            var ts = this.x;
            //ts = (ts+(tzone_diff*60000));
            var date = new Date(ts);
            date.setTime( date.getTime() + date.getTimezoneOffset()*60*1000 );
            var day = date.getDate();
            var month = date.getMonth();
            var year = date.getFullYear();
            var d = new Date(year, month, day)
            var month_name = d.toLocaleString('default', { month: 'short' });
            var x = month_name + " " + day + ", " + year;
            // console.log(x)
            input = '<b>' + x + '<b><br><br>' +
              '<b> $ ' + y + '</b>'
            return [input]
          },
          shadow: false,
          borderWidth: 0,
          backgroundColor: '#1c1c1e00',
          style: {
            color: 'white',
          }
        },
            credits: {
          enabled: false
        },
        xAxis: {
              lineColor: '#3F3D3A',
              lineWidth: 1,
              labels: {
                enabled: false,
              },
              tickWidth: 0,
            },
            yAxis: {
              labels: {
                enabled: false,
              },
              title: {
                text: '',
              },
              gridLineColor: '#242424',
              gridLineWidth: 0.5,
            },
            legend: {
              enabled: false
            },
            tooltip: { enabled: false },
            plotOptions: {
              area: {
                fillColor: '#2b2a1b',
                  linearGradient: {
                    x1: 0,
                    y1: 1,
                    x2: 0,
                    y2: 0
                  },
                  stops: [
                    [0, Highcharts.getOptions().colors[1]],
                    [1, Highcharts.color(Highcharts.getOptions().colors[2]).setOpacity(0).get('rgba')]
                  ],
                marker: {
                  radius: 1
                },
                lineWidth: 2.5,
                states: {
                  hover: {
                    lineWidth: 2.5
                  }
                },
                threshold: null
              }
            },
      
            series: [{
              type: 'area',
              name: '',
              data: data,
              color: '#9bb556',
              // lineColor: '#70843A',
              lineWidth: 2.5,
              states: {
                hover: {
                  enabled: false
                }
              }
            }]
          });

    });

});