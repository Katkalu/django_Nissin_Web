# Generated by Django 4.0 on 2022-02-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_site', '0027_document_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='department',
            field=models.CharField(choices=[('it', 'IT'), ('hr', 'HR'), ('penzugy', 'PENZUGY'), ('egyeb', 'EGYÉB')], default='1', max_length=15),
        ),
        migrations.AlterField(
            model_name='document',
            name='valid_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='valid_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
