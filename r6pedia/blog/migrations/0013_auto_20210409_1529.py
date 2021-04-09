# Generated by Django 3.1.7 on 2021-04-09 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_category_sub_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='blog.category'),
        ),
    ]
