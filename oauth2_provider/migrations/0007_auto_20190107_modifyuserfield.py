# Generated by Django 2.1.4 on 2019-01-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0006_auto_20171214_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='user',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.CharField(blank=True, default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='grant',
            name='user',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='user',
            field=models.CharField(max_length=24),
        ),
    ]
