function logout() {
    $.ajax({
        url: '/ihome/logout/',
        type: 'DELETE',
        dataType: 'json',
        success: function (data) {
            if (data.code == '200'){
                location.href = '/ihome/login/'
            }
        },
        error: function (data) {
            alert('请求失败')
        }
    });
}

// 文档一加载就返回数据给页面
$(document).ready(function(){
    $.get('/ihome/user', function (data) {
        // console.log(data)
        if (data.code == '200'){
            $('#user-mobile').html(data.user.phone);
            $('#user-name').html(data.user.name);
            $('#user-avatar').attr('src', data.user.avatar)
        }
    })
});