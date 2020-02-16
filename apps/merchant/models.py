from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Merchant(models.Model):
    m_merchantName = models.CharField(max_length=32, unique=True, verbose_name='商家名')
    m_password = models.CharField(max_length=256, verbose_name='商家密码')
    m_phone = models.CharField(max_length=13, unique=True, verbose_name='商家手机号')
    m_email = models.CharField(max_length=64, unique=True, verbose_name='商家邮箱号')
    m_icon = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='商家头像')
    m_idCard = models.CharField(max_length=18, unique=True, verbose_name='商家身份证')
    m_idCard_front = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='商家身份证正面照')
    m_idCard_back = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='商家身份证背面照')
    is_active = models.BooleanField(default=False, verbose_name='商家激活状态')
    is_delete = models.BooleanField(default=False, verbose_name='商家是否删除')

    class Meta:
        db_table = 'chuan_merchant'


class Project(models.Model):
    STATUS_CHOICES = (
        ('readyto', '即将开始'),
        ('funding', '众筹中'),
        ('success', '众筹成功'),
        ('failed', '众筹失败'),
    )
    p_title = models.CharField(max_length=32, verbose_name='项目名称')
    p_introText = models.TextField(verbose_name='项目简介')
    p_classify = models.CharField(max_length=16, verbose_name='项目分类')
    p_introImg = models.ImageField(upload_to='project/%Y/%m/%d', verbose_name='简介图片')
    p_detail = models.ImageField(upload_to='project/%Y/%m/%d', verbose_name='详细图片')
    p_days = models.IntegerField(default=30, verbose_name='众筹期限')
    p_follow = models.IntegerField(default=0, verbose_name='关注数')
    p_target = models.IntegerField(verbose_name='目标金额')
    p_already = models.IntegerField(default=0, verbose_name='已筹金额')
    p_status = models.CharField(default='readyto', max_length=20, choices=STATUS_CHOICES, verbose_name='项目状态')


    class Meta:
        db_table = 'chuan_project'


class Goods(models.Model):
    g_title = models.CharField(max_length=32, verbose_name='商品名称')
    g_detail = models.TextField(verbose_name='商品详细')
    g_price = models.IntegerField(verbose_name='商品价格')
    g_sold = models.IntegerField(default=0, verbose_name='商品已定数量')
    g_stock = models.IntegerField(default=99999999, verbose_name='商品库存')
    g_postage = models.IntegerField(default=0, verbose_name='配送费')
    g_project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='商品项目')

    class Meta:
        db_table = 'chuan_goods'
