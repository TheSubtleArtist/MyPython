"""
For your class project we will be creating an application to interacts with a webservice in order to obtain data.
Your program will use all of the information you’ve learned in the class in order to create a useful application.
Your program must prompt the user for their city or zip code and request weather forecast data from openweathermap.org.
Your program must display the weather information in an READABLE format to the user.
Requirements:

    Create a Python Application which asks the user for their zip code or city.
    Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
    Display the weather forecast in a readable format to the user.
    Use comments within the application where appropriate in order to document what the program is doing.
    Use functions including a main function.
    Allow the user to run the program multiple times.
    Validate whether the user entered valid data.  If valid data isn’t presented notify the user.
    Use the Requests library in order to request data from the webservice.
    Use Python 3.
    Use try blocks when establishing connections to the webservice.  You must print a message indicating whether or not the connection was successful.

Deliverables (More detail on these deliverables in provided in the course):

    Pseudocode (Due week 4)
    Flowchart (Due week 4)
    Draft Program in a .py file (Due week 9)
    Final Program in a .py file (Due week 12)
"""
import datetime
import json

import requests
from requests.exceptions import HTTPError

import API_Sensitive as sensitiveData

api_url = 'https://api.openweathermap.org/data/2.5/weather?q='
country = 'us'
units = 'imperial'


def print_nested_dict(dict_obj, indent=1):
	# Pretty Print nested dictionary with given indent level
	# Iterate over all key-value pairs of dictionary
	for key, value in dict_obj.items():
		# If value is dict type, then print nested dict
		if isinstance(value, dict):
			print(' ' * indent, key, ':', '{')
			print_nested_dict(value, indent + 4)
		else:
			print(' ' * indent, key, ':', value)


def windDirection(degrees):
	dirs = ['North', 'NNE', 'NE', 'ENE', 'East', 'ESE', 'SE', 'SSE', 'South', 'SSW', 'SW', 'WSW', 'West', 'WNW', 'NW', 'NNW']
	ix = round(degrees / (360. / len(dirs)))
	return dirs[ix % len(dirs)]


def convertTime(time):
	rightMeow = datetime.datetime.fromtimestamp(time)
	return rightMeow.strftime('%X')

if __name__ == '__main__':
	flag = True

	while flag == True:
		# Get user input
		location = str(input("Please enter the location to query"))

		# Get Data
		try:
			response = (requests.get(f'{api_url}{location},{country}&units={units}&appid={sensitiveData.getApiKey()}'))
			jsonResponse = response.json()
			print(f"\nSuccessful Connection!\n")
		except HTTPError as http_err:
			print(f'HTTP error occurred: {http_err}')
		except Exception as err:
			print(f'Other error occurred:{err}')

		# print_nested_dict(jsonResponse, 4)

		# Output data to a file, mostly for development purposes
		with open('API_Weather.txt', 'w') as send:
			send.write(json.dumps(jsonResponse, indent=4))

		# retrieve information from the file and output in a human friendly format
		with open('AssignmentWeek12_Weather.txt', 'r') as retrieve:
			weatherData = json.load(retrieve)
			windy = windDirection(weatherData['wind']['deg'])
			print(f"Current weather for the city of {weatherData['name']} at {convertTime(weatherData['dt'])}:")
			print(f"Sunrise: {convertTime(weatherData['sys']['sunrise'])} ")
			print(f"Sunset: {convertTime(weatherData['sys']['sunset'])} ")
			print(f"Current Temperature is: {weatherData['main']['temp']} degrees")
			print(f"With wind chill: {weatherData['main']['feels_like']}.")
			print(f"Today's highest temperature: {weatherData['main']['temp_max']} degrees.")
			print(f"Today's lowest temperature: {weatherData['main']['temp_min']} degrees.")
			print(f"Humidity is currently at: {weatherData['main']['humidity']}%.")
			print(f"Wind is out of the {windy} at {weatherData['wind']['speed']}mph, but gusting to {weatherData['wind']['gust']}mph.")

		repeat = input("Would you like to try again? \t 'Y' or 'N'")
		repeat = repeat.upper()
		if repeat != 'Y':
			flag = False
			print("Goodbye")
