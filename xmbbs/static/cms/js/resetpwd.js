


$(function () {
    $("#submit").click(function (event) {
        event.preventDefault();  //阻止默认表单提交时间
        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var newpwd2E = $("input[name=newpwd2]");

        var oldpwd = oldpwdE.val();  //拿到表单数据
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        //csrf 使用
            //1、要在模板的meta标签中渲染一个csrf_token
            //2、在ajax请求的头部中设置X-CSRFtoken
        zlajax.post({
            "url":"/cms/resetpwd/",
            "data":{
                "oldpwd":oldpwd,
                "newpwd":newpwd,
                "newpwd2":newpwd2
            },
            'success':function (data) {
                console.log(data);
            },
            'fail':function (error) {
                console.log(error);

            }
        });
    });
});



