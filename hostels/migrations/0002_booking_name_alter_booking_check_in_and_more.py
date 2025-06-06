# Generated by Django 5.1.4 on 2025-05-26 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hostels", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="name",
            field=models.CharField(default=1, max_length=256, verbose_name="Имя"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="booking",
            name="check_in",
            field=models.DateField(verbose_name="Дата заезда"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="check_out",
            field=models.DateField(verbose_name="Дата выезда"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата брони"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="phone",
            field=models.CharField(max_length=20, verbose_name="Номер телефона"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookings",
                to="hostels.room",
                verbose_name="Комната",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="number",
            field=models.CharField(max_length=10, verbose_name="Номер комнаты"),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.CharField(
                choices=[
                    ("Одноместный", "Одноместный"),
                    ("Двухместный", "Двухместный"),
                    ("Четырёхместный", "Четырёхместный"),
                ],
                max_length=20,
                verbose_name="Тип комнаты",
            ),
        ),
    ]
