# Generated by Django 5.1.1 on 2024-12-20 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_cartitem_cart'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]