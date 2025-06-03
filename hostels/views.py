import json

from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Room, Booking
from datetime import date, timedelta
from django.core.serializers.json import DjangoJSONEncoder

def hostels(request):
    form = BookingForm()

    # Собираем занятые даты по типам
    bookings = Booking.objects.all()
    unavailable_by_type = {
        'Одноместный': set(),
        'Двухместный': set(),
        'Четырёхместный': set(),
    }

    for booking in bookings:
        current = booking.check_in
        while current < booking.check_out:
            unavailable_by_type[booking.room.room_type].add(current)
            current += timedelta(days=1)

    # Преобразуем в формат пригодный для JavaScript
    json_unavailable = {
        k: [d.strftime('%Y-%m-%d') for d in sorted(v)]
        for k, v in unavailable_by_type.items()
    }

    context = {
        'form': form,
        'unavailable_json': json.dumps(json_unavailable, cls=DjangoJSONEncoder),
        'today': date.today()
    }
    return render(request, 'hostels/hostels.html', context)

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            room_type = form.cleaned_data['room_type']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            phone = form.cleaned_data['phone']

            # Найти комнату нужного типа без пересекающихся броней
            available_room = Room.objects.filter(room_type=room_type).exclude(
                bookings__check_in__lt=check_out,
                bookings__check_out__gt=check_in
            ).first()

            if available_room:
                booking = Booking(
                    room=available_room,
                    phone=phone,
                    check_in=check_in,
                    check_out=check_out
                )
                booking.save()
                return redirect('hostels')
            else:
                form.add_error(None, f'Нет свободных {room_type.lower()} номеров на выбранные даты.')
    else:
        form = BookingForm()
    return render(request, 'hostels/hostels.html', {'form': form, 'today': date.today()})

