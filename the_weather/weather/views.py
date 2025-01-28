from datetime import datetime
import requests
from django.shortcuts import render
from collections import defaultdict


def index(request):
    # Default city if none is provided
    location = request.GET.get('city', 'Dallas, US')  # Fetch city from the query parameter; default to Dallas

    # Fetch current weather
    current_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid=ef4c7dfe2ddd0f8af05723c839b3f0c2'

    city_weather = requests.get(current_url).json()

    # Error handling for invalid city
    if city_weather.get('cod') != 200:
        context = {'error': f"City '{location}' not found!"}
        return render(request, 'weather/index.html', context)

    # Current weather data
    weather = {
        'city': location,
        'temperature': round(city_weather['main']['temp'], 1),  # Rounded current temperature
        'temp_max': round(city_weather['main']['temp_max'], 1),  # Rounded max temperature
        'temp_min': round(city_weather['main']['temp_min'], 1),  # Rounded min temperature
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon'],
        'wind': city_weather['wind'].get('gust', 'N/A'),
        'feels_like': round(city_weather['main']['feels_like'], 1),  # Rounded feels-like temperature
        'date': datetime.now().strftime('%Y-%m-%d || %H:%M:%S')  # Current date and time
    }

    # Fetch 5-day forecast
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&units=imperial&appid=ef4c7dfe2ddd0f8af05723c839b3f0c2'

    forecast_data = requests.get(forecast_url).json()

    # Get the current date
    current_date = datetime.now().date()

    # Group data by date (excluding the current day)
    daily_data = defaultdict(list)
    for entry in forecast_data['list']:
        entry_date = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S').date()
        if entry_date != current_date:  # Skip the current day
            daily_data[entry_date].append(entry)

    # Sort the dates and limit to the next 5 days
    sorted_dates = sorted(daily_data.keys())[:5]

    # Calculate daily max and min temperatures for the next 5 days
    forecast = []
    for date in sorted_dates:
        entries = daily_data[date]
        max_temp_entry = max(entries, key=lambda x: x['main']['temp_max'])  # Find max temp entry
        min_temp_entry = min(entries, key=lambda x: x['main']['temp_min'])  # Find min temp entry
        forecast_day = {
            'date': date.strftime('%Y-%m-%d'),  # Format date as string
            'temperature': round(max_temp_entry['main']['temp_max'], 1),  # Rounded max temperature
            'temp_low': round(min_temp_entry['main']['temp_min'], 1),     # Rounded min temperature
            'description': max_temp_entry['weather'][0]['description'],
            'icon': max_temp_entry['weather'][0]['icon'],
            'wind': max_temp_entry['wind'].get('gust', 'N/A')
        }
        forecast.append(forecast_day)

    # Combine weather and forecast into context
    context = {
        'weather': weather,
        'forecast': forecast
    }

    return render(request, 'weather/index.html', context)