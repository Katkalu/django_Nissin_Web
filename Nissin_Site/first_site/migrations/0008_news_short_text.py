# Generated by Django 4.0 on 2022-01-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_site', '0007_alter_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='short_text',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
