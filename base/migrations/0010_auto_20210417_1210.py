# Generated by Django 3.1.6 on 2021-04-17 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20210417_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mesajlar',
            old_name='alıcı',
            new_name='alici',
        ),
    ]