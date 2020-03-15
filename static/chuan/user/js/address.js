$(function () {

    $('#closeMyModal1').click(function () {
        $("#myModal1").hide();
        $(".thickbox").hide();
    });

    $('.set_default').click(function () {
        var addrid = $(this).parents(".smc").attr("addrid");
        var logo = $(this).parents(".sm").children(".smt").find('h3');
        var smt = $(".smt").find('span');
        $.getJSON('/users/defaultaddr/', {'addrid': addrid}, function (data) {
            if (data['status'] === 200) {
                smt.remove();
                var default_h3 = "<span>默认地址</span>";
                logo.append(default_h3);
            }
        })
    });

    $('.delete-addr').click(function () {
        var addrid = $(this).parents(".smc").attr("addrid");
        var sm = $(this).parents(".sm");
        $.getJSON('/users/deleteaddr/', {'addrid': addrid}, function (data) {
            if (data['status'] === 200) {
                sm.remove();
            }
        })
    })
});


function addAddressDiag() {
    $("#myModal1").show();
    $(".thickbox").show();
}


