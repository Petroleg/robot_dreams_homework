# Generated by Django 4.2.3 on 2023-07-24 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0007_alter_purchase_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-date'], 'verbose_name': 'My purchase', 'verbose_name_plural': 'My purchases'},
        ),
    ]
