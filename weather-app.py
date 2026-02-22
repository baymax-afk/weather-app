import requests
import customtkinter as ctk
from tkinter import messagebox

# Keep as requested (hardcoded key)
api_key = "your_API_key_here"  #<===== Update this part 

ctk.set_appearance_mode("System")  # "Light", "Dark", or "System"
ctk.set_default_color_theme("blue")


def weather_emoji(main_weather: str) -> str:
    mapping = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Fog": "🌫️",
        "Haze": "🌫️",
        "Smoke": "🌫️",
    }
    return mapping.get(main_weather, "🌍")


def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Missing city", "Please enter a city name.")
        return

    status_label.configure(text="Fetching latest weather...")
    app.update_idletasks()

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "units": "imperial",
            "APPID": api_key,
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        cod = str(data.get("cod", ""))
        if cod != "200":
            status_label.configure(text="")
            messagebox.showerror("City not found", f"No city found for '{city}'.")
            return

        weather_main = data["weather"][0]["main"]
        weather_desc = data["weather"][0]["description"].title()
        temp = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        country = data["sys"]["country"]
        icon = weather_emoji(weather_main)

        city_label.configure(text=f"{data['name']}, {country}")
        icon_label.configure(text=icon)
        condition_label.configure(text=f"{weather_main} • {weather_desc}")
        temp_label.configure(text=f"{temp}°F")
        details_label.configure(
            text=f"Feels Like: {feels_like}°F   |   Humidity: {humidity}%   |   Wind: {wind} mph"
        )
        status_label.configure(text="Latest weather loaded.")

    except requests.RequestException:
        status_label.configure(text="")
        messagebox.showerror("Network error", "Could not connect to weather service. Try again.")


# App window
app = ctk.CTk()
app.title("Pretty Weather App")
app.geometry("640x420")
app.minsize(580, 580)

# Main container
main_frame = ctk.CTkFrame(app, corner_radius=18)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

title_label = ctk.CTkLabel(
    main_frame,
    text="Weather Dashboard",
    font=ctk.CTkFont(size=30, weight="bold"),
)
title_label.pack(pady=(20, 8))

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Check current weather in any city",
    font=ctk.CTkFont(size=14),
    text_color=("gray30", "gray70"),
)
subtitle_label.pack(pady=(0, 16))

# Search row
search_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
search_frame.pack(padx=20, pady=(0, 12), fill="x")

city_entry = ctk.CTkEntry(
    search_frame,
    placeholder_text="Enter city (e.g., New York)",
    height=40,
    font=ctk.CTkFont(size=14),
)
city_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
city_entry.bind("<Return>", lambda event: get_weather())

search_btn = ctk.CTkButton(
    search_frame,
    text="Get Weather",
    height=40,
    width=130,
    command=get_weather,
    font=ctk.CTkFont(size=14, weight="bold"),
)
search_btn.pack(side="left")

# Weather card
card = ctk.CTkFrame(main_frame, corner_radius=16)
card.pack(fill="both", expand=True, padx=20, pady=14)

city_label = ctk.CTkLabel(card, text="City will appear here", font=ctk.CTkFont(size=22, weight="bold"))
city_label.pack(pady=(22, 6))

icon_label = ctk.CTkLabel(card, text="🌤️", font=ctk.CTkFont(size=56))
icon_label.pack(pady=(4, 0))

condition_label = ctk.CTkLabel(card, text="Condition", font=ctk.CTkFont(size=16))
condition_label.pack(pady=(8, 4))

temp_label = ctk.CTkLabel(card, text="--°F", font=ctk.CTkFont(size=42, weight="bold"))
temp_label.pack(pady=(2, 6))

details_label = ctk.CTkLabel(
    card,
    text="Feels Like: --   |   Humidity: --   |   Wind: --",
    font=ctk.CTkFont(size=13),
    text_color=("gray30", "gray70"),
)
details_label.pack(pady=(0, 18))

status_label = ctk.CTkLabel(main_frame, text="", font=ctk.CTkFont(size=12))
status_label.pack(pady=(0, 8))

app.mainloop()
