# from django.shortcuts import render

# # Create your views here.
# from .forms import AgeCalculatorForm
# from datetime import datetime, timedelta
# import roman

# def zodiac_sign(day, month):
#     zodiacs = [
#         ("Capricorn", 19), ("Aquarius", 18), ("Pisces", 20), ("Aries", 19),
#         ("Taurus", 20), ("Gemini", 20), ("Cancer", 22), ("Leo", 22),
#         ("Virgo", 22), ("Libra", 22), ("Scorpio", 21), ("Sagittarius", 21), ("Capricorn", 31)
#     ]
#     return zodiacs[month - 1][0] if day <= zodiacs[month - 1][1] else zodiacs[month][0]

# def calculate_metrics(request):
#     if request.method == "POST":
#         form = AgeCalculatorForm(request.POST)
#         if form.is_valid():
#             dob = form.cleaned_data['date_of_birth']
#             current_date = form.cleaned_data['current_date']
            
#             # Age calculations
#             delta = current_date - dob
#             years = delta.days // 365
#             months = (delta.days % 365) // 30
#             days = (delta.days % 365) % 30

#             # Zodiac sign
#             zodiac = zodiac_sign(dob.day, dob.month)

#             # Leap year check
#             leap_year = "Yes" if (dob.year % 4 == 0 and (dob.year % 100 != 0 or dob.year % 400 == 0)) else "No"

#             # Interesting facts
#             breaths = delta.days * 21600
#             heartbeats = delta.days * 103680
#             smiles = delta.days * 15.5
#             sleep_hours = delta.days * 8
#             food_consumed = delta.days * 2.2

#             context = {
#                 'years': years, 'months': months, 'days': days,
#                 'age_in_months': years * 12 + months,
#                 'age_in_weeks': delta.days // 7,
#                 'age_in_days': delta.days,
#                 'age_in_hours': delta.days * 24,
#                 'age_in_minutes': delta.days * 1440,
#                 'age_in_seconds': delta.days * 86400,
#                 'next_birthday': (dob.replace(year=current_date.year + 1) - current_date).days,
#                 'roman_dob': f"{roman.toRoman(dob.year)}.{dob.month}.{dob.day}",
#                 'zodiac': zodiac,
#                 'leap_year': leap_year,
#                 'breaths': breaths,
#                 'heartbeats': heartbeats,
#                 'smiles': smiles,
#                 'sleep_hours': sleep_hours,
#                 'food_consumed': food_consumed
#             }
#             return render(request, 'results.html', context)
#     else:
#         form = AgeCalculatorForm()

#     return render(request, 'calculator.html', {'form': form})
from django.shortcuts import render
from .forms import AgeCalculatorForm
from datetime import datetime, timedelta
import roman

# Function to get the day of the week
def day_of_week(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date.weekday()]

def zodiac_sign(day, month):
    zodiacs = [
        ("Capricorn", 19), ("Aquarius", 18), ("Pisces", 20), ("Aries", 19),
        ("Taurus", 20), ("Gemini", 20), ("Cancer", 22), ("Leo", 22),
        ("Virgo", 22), ("Libra", 22), ("Scorpio", 21), ("Sagittarius", 21), ("Capricorn", 31)
    ]
    return zodiacs[month - 1][0] if day <= zodiacs[month - 1][1] else zodiacs[month][0]

def calculate_metrics(request):
    if request.method == "POST":
        form = AgeCalculatorForm(request.POST)
        if form.is_valid():
            dob = form.cleaned_data['date_of_birth']
            current_date = form.cleaned_data['current_date']
            
            # Age calculations
            delta = current_date - dob
            years = delta.days // 365
            months = (delta.days % 365) // 30
            days = (delta.days % 365) % 30

            # Day of the week for DOB and current date
            dob_day = day_of_week(dob)
            current_day = day_of_week(current_date)

            # Zodiac sign
            zodiac = zodiac_sign(dob.day, dob.month)

            # Leap year check
            leap_year = "Yes" if (dob.year % 4 == 0 and (dob.year % 100 != 0 or dob.year % 400 == 0)) else "No"

            # Interesting facts
            breaths = delta.days * 21600
            heartbeats = delta.days * 103680
            smiles = delta.days * 15.5
            sleep_hours = delta.days * 8
            food_consumed = delta.days * 2.2

            context = {
                'years': years, 'months': months, 'days': days,
                'dob_day': dob_day,
                'current_day': current_day,
                'age_in_months': years * 12 + months,
                'age_in_weeks': delta.days // 7,
                'age_in_days': delta.days,
                'age_in_hours': delta.days * 24,
                'age_in_minutes': delta.days * 1440,
                'age_in_seconds': delta.days * 86400,
                'next_birthday': (dob.replace(year=current_date.year + 1) - current_date).days,
                'roman_dob': f"{roman.toRoman(dob.year)}.{dob.month}.{dob.day}",
                'zodiac': zodiac,
                'leap_year': leap_year,
                'breaths': breaths,
                'heartbeats': heartbeats,
                'smiles': smiles,
                'sleep_hours': sleep_hours,
                'food_consumed': food_consumed
            }
            return render(request, 'results.html', context)
    else:
        form = AgeCalculatorForm()

    return render(request, 'calculator.html', {'form': form})
