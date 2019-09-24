# Generated by Django 2.2.4 on 2019-09-02 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190902_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 16, 58, 21, 215809), verbose_name='date published'),
        ),
    ]
