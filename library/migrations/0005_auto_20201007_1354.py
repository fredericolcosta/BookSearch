# Generated by Django 3.1.2 on 2020-10-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20201006_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
