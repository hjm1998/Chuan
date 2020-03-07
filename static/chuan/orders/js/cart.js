$(function () {

    $(".confirm").click(function () {
        var $confirm = $(this);
        var cartid = $confirm.parents(".item-list").attr("cartid");
        $.getJSON("/orders/changecartstate/", {'cartid': cartid}, function (data) {
            if (data['status'] === 200) {
                $(".all-price").html(data['total_price']);
                $(".all-num").html(data['all_num']);
                if (data['is_all_select']) {
                    $(".all_select").find("input").prop("checked", true);
                } else {
                    $(".all_select").find("input").prop("checked", false);
                }
            }
        })
    });

    $(".subShopping").click(function () {
        var $sub = $(this);
        var cartid = $sub.parents(".item-list").attr("cartid");
        var $sum = $(this).parents(".p-quantity").next(".p-sum").children(".sum");
        $.getJSON("/orders/subshopping/", {"cartid": cartid}, function (data) {
            if (data['status'] === 200) {
                $(".all-price").html(data['total_price']);
                $sum.html(data['price_sum']);
                var $span = $sub.next("span");
                $span.html(data['c_goods_num']);
                $(".all-num").html(data['all_num']);
            }
        })
    });

    $(".addShopping").click(function () {
        var $sub = $(this);
        var cartid = $sub.parents(".item-list").attr("cartid");
        var $sum = $(this).parents(".p-quantity").next(".p-sum").children(".sum");
        $.getJSON("/orders/addshopping/", {"cartid": cartid}, function (data) {
            if (data['status'] === 200) {
                $(".all-price").html(data['total_price']);
                $sum.html(data['price_sum']);
                var $span = $sub.prev("span");
                $span.html(data['c_goods_num']);
                $(".all-num").html(data['all_num']);
            }
        })
    });

    $(".all_select").click(function () {
        var $all_select = $(this);
        var select_list = [];
        var unselect_list = [];
        $(".confirm").each(function () {
            var $confirm = $(this);
            var cartid = $confirm.parents(".item-list").attr("cartid");
            if ($confirm.find("input[type='checkbox']").is(':checked')) {
                select_list.push(cartid);
            } else {
                unselect_list.push(cartid);
            }
        });
        if (unselect_list.length > 0) {
            $.getJSON("/orders/allselect/", {"cart_list": unselect_list.join('#')}, function (data) {
                if (data['status'] === 200) {
                    $(".confirm").find("input").prop("checked", true);
                    $(".all-price").html(data['total_price']);
                    $(".all-num").html(data['all_num']);
                    $(".all_select").find("input").prop("checked", true);
                }
            })
        } else {
            if (select_list.length > 0) {
                $.getJSON("/orders/allselect/", {"cart_list": select_list.join('#')}, function (data) {
                    if (data['status'] === 200) {
                        $(".confirm").find("input").prop("checked", false);
                        $(".all-price").html(data['total_price']);
                        $(".all-num").html(data['all_num']);
                        $(".all_select").find("input").prop("checked", false);
                    }
                })
            }
        }
    });

    $("#ordering").click(function () {
        var select_list = [];
        var unselect_list = [];
        $(".confirm").each(function () {
            var $confirm = $(this);
            var cartid = $confirm.parents(".item-list").attr("cartid");
            if ($confirm.find("input[type='checkbox']").is(':checked')) {
                select_list.push(cartid);
            } else {
                unselect_list.push(cartid);
            }
        });
        if (select_list.length === 0) {
            return null
        } else {
            window.open("/orders/ordering/", target = "_self")
        }
    });
});