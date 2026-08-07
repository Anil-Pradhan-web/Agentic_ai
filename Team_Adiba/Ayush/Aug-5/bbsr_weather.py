"""
Bhubaneswar Weather Predictor & AI Recommendation System

Requirements:
    - requests (install via `pip install requests`)

Environment Variables:
    - OPENWEATHER_API_KEY: OpenWeatherMap API key (Required)

Usage:
    export OPENWEATHER_API_KEY="your_api_key_here"  # On Linux/macOS
    set OPENWEATHER_API_KEY="your_api_key_here"     # On Windows CMD
    $env:OPENWEATHER_API_KEY="your_api_key_here"    # On PowerShell
    python bbsr_weather.py
"""

import os
import sys
from typing import Dict, Any, Optional
import requests


def get_api_key() -> str:
    """
    Retrieve the OpenWeather API key from environment variables.

    Returns:
        str: API key string if found.

    Raises:
        ValueError: If OPENWEATHER_API_KEY is not set.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError(
            "API Key missing! Please set the 'OPENWEATHER_API_KEY' environment variable.\n"
            "Example (PowerShell): $env:OPENWEATHER_API_KEY='your_api_key_here'\n"
            "Example (Bash/macOS): export OPENWEATHER_API_KEY='your_api_key_here'"
        )
    return api_key


def fetch_weather_data(city: str, api_key: str) -> Optional[Dict[str, Any]]:
    """
    Fetch current weather data for a given city from OpenWeather API.

    Args:
        city (str): Name of the city to query.
        api_key (str): OpenWeather API key.

    Returns:
        Optional[Dict[str, Any]]: Weather API JSON response or None if request fails.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Temperature in Celsius, Wind speed in m/s
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        status_code = response.status_code if response else "Unknown"
        if status_code == 401:
            print("[ERROR] Invalid API Key provided. Please check OPENWEATHER_API_KEY.")
        elif status_code == 404:
            print(f"[ERROR] City '{city}' not found.")
        else:
            print(f"[ERROR] HTTP Error occurred ({status_code}): {http_err}")
    except requests.exceptions.ConnectionError:
        print("[ERROR] Network connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out. OpenWeather API did not respond in time.")
    except requests.exceptions.RequestException as err:
        print(f"[ERROR] An unexpected error occurred while fetching weather data: {err}")

    return None


def generate_ai_recommendation(temp: float, humidity: int, wind_speed: float, description: str) -> str:
    """
    Generate an AI-style context-aware recommendation based on weather metrics.

    Args:
        temp (float): Temperature in Celsius.
        humidity (int): Humidity percentage.
        wind_speed (float): Wind speed in m/s.
        description (str): Weather description text.

    Returns:
        str: AI-style recommendation text.
    """
    desc_lower = description.lower()
    recommendations = []

    # Rain / Precipitation check
    if any(keyword in desc_lower for keyword in ["rain", "drizzle", "thunderstorm", "squall"]):
        recommendations.append("🌧️ Rain expected: Carry an umbrella or a raincoat when stepping out.")

    # Extreme Heat / High Humidity check
    if temp >= 33.0:
        recommendations.append("🔥 High temperature: Stay hydrated, stay indoors during peak hours, and wear lightweight clothes.")
    elif temp >= 28.0 and humidity >= 70:
        recommendations.append("💧 Warm & Humid: Keep a water bottle handy and stay hydrated.")

    # High Wind check
    if wind_speed >= 10.0:
        recommendations.append("💨 Strong winds: Secure loose outdoor items and take care while driving.")

    # Cold weather check
    if temp <= 18.0:
        recommendations.append("🧥 Cool weather: Consider wearing a light sweater or jacket.")

    # Pleasant outdoor weather check
    if not recommendations and 20.0 <= temp <= 30.0 and humidity < 75:
        recommendations.append("✨ Excellent weather: Great conditions for outdoor activities and walks!")

    # Default safety fall-through
    if not recommendations:
        recommendations.append("👍 Weather is manageable. Have a great day and stay safe!")

    return "\n".join(recommendations)


def display_weather_report(city: str, data: Dict[str, Any]) -> None:
    """
    Format and display the weather report along with AI recommendations.

    Args:
        city (str): Name of the city.
        data (Dict[str, Any]): OpenWeather API response dict.
    """
    try:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].title()
        country = data.get("sys", {}).get("country", "")

        recommendation = generate_ai_recommendation(temp, humidity, wind_speed, description)

        print("\n" + "=" * 55)
        print(f"       WEATHER REPORT: {city.upper()}, {country}")
        print("=" * 55)
        print(f" 🌡️  Temperature        : {temp:.1f}°C (Feels like {feels_like:.1f}°C)")
        print(f" 💧 Humidity           : {humidity}%")
        print(f" 💨 Wind Speed         : {wind_speed} m/s")
        print(f" 🌤️  Condition          : {description}")
        print("-" * 55)
        print(" 🤖 AI Recommendation:")
        for line in recommendation.split("\n"):
            print(f"    • {line}")
        print("=" * 55 + "\n")

    except KeyError as key_err:
        print(f"[ERROR] Failed to parse weather data. Missing key: {key_err}")


def main():
    """Main execution flow for Bhubaneswar weather prediction."""
    city = "Bhubaneswar"
    print(f"\n[INFO] Fetching weather forecast for {city}...")

    try:
        api_key = get_api_key()
    except ValueError as err:
        print(f"\n{err}\n")
        sys.exit(1)

    weather_data = fetch_weather_data(city, api_key)
    if weather_data:
        display_weather_report(city, weather_data)
    else:
        print(f"[FAILED] Could not retrieve weather report for {city}.")


if __name__ == "__main__":
    main()
