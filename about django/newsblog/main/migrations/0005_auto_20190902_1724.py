# Generated by Django 2.2.4 on 2019-09-02 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190902_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='tech_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_news_title', models.CharField(max_length=200)),
                ('tech_news_content', models.TextField(blank=True)),
                ('tech_news_published', models.DateTimeField(default=datetime.datetime(2019, 9, 2, 17, 24, 49, 875896), verbose_name='date published')),
                ('tech_news_image', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
        migrations.AlterField(
            model_name='story',
            name='story_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 17, 24, 49, 875896), verbose_name='date published'),
        ),
    ]
