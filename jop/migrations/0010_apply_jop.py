# Generated by Django 4.1.1 on 2022-09-13 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0009_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='jop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply_jop', to='jop.jop'),
            preserve_default=False,
        ),
    ]
