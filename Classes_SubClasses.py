class Vehicle(object):  # no instance of this class should be created

	def __init__(self, year, make, model, color):
		# Initialize the Super Class
		self.year = year
		self.make = make
		self.model = model
		self.color = color.lower()
		self.drive = {
			'2WD': False,
			'4WD': False,
			'AWD': False
		}
		self.fuel = {
			'Gas': False,
			'Diesel': False,
			'Hydrogen': False,
			'Electric': False,
			'Hybrid': False,
		}
		self.transmission = {
			'Manual': False,
			'Automatic': False
		}
		self.vehicleOptions = {
			'Bluetooth': 0,
			'Navigation': 0,
			'Backup Camera': 0,
			'Sunroof': 0,
			'Cruise Control': 0,
			'Premium Audio': 0,
			'Remote Engine Start': 0,
			'Automatic Parking': 0
		}

	def setOptions(self):
		# Set Non-Functional Options
		print("Please set your options. (Y or N)")
		optionChoice = 'N'
		for key, value in self.vehicleOptions.items():
			print(str(key))
			optionChoice = input('Y or N?')
			if optionChoice == 'Y':
				self.vehicleOptions.update({key: 1})
			else:
				self.vehicleOptions.update({key: 0})

	def setTransmission(self):
		# Set the type transmission
		print("Transmission Options:")
		for key, value in self.transmission.items():
			print(str(key))
		transChoice = input("Please make a selection: 1 for Manual or 2 for Automatic")
		try:
			if transChoice == 1:
				self.transmission.update({'Manual': True})
			if transChoice == 2:
				self.transmission.update({'Automatic': True})
		except:
			print("Invalid choice. Transmission will be set to Automatic")
			self.transmission.update({'Automatic': True})

	def setFuel(self):
		# Choose type of fuel
		print("Fuel Options:")
		for key, value in self.fuel.items():
			print(str(key))
		fuelChoice = input("Please make a selection: 1 for Gas, 2 for Diesel, 3 for Hydrogen, 4 for Electric, and 5 for Hybrid.")
		try:
			if fuelChoice == 1:
				self.fuel.update({'Gas': True})
			if fuelChoice == 2:
				self.fuel.update({'Diesel': True})
			if fuelChoice == 3:
				self.fuel.update({'Hydrogen': True})
			if fuelChoice == 4:
				self.fuel.update({'Electric': True})
			if fuelChoice == 5:
				self.fuel.update({'Hybrid': True})
		except:
			print("Invalid Option. Fuel type will be set to Diesel.")
			self.fuel.update({'Diesel': True})

	def setDrive(self):
		# Set the Drive Type
		print("Drive Options:")
		for key, value in self.drive.items():
			print(str(key))
		driveChoice = input("Please make a selection: 1 for 2WD, 2 for 4WD, and 3 for AWD")
		try:
			if driveChoice == 1:
				self.drive.update({'2WD': True})
			if driveChoice == 2:
				self.drive.update({'4WD': True})
			if driveChoice == 3:
				self.drive.update({'AWD': True})
		except:
			print("Invalid option. Drive will be set to AWD")
			self.drive.update({'AWD': True})

	def vehicle_print(self):
		# Prints the common elements of all vehicle
		print('Year: ' + str(self.year))
		print('Make: ' + str(self.make))
		print('Model: ' + str(self.model))
		print('Color: ' + str(self.color))
		for key, value in self.drive.items():
			if value:
				print('Drive: ' + str(key))
		for key, value in self.fuel.items():
			if value:
				print('Fuel: ' + str(key))
		for key, value in self.transmission.items():
			if value:
				print('Transmission: ' + str(key))
		for key, value in self.vehicleOptions.items():
			if value == 1:
				print(str(key))


"""BEGIN PASSENGER CAR SUBCLASS"""


