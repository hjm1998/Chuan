from django.db import models

from merchant.models import Goods, Project
from orders.views_constant import ORDER_STATUS_NOT_PAY
from users.models import Users


class Cart(models.Model):
    c_user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='用户ID')
    c_goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品ID')

    c_goods_num = models.IntegerField(default=1, verbose_name='商品总数')
    c_is_select = models.BooleanField(default=True, verbose_name='商品是否选中')

    class Meta:
        db_table = 'chuan_cart'


class Order(models.Model):
    o_user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='用户ID')
    o_price = models.FloatField(default=0, verbose_name='订单价格')
    o_time = models.DateTimeField(auto_now=True, verbose_name='下单时间')
    o_status = models.IntegerField(default=ORDER_STATUS_NOT_PAY, verbose_name='订单状态')

    class Meta:
        db_table = 'chuan_order'


class OrderGoods(models.Model):
    o_order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='订单ID')
    o_goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='订单商品')
    o_goods_num = models.IntegerField(default=1, verbose_name='商品数量')

    class Meta:
        db_table = 'chuan_orderGoods'
