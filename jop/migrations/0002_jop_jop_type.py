# Generated by Django 4.1.1 on 2022-09-10 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='jop_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
