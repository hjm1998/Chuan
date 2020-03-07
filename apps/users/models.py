from django.db import models


class Users(models.Model):
    u_username = models.CharField(max_length=32, unique=True, verbose_name='用户名')
    u_password = models.CharField(max_length=256, verbose_name='用户密码')
    u_email = models.CharField(max_length=64, unique=True, verbose_name='用户邮箱')
    u_icon = models.ImageField(upload_to='icons/%Y/%m/%d', verbose_name='用户头像')
    is_active = models.BooleanField(default=False, verbose_name='用户激活状态')
    is_delete = models.BooleanField(default=False, verbose_name='用户是否删除')

    class Meta:
        db_table = 'chuan_user'


class Address(models.Model):
    a_name = models.CharField(max_length=16, verbose_name='收货姓名')
    a_phone = models.CharField(max_length=11, verbose_name='收货手机号码')
    a_address = models.CharField(max_length=256, verbose_name='收货地址')
    a_code = models.CharField(max_length=6, verbose_name='邮政编码')
    a_is_default = models.BooleanField(default=True, verbose_name='默认地址')
    a_user = models.ForeignKey(Users, verbose_name='用户ID', on_delete=models.CASCADE)

    class Meta:
        db_table = 'chuan_address'


class AddressCopy(models.Model):
    a_name = models.CharField(max_length=16, verbose_name='收货姓名')
    a_phone = models.CharField(max_length=11, verbose_name='收货手机号码')
    a_address = models.CharField(max_length=256, verbose_name='收货地址')
    a_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    a_order = models.ForeignKey('orders.Order', verbose_name='订单ID', on_delete=models.CASCADE)

    class Meta:
        db_table = 'chuan_addressCopy'
