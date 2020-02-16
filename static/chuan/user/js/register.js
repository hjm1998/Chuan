$(function () {
    var $username = $('#username_input');
    $username.change(function () {
        var username = $username.val().trim();
        if (username.length) {
            // 用户名发射给服务器进行校验
            $.getJSON('/users/checkuser/', {'username': username}, function (data) {
                var $username_info = $('#username_info');
                if (data['status'] === 200) {
                    $username_info.html('用户名可用').css('color', 'green');
                } else if (data['status'] === 901) {
                    $username_info.html('用户已存在').css('color', 'red');
                }
            });
        }
    });

    var $email = $('#email_input');
    $email.change(function () {
        var email = $email.val().trim();
        var reg = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
        var $email_info = $('#email_info');

        if (email.length) {
            if (reg.test(email)) {
                $.getJSON('/users/checkemail/', {'email': email}, function (data) {
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

    var $button = $('#button');
    $button.click(function () {
        var username = $username.val().trim();
        var email = $email.val().trim();
        if (!username.length) {
            $username_info = $('#username_info');
            $username_info.html('帐号不能为空').css('color', 'red');
        }
        if (!email.length) {
            $email_info = $('#email_info');
            $email_info.html('邮箱不能为空').css('color', 'red');
        }
    });

});


function check() {
    var $username = $("#username_input");
    var username = $username.val().trim();
    if (!username) {
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

    var info_color = $("#username_info").css('color');
    var emailInfo_color = $("#email_info").css('color');

    if (info_color === 'rgb(255, 0, 0)' || emailInfo_color === 'rgb(255, 0, 0)') {
        return false
    }

    $password.val(md5(password));
    $password_confirm.val(md5(password_confirm));

    return true

}