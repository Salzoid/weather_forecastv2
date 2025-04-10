import requests
import csv


# Replace with your actual Weatherstack API key
API_KEY = 'use your own api key for this'
BASE_URL = 'http://api.weatherstack.com/current'

# City to fetch weather for

city = input('Where are you at? ')


# Full request URL
params = {
    'access_key': API_KEY,
    'query': city
}

# Make the request
response = requests.get(BASE_URL, params=params)
data = response.json()

# Check for successful response
if 'current' in data:
    temperature = data['current']['temperature']
    description = data['current']['weather_descriptions'][0]
    humidity = data['current']['humidity']
    observation = data['current']['observation_time']
    localtime = data['location']['localtime']
    sunrise = data['current']['astro']['sunrise']
    sunset = data['current']['astro']['sunset']
    print(f"Current weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Observation_time: {observation}")
    print(f"localtime: {localtime}")
    print(f"sunrise: {sunrise}")
    print(f"sunset: {sunset}")
else:
    print("Error fetching data:", data.get("error", "Unknown error"))

# Save to CSV
with open('weather_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['City', 'Temperature (°C)', 'Condition', 'Humidity (%)', 'Observation Time', 'Local Time'])
    writer.writerow([city, temperature, description, humidity, observation, localtime])


