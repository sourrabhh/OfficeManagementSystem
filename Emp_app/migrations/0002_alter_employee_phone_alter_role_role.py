# Generated by Django 4.1.7 on 2023-02-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]