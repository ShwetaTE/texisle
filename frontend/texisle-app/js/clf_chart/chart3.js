$(function () {
    Highcharts.setOptions({
        lang: {
            numericSymbols: null,
            thousandsSep: ','
        }
    });

    var form = new FormData();
    form.append("chart", "CLF");

    var settings = {
        "url": urlresource + "/y_data_3/",
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
        Highcharts.chart('container_clf_3', {
            chart: {
              // spacingTop: 0,
              // width: 375,
              height: 280,
              backgroundColor: '#1C1C1E',
              style: {
                  fontFamily: '\'Unica One\', sans-serif'
              },
              plotBorderColor: '#606063',
            events: {
              load: function() {
                var firstValue = this.series[0].processedYData[0];
                var endValue = this.series[0].processedYData[this.series[0].processedYData.length - 1];
                var val_diff = endValue - firstValue
                // console.log(this.series[0].color)
                if(val_diff < 0){
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
          crosshair: {
            width: 0.5,
            color: '#9bb556',
          },
              type: 'datetime',
              labels: {
                formatter() {
                  // console.log(this.value)
                  return Highcharts.dateFormat('%e  %b', this.value)
                },
                style: {
                  color: '#FFFFFF',
                  fontWeight: 'bold',
                  fontSize: 15
                }
              },
              // type: 'datetime',
              // dateTimeLabelFormats: {
              //   // day: "%e-%b-%y",
              //   month: "%b"
              // },
              gridLineColor: '#242424',
              gridLineWidth: 1.5
            },
            yAxis: {
              labels: {
                format: '{value:,.0f}',
                style: {
                  color: '#FFFFFF',
                  fontWeight: 'bold',
                  align: 'right',
                  fontSize: 15
                }
              },
              title: {
                text: '',
                style: {
                  color: '#FFFFFF',
                  fontWeight: 'bold',
                }
              },
              gridLineColor: '#242424',
              gridLineWidth: 1.5,
            },
            legend: {
              enabled: false
            },
            plotOptions: {
              area: {
                fillColor: '#a59a001c',
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
              name: 'Spot Price',
              data: data,
              color: '#9bb556',
              // lineColor: '#70843A',
              lineWidth: 2.5
            }]
          });

    });

});