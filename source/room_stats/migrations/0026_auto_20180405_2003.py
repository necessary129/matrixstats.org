# Generated by Django 2.0.1 on 2018-04-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_stats', '0025_auto_20180405_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='status',
            field=models.CharField(choices=[('a', 'assumed'), ('c', 'confirmed'), ('n', 'not_exist'), ('p', 'captcha_required'), ('r', 'registered'), ('u', 'unknown')], default='a', max_length=1),
        ),
    ]
