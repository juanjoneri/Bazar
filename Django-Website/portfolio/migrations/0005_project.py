# Generated by Django 2.0.6 on 2018-06-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20180603_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('link', models.URLField()),
                ('button_icon', models.CharField(max_length=16)),
                ('img', models.CharField(max_length=64)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
