# Generated by Django 4.0.1 on 2022-02-18 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0007_rename_logs_logs_distributors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='telephone',
            field=models.CharField(max_length=15),
        ),
    ]