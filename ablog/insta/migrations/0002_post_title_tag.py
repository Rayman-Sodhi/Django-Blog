# Generated by Django 3.1.3 on 2020-11-13 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Instagram', max_length=255),
        ),
    ]