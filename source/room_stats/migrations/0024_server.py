# Generated by Django 2.0.1 on 2018-04-05 17:39

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_stats', '0023_delete_serverstats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255)),
                ('port', models.IntegerField(default=80)),
                ('login', models.CharField(blank=True, max_length=127, null=True)),
                ('password', models.CharField(blank=True, max_length=127, null=True)),
                ('status', models.CharField(choices=[('a', 'assumed'), ('c', 'confirmed'), ('p', 'captcha_required'), ('r', 'registered'), ('u', 'unknown')], default='a', max_length=1)),
                ('last_response_data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('last_response_code', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
