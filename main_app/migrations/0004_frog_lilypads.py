# Generated by Django 4.2.16 on 2024-09-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_lilypad_alter_feeding_options_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='frog',
            name='lilypads',
            field=models.ManyToManyField(to='main_app.lilypad'),
        ),
    ]
