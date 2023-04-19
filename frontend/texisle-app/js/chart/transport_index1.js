$(function () {
  try {
    Highcharts.setOptions({
      lang: {
        numericSymbols: null,
        thousandsSep: ','
      }
    });

    var data = JSON.parse(window.localStorage.getItem("transport"));
    Highcharts.chart('container_transport_index1', {
      chart: {
        width: 100,
        height: 70,
        backgroundColor: '#ff000000',
        style: {
          fontFamily: '\'Unica One\', sans-serif'
        },
        plotBorderColor: '#606063',
        events: {
          load: function () {
            diff = stock.t_index.data;
            if (diff < 0) {
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
        animation: false,
        type: 'area',
        name: 'Spot Price',
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
  }
  catch (err) {
    console.log(err);
    err_pop();
  }

});