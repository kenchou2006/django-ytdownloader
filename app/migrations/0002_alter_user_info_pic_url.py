# Generated by Django 5.0.1 on 2024-02-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='pic_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
