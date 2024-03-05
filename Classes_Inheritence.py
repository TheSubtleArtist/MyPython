class User:
	"""A simple way to model a user"""

	def __init__(self, first_name, last_name, age, city, nickname, title):
		"""Initialize attributes."""
		"""Runs automatically whenever a new user object is created"""
		self.fname = first_name.title()
		self.lname = last_name.title()
		self.nname = nickname.title()
		self.title = title.title()
		self.age = age
		self.city = city.title()

	def describe_user(self):
		"""Display user attributes"""
		print(f"\n Name: {self.lname}, {self.fname}")
		print(f"\tPreferred Nickname: {self.nname}")
		print(f"\tAge: {self.age}")
		print(f"\tJob Title: {self.title}")
		print(f"\tWork Site: {self.city}")

	def greet_user(self):
		print(f"\n Hello, {self.fname} {self.lname}, welcome to the office.")


class Admin(User):

	def __init__(self, first_name, last_name, age, city, nickname, title):
		"""Initialize superclass"""
		super().__init__(first_name, last_name, age, city, nickname, title)
		self.privis = Privileges()


class Privileges:

	def __init__(self, privis=['add user', 'delete user', 'change user', 'lock thread']):
		self.privileges = privis

	def show_admin_privileges(self):
		print("\tThis user can:")
		for each in self.privileges:
			print(f"\t{each}")
