# Generated by Django 2.2 on 2019-04-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surl',
            fields=[
                ('given_url', models.URLField(max_length=300)),
                ('short_url', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('visit_count', models.IntegerField(default=0)),
                ('creat_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]