function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');
    $.get('/ihome/area_facility', function (data) {
        var area_html_list = '';
        for(var i = 0; i < data.area_list.length; i++){
            var area_html = '<option value="'+ data.area_list[i].id +'"> '+ data.area_list[i].name + '</option>';
            area_html_list += area_html
        }
        $('#area-id').html(area_html_list);
        var facility_html_list = '';
        for(var j = 0; j < data.facility_list.length; j++){
            var facitily_html = '<li>\n' +
                '                   <div class="checkbox">\n' +
                '                       <label>\n' +
                '                           <input type="checkbox" name="facility" value="' + data.facility_list[j].id + '">' + data.facility_list[j].name + '\n' +
                '                       </label>\n' +
                '                   </div>\n' +
                '               </li>';
            facility_html_list += facitily_html
        }
        $('.house-facility-list').html(facility_html_list);
    });
});



$('#form-house-info').submit(function(e){
    e.preventDefault();
    $(this).ajaxSubmit({
        url: '/ihome/newhouse_source/',
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.code = '200'){}
            $('#form-house-info').hide();
            $('#form-house-image').show();
            $('#house-id').val(data.house_id)
        },
        error: function (data) {
            alert('请求失败')
        }
    });
    return false;
});


$('#form-house-image').submit(function (e) {
    e.preventDefault();
    $(this).ajaxSubmit({
        url: '/ihome/house_images/',
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.code == '200'){
                $('.house-image-cons').append('<img src="' + data.image_url + '">')
            }
        },
        error: function (data) {
            alert('上传图片失败')
        }
    })
});