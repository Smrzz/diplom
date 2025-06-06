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
        """
        Проверяет, доступна ли комната на указанные даты
        """
        # Проверяем все брони для этой комнаты
        overlapping_bookings = Booking.objects.filter(
            room=self,
            check_in__lt=check_out,  # Дата заезда существующей брони раньше даты выезда новой
            check_out__gt=check_in   # Дата выезда существующей брони позже даты заезда новой
        )
        return not overlapping_bookings.exists()

    @classmethod
    def get_available_room(cls, room_type, check_in, check_out):
        """
        Находит первую доступную комнату указанного типа на указанные даты
        """
        rooms = cls.objects.filter(room_type=room_type)
        for room in rooms:
            if room.is_available(check_in, check_out):
                return room
        return None
    
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


