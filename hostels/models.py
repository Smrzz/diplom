from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('Одноместный', 'Одноместный'),
        ('Двухместный', 'Двухместный'),
        ('Четырёхместный', 'Четырёхместный'),
    ]
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, verbose_name='Тип комнаты')
    number = models.CharField(max_length=10, verbose_name='Номер комнаты')
    
    def __str__(self):
        return f"{self.room_type} №{self.number}"

    def is_available(self, check_in, check_out):
        return not self.bookings.filter(
            check_in__lt=check_out,
            check_out__gt=check_in
        ).exists()
    
    class Meta:
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'


class Booking(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='bookings', verbose_name='Комната')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    check_in = models.DateField(verbose_name='Дата заезда')
    check_out = models.DateField(verbose_name='Дата выезда')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата брони')

    def __str__(self):
        return f"{self.room} с {self.check_in} по {self.check_out} ({self.phone})"
    
    class Meta:
        verbose_name = 'бронь'
        verbose_name_plural = 'брони'


