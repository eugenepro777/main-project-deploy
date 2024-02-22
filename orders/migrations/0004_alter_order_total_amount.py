# Generated by Django 4.2.9 on 2024-02-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=10, verbose_name='Сумма заказа'),
        ),
    ]