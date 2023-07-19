# Generated by Django 4.1.5 on 2023-01-24 07:50

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=255)),
                ('Qdescription', models.TextField()),
                ('Qimage', models.ImageField(upload_to='uploads')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('modelname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='BPage.devices')),
            ],
        ),
    ]
