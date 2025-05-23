# Generated by Django 4.2.7 on 2025-04-20 15:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.UUIDField()),
                ('theater_id', models.UUIDField()),
                ('screen_id', models.UUIDField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'showtimes',
                'ordering': ['start_time'],
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=2)),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('is_available', models.BooleanField(default=True)),
                ('is_reserved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='showtimes.showtime')),
            ],
            options={
                'db_table': 'seats',
                'ordering': ['row', 'number'],
                'unique_together': {('showtime', 'row', 'number')},
            },
        ),
    ]
