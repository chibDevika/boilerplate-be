# Generated by Django 4.0.1 on 2022-01-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
