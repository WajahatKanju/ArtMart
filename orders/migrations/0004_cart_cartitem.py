# Generated by Django 4.2.4 on 2023-09-14 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
        ('users', '0006_alter_user_payment_preferences'),
        ('orders', '0003_orderstatus_remove_order_product_order_items_return_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer', verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart', verbose_name='Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Cart Item',
                'verbose_name_plural': 'Cart Items',
            },
        ),
    ]