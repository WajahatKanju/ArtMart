# Generated by Django 4.2.4 on 2023-08-31 16:49

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_attributevalue_attribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevalue',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.attribute'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='attribute_value',
            field=smart_selects.db_fields.ChainedForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_values', to='products.attributevalue'),
        ),
    ]
