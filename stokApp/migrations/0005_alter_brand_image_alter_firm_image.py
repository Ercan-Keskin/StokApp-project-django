# Generated by Django 4.2.3 on 2023-09-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stokApp', '0004_alter_purchases_price_total_alter_sales_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='image/'),
        ),
    ]
