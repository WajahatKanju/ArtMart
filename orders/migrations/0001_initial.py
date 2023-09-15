# Generated by Django 4.2.4 on 2023-09-13 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_initial'),
        ('users', '0005_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_date', models.DateTimeField(auto_created=True)),
                ('payment_method', models.CharField(choices=[('CREDIT/DEBIT CARD', 'Credit/Debit Card'), ('JAZZCASH', 'Jazz Cash'), ('EASYPAISA', 'Easy Paisa'), ('CASH_ON_DELIVERY', 'Cash On Delivery')], max_length=50, verbose_name='Payment Method')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
            ],
        ),
    ]