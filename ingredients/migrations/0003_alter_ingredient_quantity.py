# Generated by Django 4.0.1 on 2022-02-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_alter_ingredient_distributor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(max_length=10),
        ),
    ]
