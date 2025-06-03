from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    ROOM_TYPE_CHOICES = [
        ('Одноместный', 'Одноместный'),
        ('Двухместный', 'Двухместный'),
        ('Четырёхместный', 'Четырёхместный'),
    ]

    room_type = forms.ChoiceField(choices=ROOM_TYPE_CHOICES, label="Тип номера")

    class Meta:
        model = Booking
        fields = ['phone', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        today = date.today()

        if check_in and check_in < today:
            self.add_error('check_in', 'Дата заезда не может быть в прошлом.')
        if check_out and check_out <= check_in:
            self.add_error('check_out', 'Дата выезда должна быть позже даты заезда.')
