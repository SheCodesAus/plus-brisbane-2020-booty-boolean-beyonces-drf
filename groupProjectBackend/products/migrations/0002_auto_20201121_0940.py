# Generated by Django 3.0.8 on 2020-11-20 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='justification',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='model_tech',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='os',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='overview',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='spec6',
            field=models.TextField(default=''),
        ),
    ]