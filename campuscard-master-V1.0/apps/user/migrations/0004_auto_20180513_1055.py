# Generated by Django 2.0.5 on 2018-05-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180513_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='crate_time',
            new_name='create_time',
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=10, verbose_name='年级'),
        ),
    ]
