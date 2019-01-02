# Generated by Django 2.0.4 on 2018-12-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181130_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='real_name',
        ),
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(choices=[('admin', '管理组'), ('dev', '开发组')], default='dev', max_length=20, verbose_name='用户组'),
        ),
    ]