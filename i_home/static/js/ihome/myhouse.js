$(document).ready(function(){
    $(".auth-warn").show();

    $.get('/ihome/auth_myhouse', function (data) {
        if (data.code == '200'){
            $('#house_auth').hide();
            console.log(data);
            var house_list_html = '';
            for (var i = 0; i < data.hlist_list.length; i++){

                house_html = '<li>\n' +
                    '              <a href="/ihome/detail/?id='+ data.hlist_list[i].id +'">\n' +
                    '                 <div class="house-title">\n' +
                    '                            <h3>房屋ID:' + data.hlist_list[i].id + ' —— ' + data.hlist_list[i].title + '</h3>\n' +
                    '                 </div>\n' +
                    '                     <div class="house-content">\n' +
                    '                         <img src="' + data.hlist_list[i].image + '">\n' +
                    '                         <div class="house-text">\n' +
                    '                             <ul>\n' +
                    '                                 <li>位于：' + data.hlist_list[i].address + '</li>\n' +
                    '                                 <li>价格：' + data.hlist_list[i].price + '</li>\n' +
                    '                                 <li>发布时间：' + data.hlist_list[i].create_time + '</li>\n' +
                    '                             </ul>\n' +
                    '                         </div>\n' +
                    '                     </div>\n' +
                    '                </a>\n' +
                    '           </li>';


                house_list_html += house_html;
            }
            $('#houses-list').append(house_list_html)
        }else{
            $('.new-house').hide();
        }
    })
});

                // <!--<li>
                //     <a href="#">
                //         <div class="house-title">
                //             <h3>房屋ID:1 —— 房屋标题1</h3>
                //         </div>
                //         <div class="house-content">
                //             <img src="/static/images/home01.jpg">
                //             <div class="house-text">
                //                 <ul>
                //                     <li>位于：西城区</li>
                //                     <li>价格：￥200/晚</li>
                //                     <li>发布时间：2016-11-11 20:00:00</li>
                //                 </ul>
                //             </div>
                //         </div>
                //     </a>
                // </li>
