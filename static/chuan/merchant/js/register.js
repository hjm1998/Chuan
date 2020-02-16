$(function () {
    var $merchantName = $('#merchantName_input');
    $merchantName.change(function () {
        var merchantName = $merchantName.val().trim();
        if (merchantName.length) {
            // 用户名发射给服务器进行校验
            $.getJSON('/merchant/checkname/', {'merchantName': merchantName}, function (data) {
                var $merchantName_info = $('#merchantName_info');
                if (data['status'] === 200) {
                    $merchantName_info.html('商家名可用').css('color', 'green');
                } else if (data['status'] === 901) {
                    $merchantName_info.html('商家名已存在').css('color', 'red');
                }
            });
        }
    });

    var $phone = $('#phone_input');
    $phone.change(function () {
        var phone = $phone.val().trim();
        var reg = /^1[3456789]\d{9}$/;
        var $phone_info = $('#phone_info');

        if (phone.length) {
            if (reg.test(phone)) {
                $.getJSON('/merchant/checkphone/', {'phone': phone}, function (data) {
                    if (data['status'] === 200) {
                        $phone_info.html('手机号可用').css('color', 'green');
                    } else if (data['status'] === 903) {
                        $phone_info.html('手机号已存在').css('color', 'red');
                    }
                });
            } else {
                $phone_info.html('请输入正确的手机号').css('color', 'red');
            }
        }
    });

    var $email = $('#email_input');
    $email.change(function () {
        var email = $email.val().trim();
        var reg = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
        var $email_info = $('#email_info');

        if (email.length) {
            if (reg.test(email)) {
                $.getJSON('/merchant/checkemail/', {'email': email}, function (data) {
                    if (data['status'] === 200) {
                        $email_info.html('邮箱号可用').css('color', 'green');
                    } else if (data['status'] === 902) {
                        $email_info.html('邮箱号已存在').css('color', 'red');
                    }
                });
            } else {
                $email_info.html('请输入正确的邮箱号').css('color', 'red');
            }
        }
    });

    var $password_confirm = $('#password_confirm_input');
    $password_confirm.change(function () {
        var password = $('#password_input').val().trim();
        var password_confirm = $password_confirm.val().trim();
        var $password_info = $('#password_info');
        if (password !== password_confirm) {
            $password_info.html('两次密码不一致').css('color', 'red');
        } else {
            $password_info.html('')
        }
    });

    var $idCard = $('#idCard_input');
    $idCard.change(function () {
        var idcardReg = /^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$/;
        var idCard = $idCard.val().trim();
        var $idCard_info = $('#idCard_info');
        if (idCard.length) {
            if (idcardReg.test(idCard)) {
                $.getJSON('/merchant/checkidCard/', {'idCard': idCard}, function (data) {
                    if (data['status'] === 200) {
                        $idCard_info.html('身份证可用').css('color', 'green')
                    } else if (data['status'] === 904) {
                        $idCard_info.html('身份证已存在').css('color', 'red')
                    }
                })
            } else {
                $idCard_info.html('请输入正确的身份证号码').css('color', 'red');
            }
        }
    });

    var $button = $('#button');
    $button.click(function () {
        var merchantName = $merchantName.val().trim();
        var email = $email.val().trim();
        var idCard_front_input = $('#idCard_front_input');
        var idCard_back_input = $('#idCard_back_input');
        var icon_input = $('#icon_input');
        if (!merchantName.length) {
            $merchantName_info = $('#merchantName_info');
            $merchantName_info.html('帐号不能为空').css('color', 'red');
        }
        if (!email.length) {
            $email_info = $('#email_info');
            $email_info.html('邮箱不能为空').css('color', 'red');
        }
        if (idCard_front_input.val() === '') {
            var $idCard_front_input = $('#idCard_front_info');
            $idCard_front_input.html('身份证正面照不能为空').css('color', 'red');
        }
        if (idCard_back_input.val() === '') {
            var $idCard_back_info = $('#idCard_back_info');
            $idCard_back_info.html('身份证背面照不能为空').css('color', 'red');
        }
        if (icon_input.val() === '') {
            var $icon_info = $('#icon_info');
            $icon_info.html('商家图标不能为空').css('color', 'red');
        }
    });

    var $idCard_front_input = $('#idCard_front_input');
    $idCard_front_input.change(function () {
        if ($idCard_front_input.val() !== '') {
            var $idCard_front_info = $('#idCard_front_info');
            $idCard_front_info.html('')
        }
    });

    var $idCard_back_input = $('#idCard_back_input');
    $idCard_back_input.change(function () {
        if ($idCard_back_input.val() !== '') {
            var $idCard_back_info = $('#idCard_back_info');
            $idCard_back_info.html('')
        }
    });

    var $icon_input = $('#icon_input');
    $icon_input.change(function () {
        if ($icon_input.val() !== '') {
            var $icon_info = $('#icon_info');
            $icon_info.html('')
        }
    });

});


function check() {


    var $merchantName = $('#merchantName_input');
    var merchantName = $merchantName.val().trim();
    if (!merchantName) {
        return false
    }

    var $password = $("#password_input");
    var password = $password.val().trim();
    var $password_confirm = $("#password_confirm_input");
    var password_confirm = $password_confirm.val().trim();
    if (!password || !password_confirm || password !== password_confirm) {
        return false
    }

    var $email = $("#email_input");
    var email = $email.val().trim();
    if (!email) {
        return false
    }

    var nameInfo_color = $("#merchantName_info").css('color');
    var phoneInfo_color = $("#phone_info").css('color');
    var emailInfo_color = $("#email_info").css('color');
    var idCartInfo_color = $("#idCard_info").css('color');
    var $idCard_front_input = $('#idCard_front_info');
    var $idCard_back_info = $('#idCard_back_info');

    if (nameInfo_color === 'rgb(255, 0, 0)' || phoneInfo_color === 'rgb(255, 0, 0)' || emailInfo_color === 'rgb(255, 0, 0)' || idCartInfo_color === 'rgb(255, 0, 0)' || $idCard_front_input === 'rgb(255, 0, 0)' || $idCard_back_info === 'rgb(255, 0, 0)') {
        return false
    }

    $password.val(md5(password));
    $password_confirm.val(md5(password_confirm));

    return true

}