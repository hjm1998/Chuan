$(function () {
    $("#make_order").click(function () {
        var addressid = $("#address").find("li[class=selected]").attr("addressid");
        $.getJSON('/orders/makeorder/', {'addressid': addressid}, function (data) {
            if (data['status'] === 200) {
                window.open("/orders/orderdetail/?orderid=" + data['order_id'], target = "_self")
            }
        })
    });

    $("#address li").click(function () {
        $(this).siblings('li').removeClass('selected');  // 删除其他兄弟元素的样式
        $(this).addClass('selected');                            // 添加当前元素的样式
        var name = $(this).children("#a-name").text();
        var address = $(this).children("#a-address").text();
        var phone = $(this).children("#a-phone").text();

        $(".pay-count-addr").html('寄送至：' + name + '&nbsp;收货人：' + address + '&nbsp;' + phone);

    });

    $(".payment-item").click(function () {
        $(this).siblings('li').removeClass('pay-selected');  // 删除其他兄弟元素的样式
        $(this).addClass('pay-selected');                            // 添加当前元素的样式
    });
});

