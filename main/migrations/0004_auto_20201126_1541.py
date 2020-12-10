# Generated by Django 3.1.3 on 2020-11-26 10:41

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_makepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makepost',
            name='post_img',
            field=models.ImageField(upload_to=main.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='makepost',
            name='post_user',
            field=models.CharField(max_length=50),
        ),
    ]
