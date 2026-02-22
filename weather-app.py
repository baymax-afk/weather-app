import json
import requests as rq

api_key = "8ee9b548f1019e20292bf6ca99f8aa9d"

def get_weather(city):
    weather_data = rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=SI&APPID={api_key}")
    
    # Pretty print with 2-space indentation
    #print(json.dumps(weather_data.json(), indent=2))

    if weather_data.json()['cod'] == '404':
        print("No City Found")

    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        print(f"The weather in {city} is: {weather}")
        print(f"The temperature in {city} is: {temp}ºF")

if __name__ == "__main__":
    city = input("Enter a city:")
    city = 'London'
    get_weather(city)


