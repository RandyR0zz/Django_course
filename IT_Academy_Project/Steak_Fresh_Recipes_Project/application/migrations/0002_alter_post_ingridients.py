# Generated by Django 4.1.2 on 2022-10-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ingridients',
            field=models.CharField(max_length=1000),
        ),
    ]