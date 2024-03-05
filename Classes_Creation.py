class Restaurant:
	"""A simple way to model a Restaurant"""

	def __init__(self, name, cuisine):
		"""Initialize title and cuisine attributes."""
		"""Runs automatically whenever a new Dog object is created"""
		self.name = name.title()
		self.cuisine = cuisine.title()
		self.number_served = 0

	def update_number_served(self):
		"""Updates the number of people served"""
		self.number_served = int(input("How many people were served?"))
		return self.number_served

	def increment_number_served(self):
		"""increments the number served"""
		self.number_served += int(input("How many additional people were served"))

	def display_restaruant_profile(self):
		"""Displays the current profile for the restaurant instance"""
		print(f"My restaurant's name is {self.name}.")
		print(f"My restaurant serves {self.cuisine} food.")
		print(f"We have served {self.number_served} people.")
