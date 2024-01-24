import requests

api_key = 'd6013cff1b5047d8a41100734242401'
city = 'dar es salaam'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
response = requests.get(url)
data = response.json()

temperature_celsius = data['current']['temp_c']
print(f"The temperature in {city} is {temperature_celsius} Celsius")

