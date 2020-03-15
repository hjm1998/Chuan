function projectHide() {
    document.getElementById('project-module').style.display = 'none';
    document.getElementById('goods-module').style.display = 'block';
}

function projectShow() {
    document.getElementById('project-module').style.display = 'block';
    document.getElementById('goods-module').style.display = 'none';
}

$(function () {

    $("#newGoods").click(function () {
        var parentdiv = "                    <div id=\"new-goods\">\n" +
            "                        <div class=\"goods-Texts clear\">\n" +
            "                            <div class=\"text-tip\" style=\"float: left\">商品名称</div>\n" +
            "                            <input type=\"text\" placeholder=\"商品名称\" class=\"form-control goods-inputText\" name=\"g_title\">\n" +
            "                        </div>\n" +
            "\n" +
            "                        <div class=\"goods-Texts clear\">\n" +
            "                            <div class=\"text-tip\" style=\"float: left\">商品简介</div>\n" +
            "                            <textarea placeholder=\"项目简介\" class=\"goods-introText\" name=\"g_detail\"></textarea>\n" +
            "                        </div>\n" +
            "\n" +
            "                        <div class=\"goods-Texts clear\">\n" +
            "                            <div class=\"text-tip\" style=\"float: left\">商品价格</div>\n" +
            "                            <input type=\"text\" placeholder=\"商品价格\" class=\"form-control goods-inputText\" name=\"g_price\">\n" +
            "                        </div>\n" +
            "\n" +
            "                        <div class=\"goods-Texts clear\">\n" +
            "                            <div class=\"text-tip\" style=\"float: left\">商品库存</div>\n" +
            "                            <input type=\"text\" placeholder=\"商品库存\" class=\"form-control goods-inputText\" name=\"g_stock\">\n" +
            "                        </div>\n" +
            "\n" +
            "                        <div>\n" +
            "                            <div class=\"text-tip\">上传商品封面</div>\n" +
            "                            <input type=\"file\" name=\"g_img\">\n" +
            "                        </div>\n" +
            "\n" +
            "                        <button type=\"button\" class=\"btn btn-success goods-add-btn\" id=\"addGoods\" id=\"addGoods\">\n" +
            "                            新建商品\n" +
            "                        </button>\n" +
            "\n" +
            "                        <button type=\"button\" class=\"btn btn-default goods-add-btn\" id=\"delGoods\" id=\"delGoods\">\n" +
            "                            取消\n" +
            "                        </button>\n" +
            "                    </div>";
        $("#goods-list").append(parentdiv)
    });


    $(document).on('click', '#delGoods', function () {
        $(this).parents("#new-goods").remove();
    });

    $(document).on('click', '#addGoods', function () {
        $(this).parents("#new-goods").css('display', 'none');
    });

});