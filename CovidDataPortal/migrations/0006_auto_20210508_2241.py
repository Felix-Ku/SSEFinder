# Generated by Django 3.1.7 on 2021-05-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CovidDataPortal', '0005_auto_20210508_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case_record',
            name='id',
        ),
        migrations.AlterField(
            model_name='case_record',
            name='case_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
