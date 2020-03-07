$(function () {
    $(".subShopping").click(function () {
        console.log('add');
        var $add = $(this);
        var goodsid = $add.attr("goodsid");
        $.get('/orders/addtocart', {'goodsid': goodsid}, function (data) {
            console.log(data);
            if (data['status'] === 302) {
                window.open('/users/login/', target = "_self");
            }
        })
    })
});