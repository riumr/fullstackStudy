# Generated by Django 4.1.1 on 2022-10-17 08:38

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=''),
        ),
    ]
