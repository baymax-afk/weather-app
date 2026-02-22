# Weather-App (OpenWeather + CustomTkinter)

Created a desktop weather app built with Python, `requests`, and `customtkinter`.
It fetches current weather data from the OpenWeather API and displays it in a clean GUI.

## The Features

- Search weather by city name
- Displays:
  - City and country
  - Current condition
  - Temperature (F)
  - Feels like temperature
  - Humidity
  - Wind speed
- Basic error handling for invalid city and network issues

## The Requirements

- Python 3.8+
- OpenWeather API key

## Install Dependencies

```bash
pip install requests customtkinter
```

## IMP: Make sure to Configure your API Key to exceute this script properly

Open `weather-app.py` and update:

```python
api_key = "YOUR_API_KEY_HERE"
```

Get your API key from: <https://openweathermap.org/>
Create an account with you email and you should recieve it in you inbox.

## Run the App

```bash
python weather-app.py
```

Then enter a city name and click **Get Weather**.

## Notes

- Units are currently set to `imperial` (Fahrenheit, mph).
- Data source endpoint:
  - `https://api.openweathermap.org/data/2.5/weather`



<div align="center">

<pre>
   |\___/|
   )     (
   =\   /=
    )===(
   /     \
   |     |
  /       \
  \       /
 _/\_/\_/_
</pre>


</div>
