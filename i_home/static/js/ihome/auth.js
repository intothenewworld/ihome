function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}


$('#form-auth').submit(function () {
    var id_name = $('#real-name').val();
    var id_card = $('#id_card').val();
    $.ajax({
        url: '/ihome/auths/',
        type: 'put',
        data: {'id_name': id_name, 'id_card': id_card},
        dataType: 'json',
        success: function (data) {
            if (data.code == '200'){
                $('.btn-success').hide();
                $('.error-msg').hide()
            }else{
                $('.error-msg').html('<i class="fa fa-exclamation-circle">' + data.msg +'</i>');
                $('.error-msg').show();
            }
        },
        error: function (data) {
            alert('请求失败')
        }
    });
    return false;
});


$.get('/ihome/auths/', function (data) {
    if (data.code == '200'){
        $('#real-name').val(data.id_name);
        $('#id_card').val(data.id_card);
        $('.btn-success').hide()
    }
});