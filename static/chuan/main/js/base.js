$(function () {
    $("#search-submit").click(function () {
        var content = $(this).siblings("#search-input").val();
        window.open("/index/search/?content=" + content, target="_self")
    })
});