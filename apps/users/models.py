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

