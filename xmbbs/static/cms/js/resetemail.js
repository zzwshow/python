
//使用ajax方法  get发送邮件  用来修改邮箱！
$(function () {
    $("#captcha-btn").click(function (event) {
        event.preventDefault();
        var email = $("input[name='email']").val();
        if (!email){
            zlalert.alertInfoToast("请输入邮箱~")
            return;
        }
        zlajax.get({
            'url':'/cms/email_captcha/',
            'data':{
                'email':email
            },
            'success':function (data) {
                if (data['code']===200){
                    zlalert.alertSuccess("邮件发送成功！请注意查收~");
                }else {
                    zlalert.alertInfo(data["message"]);
                }

            },
            'fail':function (error) {
                zlalert.alertNetworkError();

            }

        });


    });

});

//使用ajax 提交用户修改邮箱的信息！
$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();
        var emailE = $("input[name='email']");
        var captchaE = $("input[name='captcha']");

        var email = emailE.val();
        var captcha = captchaE.val();

        zlajax.post({
            'url':'/cms/resetemail/',
            'data':{
                'email':email,
                'captcha':captcha
            },
            'success':function (data) {
                if (data['code']===200){
                    zlalert.alertSuccessToast();
                    emailE.val('');
                    captchaE.val('');

                }else {
                    zlalert.alertInfo(data["message"]);
                }
            },
            'fail':function (error) {
                zlalert.alertNetworkError();

            }

        });

    });

});
