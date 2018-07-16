//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);
    $(".order-accept").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-accept").attr("order-id", orderId);
    });
    $(".order-reject").on("click", function(){
        var orderId = $(this).parents("li").attr("order-id");
        $(".modal-reject").attr("order-id", orderId);
    });
});


$(document).ready(function () {
    $.get('/order/fd/', function (data) {
        // console.log(data);
        if (data.code == '200'){
            var lorders_html = template('lorders_list', {orders:data.olist});
            $('.orders-list').html(lorders_html)
        }

        // 接单按钮
        $('.order-accept').on('click', function () {
            // alert($(this).parents('li').attr('order-id'));
            var order_id = $(this).parents('li').attr('order-id');
            $('.modal-accept').attr('order_id', order_id)

        });

        $('.modal-accept').on('click', function () {
            var order_id = $(this).attr('order_id');
            $.ajax({
                url: '/order/lorders/' + order_id + '/',
                type: 'PATCH',
                data: {'status': 'WAIT_PAYMENT'},
                dataType: 'json',
                success:function (data) {
                    if(data.code == '200'){
                        $('#btn_accept_regect_' + order_id).hide();
                        $('#accept-modal').modal('hide');
                        $('#order_status_' + order_id).html('待支付')
                    }
                },
                error: function (data) {
                    alert('确认接单失败')
                }
            })
        });

        // 拒单按钮
        $('.order-reject').on('click', function () {
            // alert($(this).parents('li').attr('order-id'));
            var order_id = $(this).parents('li').attr('order-id');
            $('.modal-reject').attr('order_id', order_id)

        });
        $('.modal-reject').on('click', function () {
            var order_id = $(this).attr('order_id');
            var reject_reason = $('#reject-reason').val();
            $.ajax({
                url: '/order/lorders/' + order_id + '/',
                type: 'PATCH',
                data: {'status': 'REJECTED', 'comment': reject_reason},
                dataType: 'json',
                success:function (data) {
                    if(data.code == '200'){
                        $('#btn_accept_regect_' + order_id).hide();
                        $('#reject-modal').modal('hide');
                        $('#order_status_' + order_id).html('已拒单')

                    }
                },
                error: function (data) {
                    alert('确认拒绝接单失败')
                }
            })
        });

    })
});