import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, city):
    base_url = "https://api.weatherbit.io/v2.0/current"
    params = {
        'city': city,
        'key': api_key,
        'units': 'M'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['data'][0]['temp']
            description = data['data'][0]['weather']['description']
            result_text.set(f'Temperature in {city}: {temperature}°C, Description: {description}')
        else:
            result_text.set(f'Error: {data["error"]}')
    except Exception as e:
        result_text.set(f'Error: {e}')

def check_weather():
    city = city_entry.get()
    get_weather(api_key, city)


api_key = 'da449304e554433bbb5aa7c66df986ce'

app = tk.Tk()
app.title("Weather Checker")

city_label = tk.Label(app, text="Enter City:")
city_entry = tk.Entry(app)
check_button = tk.Button(app, text="Check Weather", command=check_weather)
result_label = tk.Label(app, text="Result:")
result_text = tk.StringVar()
result_display = tk.Label(app, textvariable=result_text)

city_label.grid(row=0, column=0, pady=10)
city_entry.grid(row=0, column=1, pady=10)
check_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label.grid(row=2, column=0, pady=10)
result_display.grid(row=2, column=1, pady=10)

app.mainloop()
