# Generated by Django 2.1 on 2019-04-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190424_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DOB',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='FB',
            field=models.URLField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]