# Generated by Django 4.2.3 on 2023-07-24 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'My user', 'verbose_name_plural': 'My users'},
        ),
    ]
