# Generated by Django 3.1.7 on 2021-03-30 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'پست', 'verbose_name_plural': 'پست\u200cها'},
        ),
    ]
