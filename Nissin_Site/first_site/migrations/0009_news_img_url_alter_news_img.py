# Generated by Django 4.0 on 2022-01-11 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_site', '0008_news_short_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img_url',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='first_site/static/upload_images/'),
        ),
    ]
