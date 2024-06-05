from tkinter import *
from urllib import request
import json

def showWeather():
    city_name = city_entry.get()

    api_key = "eda2b2s6d#sd65f4de7c4b8"  # sample API
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    try:
        response = request.urlopen(weather_url)
        weather_info = json.loads(response.read())

        if weather_info['cod'] == 200:
            temp = int(weather_info['main']['temp'] - 273)
            description = weather_info['weather'][0]['description']
            result_label.config(text=f"The weather in {city_name} is {description} with a temperature of {temp}°C.")
        else:
            result_label.config(text=f"Weather for '{city_name}' not found! Please enter a valid city name.")
    except Exception as e:
        result_label.config(text="An error occurred. Please check your internet connection or try again later.")

root = Tk()
root.geometry("400x200")
root.title("Weather App")

city_label = Label(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = Entry(root)
city_entry.pack(pady=5)

check_button = Button(root, text="Check Weather", command=showWeather)
check_button.pack(pady=5)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
