# Generated by Django 2.1 on 2019-04-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190425_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DOB',
            field=models.DateField(blank=True, default=None),
        ),
    ]