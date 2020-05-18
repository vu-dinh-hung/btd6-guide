# Generated by Django 3.0.6 on 2020-05-17 15:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200517_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='post_content',
            field=tinymce.models.HTMLField(default='', verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_slug',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.CharField(max_length=200),
        ),
    ]