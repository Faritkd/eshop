# Generated by Django 4.2.4 on 2023-11-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سبد خرید', 'verbose_name_plural': 'سبدهای خرید کاربران'},
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(verbose_name='نهایی شده/نشده'),
        ),
    ]
