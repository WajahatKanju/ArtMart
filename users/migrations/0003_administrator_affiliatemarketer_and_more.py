# Generated by Django 4.2.4 on 2023-09-11 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
            },
        ),
        migrations.CreateModel(
            name='AffiliateMarketer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('marketing_campaign', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Affiliate Marketer',
                'verbose_name_plural': 'Affiliate Marketers',
            },
        ),
        migrations.CreateModel(
            name='CustomerServiceRepresentative',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('support_ticket_assignments', models.TextField(blank=True)),
                ('performance_metrics', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Customer Service Representative',
                'verbose_name_plural': 'Customer Service Representatives',
            },
        ),
        migrations.CreateModel(
            name='DataAnalyst',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('data_sources', models.TextField(blank=True)),
                ('analysis_methodologies', models.TextField(blank=True, null=True)),
                ('reports_generated', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Data Analyst',
                'verbose_name_plural': 'Data Analysts',
            },
        ),
        migrations.CreateModel(
            name='DeliveryDriver',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('license_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('vehicle_registration_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Delivery Driver',
                'verbose_name_plural': 'Delivery Drivers',
            },
        ),
        migrations.CreateModel(
            name='FinancialAnalyst',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('financial_data', models.JSONField(blank=True, null=True)),
                ('reports', models.TextField(blank=True, verbose_name='FinancialReport')),
                ('forecasting_models', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Financial Analyst',
                'verbose_name_plural': 'Financial Analysts',
            },
        ),
        migrations.CreateModel(
            name='InventoryManager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('inventory_tracking_data', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Inventory Manager',
                'verbose_name_plural': 'Inventory Managers',
            },
        ),
        migrations.CreateModel(
            name='LegalCounsel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('legal_documents', models.TextField(blank=True)),
                ('legal_cases', models.TextField(blank=True)),
                ('legal_advice', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Legal Counsel',
                'verbose_name_plural': 'Legal Counsel',
            },
        ),
        migrations.CreateModel(
            name='LogisticsCoordinator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('shipping_methods', models.TextField(blank=True)),
                ('tracking_information', models.TextField(blank=True, null=True)),
                ('delivery_schedules', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Logistics Coordinator',
                'verbose_name_plural': 'Logistics Coordinators',
            },
        ),
        migrations.CreateModel(
            name='MarketingManager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('marketing_campaigns', models.TextField(blank=True)),
                ('marketing_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('marketing_strategy', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Marketing Manager',
                'verbose_name_plural': 'Marketing Managers',
            },
        ),
        migrations.CreateModel(
            name='ProductManager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('product_categories', models.TextField(blank=True)),
                ('product_SKUs', models.TextField(blank=True)),
                ('product_descriptions', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Product Manager',
                'verbose_name_plural': 'Product Managers',
            },
        ),
        migrations.CreateModel(
            name='SalesRepresentative',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sales_targets', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Sales Representative',
                'verbose_name_plural': 'Sales Representatives',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaInfluencer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('social_media_profiles', models.TextField(blank=True, null=True)),
                ('follower_count', models.PositiveIntegerField(blank=True, null=True)),
                ('engagement_metrics', models.JSONField(blank=True, null=True)),
                ('content_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Social Media Influencer',
                'verbose_name_plural': 'Social Media Influencers',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('SELLER', 'Seller/Merchant'), ('CUSTOMER', 'CUSTOMER/Shopper')], max_length=50),
        ),
    ]
