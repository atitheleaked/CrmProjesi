# Generated by Django 3.2 on 2021-05-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_userextra_seviye'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextra',
            name='userID',
            field=models.IntegerField(null=True, verbose_name='Kullanıcı ID'),
        ),
    ]
