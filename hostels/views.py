import json

from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Room, Booking
from datetime import date, timedelta
from django.core.serializers.json import DjangoJSONEncoder

def hostels(request):
    form = BookingForm()

    # Собираем занятые даты по типам и номерам
    bookings = Booking.objects.all()
    print(f"Всего броней: {bookings.count()}")
    
    # Инициализируем словарь для всех типов комнат
    unavailable_by_type = {
        'Одноместный': {},
        'Двухместный': {},
        'Четырёхместный': {},
    }

    # Сначала добавляем все существующие комнаты
    rooms = Room.objects.all()
    for room in rooms:
        if room.room_type not in unavailable_by_type:
            unavailable_by_type[room.room_type] = {}
        unavailable_by_type[room.room_type][str(room.number)] = []

    # Затем добавляем брони
    for booking in bookings:
        room_type = booking.room.room_type
        room_number = str(booking.room.number)
        print(f"Обрабатываем бронь: {room_type} №{room_number} с {booking.check_in} по {booking.check_out}")
        
        if room_type in unavailable_by_type and room_number in unavailable_by_type[room_type]:
            unavailable_by_type[room_type][room_number].append({
                'start': booking.check_in.strftime('%Y-%m-%d'),
                'end': booking.check_out.strftime('%Y-%m-%d')
            })

    # Преобразуем в формат пригодный для JavaScript
    json_unavailable = {
        k: {num: periods for num, periods in v.items()}
        for k, v in unavailable_by_type.items()
    }
    
    print("Сформированные данные о занятых датах:", json_unavailable)

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
            name = form.cleaned_data['name']

            print(f"Попытка бронирования: {room_type} с {check_in} по {check_out}")

            # Найти свободную комнату нужного типа
            available_room = Room.get_available_room(room_type, check_in, check_out)
            
            if available_room:
                print(f"Найдена свободная комната: {available_room}")
                booking = Booking(
                    room=available_room,
                    phone=phone,
                    name=name,
                    check_in=check_in,
                    check_out=check_out
                )
                booking.save()
                print("Бронь успешно создана")
                return redirect('hostels')
            else:
                print("Свободных комнат не найдено")
                form.add_error(None, f'Нет свободных {room_type.lower()} номеров на выбранные даты.')
    else:
        form = BookingForm()
    return render(request, 'hostels/hostels.html', {'form': form, 'today': date.today()})

