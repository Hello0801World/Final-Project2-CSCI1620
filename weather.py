import requests


class weather:
    def __init__(self,city):
        """
        Constructor to get weather api and to make url
        :param city: city name that is taken from text box
        """
        self.city = city
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        self.API_KEY = 'bb8b1d3002cc41ddddb6dc0a79b906ea'
        self.url = self.BASE_URL + 'appid=' + self.API_KEY + '&q=' + self.city

    def __str__(self):
        """
        Method to return string for user
        :return: weather information of city asked by user
        :return: otherwise return error message
        """
        response = requests.get(self.url).json()

        try:
            temp_kelvin = response['main']['temp']
            temp_fahrenheit = (9/5)*(temp_kelvin-273) +32

            feels_like_kelvin = response['main']['feels_like']
            feels_like_fahrenheit = (9 / 5) * (feels_like_kelvin - 273) + 32

            wind_speed = response['wind']['speed']
            humidity = response['main']['humidity']
            description = response['weather'][0]['description']

            return f'Temperature in {self.city}: {temp_fahrenheit:.2f}°F\n' \
                   f'It feels like {feels_like_fahrenheit:.2f}°F\n' \
                   f'It is {description}\n' \
                   f'Wind speed is {wind_speed}m/s\n' \
                   f'Humidity is {humidity}%'

        except KeyError:
            return f'City not found or there might be typo. Sorry'
