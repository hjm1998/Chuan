# Generated by Django 2.2.9 on 2020-02-17 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchant', '0002_goods_project'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_goods_num', models.IntegerField(default=1, verbose_name='商品总数')),
                ('c_is_select', models.BooleanField(default=True, verbose_name='商品是否选中')),
                ('c_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.Goods', verbose_name='商品ID')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users', verbose_name='用户ID')),
            ],
            options={
                'db_table': 'chuan_cart',
            },
        ),
    ]