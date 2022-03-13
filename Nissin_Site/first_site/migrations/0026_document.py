# Generated by Django 4.0 on 2022-02-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_site', '0025_alter_announcement_type_alter_news_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel_hu', models.CharField(max_length=50)),
                ('short_text_hu', models.CharField(max_length=250)),
                ('titel_en', models.CharField(max_length=50)),
                ('short_text_en', models.CharField(max_length=250)),
                ('valid_from', models.DateField(blank=True)),
                ('valid_until', models.DateField(blank=True)),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('picked', models.CharField(max_length=50)),
            ],
        ),
    ]
