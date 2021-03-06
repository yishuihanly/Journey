# Generated by Django 2.0.4 on 2018-11-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MySQLDatabase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('dbname', models.CharField(max_length=128, verbose_name='MYSQL数据库名')),
                ('host', models.GenericIPAddressField(blank=True, null=True, verbose_name='MYSQL IP地址')),
                ('port', models.PositiveIntegerField(blank=True, default=3306, null=True, verbose_name='MYSQL端口')),
                ('adminuser', models.CharField(max_length=32, verbose_name='MYSQL用户名')),
                ('password', models.CharField(max_length=64, verbose_name='MYSQL密码')),
                ('version', models.CharField(default=5.7, max_length=32, verbose_name='MYSQL版本')),
                ('is_enabled', models.PositiveSmallIntegerField(choices=[(0, '禁用'), (1, '启用')], verbose_name='是否启用')),
            ],
            options={
                'verbose_name': 'MYSQL数据库',
                'verbose_name_plural': 'MYSQL数据库',
                'db_table': 'mysql_databases',
            },
        ),
    ]