class passengerVehicle(Vehicle):
	# Create Passenger Vehicle Subclass
	def __init__(self, *args):
		self.doors = 4
		self.engineSize = {
			1.5: False,
			2.0: False,
			2.5: False,
			3.0: False,
		}
		Vehicle.__init__(self, *args)

	def vehicle_print(self):
		Vehicle.vehicle_print(self)
		print('Number of Doors: ' + str(self.doors))
		for key, value in self.engineSize.items():
			if value:
				print('Engine Size: ' + str(key) + 'Liters')

	def setDoors(self):
		numDoors = int(input("How many doors? (2-5)"))
		if 2 <= numDoors <= 5:
			self.doors = numDoors
		else:
			print("Invalid Input. Number of doors will be set to 4.")
			self.doors = 4

	def setEngineSize(self):
		print("Engine Size Options:")
		for key, value in self.engineSize.items():
			print(str(key))
		sizeChoice = input("Please type the number of your selection")
		try:
			if sizeChoice == 1.5:
				self.engineSize.update({1.5: True})
			if sizeChoice == 2.0:
				self.engineSize.update({2.0: True})
			if sizeChoice == 2.5:
				self.engineSize.update({2.5: True})
			if sizeChoice == 3.0:
				self.engineSize.update({3.0: True})
		except:
			print("Invalid Input. Engine size will be set at 2.0 Liters")
			self.engineSize.update({2.0: True})


"""END PASSENGER VEHICLE CLASS"""

""" BEGIN TRUCK SUBCLASS"""


class workTruck(Vehicle):
	# Initialize the Truck subclass
	def __init__(self, *args):
		self.cab = {
			'Regular Cab': False,
			'Extended Cab': False,
			'Crew Cab': False
		}
		self.bed = {
			'short': False,
			'standard': False,
			'long': False
		}
		Vehicle.__init__(self, *args)

	def vehicle_print(self):
		Vehicle.vehicle_print(self)
		for key, value in self.cab.items():
			if value:
				print('Cab Style: ' + str(key))
		for key, value in self.bed.items():
			if value:
				print('Bed Style: ' + str(key))

	def setCab(self):
		print("Cab style options:")
		for key, value in self.cab.items():
			print(str(key))
		cabChoice = input("Please choose an option: 1 for Regular Cab, 2 for Extended Cab, and 3 for Crew Cab.")
		try:
			if cabChoice == 1:
				self.cab.update({'Regular Cab': True})
			if cabChoice == 2:
				self.cab.update({'Extended Cab': True})
			if cabChoice == 3:
				self.cab.update({'Crew Cab': True})
		except:
			print("Invalid Input. Cab style will be set to Extended")
			self.cab.update({'Extended Cab': True})

	def setBed(self):
		print("Bed length options:")
		for key, value in self.bed.items():
			print(str(key))
		bedChoice = input("Please choose an option: 1 for short bed, 2 for regular bed, and 3 for long bed.")
		try:
			if bedChoice == 1:
				self.bed.update({'short': True})
			if bedChoice == 2:
				self.bed.update({'standard': True})
			if bedChoice == 3:
				self.bed.update({'long': True})
		except:
			print("Invalid Input. Bed style will be set to standard")
			self.bed.update({'standard': True})


"""END TRUCK SUBCLASS"""


def main():
	vehicle_number = input("How many vehicle you want to make?")
	print("You will make", vehicle_number, "vehicles")
	itr = 1
	while itr <= (int(vehicle_number)):
		vehicleChoice = input("Create car or truck? (C or T)")
		vehicleChoice.upper
		if vehicleChoice == 'C':
			print("This is your", itr, "vehicle")
			print("Let's configure your car.")
			year = input('Year:')
			make = input('Make:')
			model = input('Model:')
			color = input('Color:')
			myCar = passengerVehicle(year, make, model, color)
			myCar.setDoors()
			myCar.setEngineSize()
			myCar.setDrive()
			myCar.setFuel()
			myCar.setTransmission()
			myCar.setOptions()
			myCar.vehicle_print()
			itr = itr + 1
		elif vehicleChoice == 'T':
			print("This is your", itr, "vehicle")
			print("Let's configure your truck:")
			year = input('Year:')
			make = input('Make:')
			model = input('Model:')
			color = input('Color:')
			myTruck = workTruck(year, make, model, color)
			myTruck.setDrive()
			myTruck.setFuel()
			myTruck.setTransmission()
			myTruck.setCab()
			myTruck.setBed()
			myTruck.setOptions()
			myTruck.vehicle_print()
			itr = itr + 1
		else:
			# if itr<0:
			# itr=0
			# else:
			# itr=itr-1
			print("Your vehicle type is wrong, please choose between car or truck only (C or T)")
			print("This is your", itr, "vehicle")


if __name__ == "__main__":
	main()
