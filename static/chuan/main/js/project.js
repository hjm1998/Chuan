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
    });

    $("#a_focus").click(function () {
        var img = "";
        img = $(this).find("img").attr('src');
        if (img == "/static/img/icon/like.png") {
            $("#like-icon").attr("src", "/static/img/icon/liked.png");
            $("#focus").html("已关注")
        } else {
            $("#like-icon").attr("src", "/static/img/icon/like.png");
            $("#focus").html("关注")
        }
    })
});

