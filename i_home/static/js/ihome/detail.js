function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){
});

$(document).ready(function () {
   // alert(location.href);
    var path = location.href;
    var id = path.split('=')[1];
    $.get('/ihome/detail/' + id + '/', function (data) {
        if (data.code == '200'){
            var detail_house = template('house_detail_list', {ohouse:data.house});
            $('.container').append(detail_house)
        }
    var mySwiper = new Swiper ('.swiper-container', {
        loop: true,
        autoplay: 2000,
        autoplayDisableOnInteraction: false,
        pagination: '.swiper-pagination',
        paginationType: 'fraction'
    });
    $(".book-house").show();
    })

});