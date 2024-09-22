# Generated by Django 4.2.16 on 2024-09-22 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('B', 'Breakfast Flies'), ('L', 'Lunch Flies'), ('D', 'Dinner Flies')], default='B', max_length=1)),
                ('frog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.frog')),
            ],
        ),
    ]
