# Generated by Django 3.1.3 on 2020-12-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_auto_20201229_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cr_c',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='determination',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='header_percent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='leadership',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='tackle_ratio',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='teamwork',
            field=models.IntegerField(default=0),
        ),
    ]