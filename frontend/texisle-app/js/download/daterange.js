$(function () {

    var start = moment().subtract(30, 'days');
    var end = moment().subtract(1, 'days');

    function cb1(start) {
        st_date = start;
        $('#startDate').html(st_date.format('MM/DD/YYYY'));
        document.getElementById("startDate").value = start.format('MM/DD/YYYY');
    }
    function cb2(end) {
        end_date = end;
        $('#endDate').html(end.format('MM/DD/YYYY'));
        document.getElementById("endDate").value = end_date.format('MM/DD/YYYY');
    }

    cb1(start);
    cb2(end);

    $('input[name="start"]').daterangepicker({
        // locale: {
        //     format: "MMMM D, YYYY",
        // },
        autoApply: true,
        singleDatePicker: true,
        showDropdowns: true,
        minDate: "01/01/2020",
        maxDate: moment().subtract(1, 'days'),
    }, cb1);

    $('input[name="end"]').daterangepicker({
        autoApply: true,
        singleDatePicker: true,
        showDropdowns: true,
        minDate: "01/01/2020",
        maxDate: moment().subtract(1, 'days'),
        // locale: {
        //     "format": "MMMM D, YYYY",
        // }
    }, cb2);

});

///////////////////////////////////////
// $(function () {

//     // var start = moment()
//     // var end = moment()
//     var start = moment().subtract(30, 'days');
//     var end = moment().subtract(1, 'days');

//     function cb(start, end) {
//         st_date = start;
//         end_date = end;
//         $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
//     }

//     // $('#reportrange').daterangepicker({
//     //     startDate: start.format('MMMM D, YYYY'), //start,
//     //     endDate: end.format('MMMM D, YYYY'), //end,
//     //     showDropdowns: true,
//     //     // minYear: 2020,
//     //     minDate: "01/01/2020",
//     //     maxDate : moment().subtract(1, 'days'),
//     //     ranges: {
//     //        'Last 7 Days': [moment().subtract(7, 'days'), moment().subtract(1, 'days')],
//     //        'Last 30 Days': [moment().subtract(30, 'days'), moment().subtract(1, 'days')],
//     //        'Last 3 Months': [moment().subtract(92, 'days'), moment().subtract(1, 'days')],
//     //        'Last 6 Months': [moment().subtract(184, 'days'), moment().subtract(1, 'days')],
//     //        'Last 1 Year': [moment().subtract(365, 'days'), moment().subtract(1, 'days')],
//     //     }
//     // }, cb);
// cb(start, end);
// });
