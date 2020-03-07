$(function () {
    $("#alipay").click(function () {
        var orderid = $(this).attr("orderid");
        $.getJSON("/orders/payed/", {"orderid": orderid}, function (data) {
            console.log(data);
            if (data['status'] === 200) {
                window.open("/users/mine/", target="_self");
            }
        })
    })
});