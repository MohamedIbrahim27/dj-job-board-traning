# Generated by Django 4.1.1 on 2022-09-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0010_apply_jop'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]