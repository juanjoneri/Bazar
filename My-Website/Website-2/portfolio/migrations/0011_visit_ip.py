# Generated by Django 2.0.6 on 2018-06-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20180605_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='ip',
            field=models.CharField(default='0.0.0.0', max_length=32),
            preserve_default=False,
        ),
    ]