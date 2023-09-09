# Generated by Django 4.2.4 on 2023-09-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_payment_preferences'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='business_registration_number',
            field=models.CharField(default='', max_length=50, verbose_name='Business Registration Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='business_type',
            field=models.CharField(choices=[('sole_proprietorship', 'Sole Proprietorship'), ('llc', 'Limited Liability Company (LLC)'), ('corporation', 'corporation')], default='', max_length=50, verbose_name='Business Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='company_name',
            field=models.CharField(default='', max_length=75, verbose_name='Company Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='tax_identification_number',
            field=models.CharField(default='', max_length=50, verbose_name='Tax Identification Number (TIN)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='payment_preferences',
            field=models.CharField(blank=True, choices=[('JAZZ_CASH', 'Jazz Cash'), ('EASY_PAISA', 'Easy Paisa')], max_length=50, null=True, verbose_name='Payment Preferences'),
        ),
    ]
