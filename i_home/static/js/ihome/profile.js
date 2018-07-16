function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

// $('#btn').on('click', function () {
//     var url = $('#img').val();
//     $.ajax({
//         url: '/ihome/user/',
//         type: 'PUT',
//         data: {'avatar': url},
//         dataType: 'json',
//         success: function (data) {
//             console.log(data);
//             if(data.code == '200'){
//                 $('#user-avatar').attr('src', data.user.url)
//             }
//         },
//         error: function (data) {
//             alert(data)
//         }
//     })
// });

$('#form-avatar').submit(function () {
    $(this).ajaxSubmit({
        url: '/ihome/user/',
        type: 'PUT',
        dataType: 'json',
        success: function(data) {
            if (data.code == '200') {
                $('#user-avatar').attr('src', data.url)
            }
        },
        error: function (data) {
            alert(data)
        }
    });
    return false;
});


$('#form-name').submit(function () {
    $('.error-msg').hide();
    var name = $('#user-name').val();
    $.ajax({
        url: '/ihome/user/',
        type: 'PUT',
        data: {'name': name},
        dataType: 'json',
        success: function (data) {
            if (data.code == '200'){

            }else{
                $('.error-msg').html('<i class="fa fa-exclamation-circle">' + data.msg + '</i>');
                $('.error-msg').show();
            }

        },
        error: function (data) {
            alert('请求失败')
        }
    });
    return false;
});



