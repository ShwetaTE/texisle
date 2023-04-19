PullToRefresh.init({
    mainElement: '#main', // above which element?
    onRefresh: function (done) {
        setTimeout(function () {
            done(); // end pull to refresh
            alert('refresh');
        }, 1500);
    }
});