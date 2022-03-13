# Generated by Django 4.0 on 2022-02-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_site', '0028_alter_document_department_alter_document_valid_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, upload_to='upload_docu'),
        ),
        migrations.AddField(
            model_name='document',
            name='file_titel_en',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='document',
            name='file_titel_hu',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='department',
            field=models.CharField(choices=[('it', 'IT'), ('hr', 'HR'), ('penzugy', 'PÉNZÜGY'), ('egyeb', 'EGYÉB')], default='1', max_length=15),
        ),
    ]
