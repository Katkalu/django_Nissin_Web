# Generated by Django 4.0 on 2022-01-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_site', '0014_delta_time_delete_safe_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='delta_time',
            name='title',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
