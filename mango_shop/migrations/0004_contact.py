# Generated by Django 5.1.4 on 2025-03-06 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mango_shop', '0003_rename_product_name_product_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.EmailField(default='', max_length=90)),
                ('phone', models.TextField(default='', max_length=30)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
