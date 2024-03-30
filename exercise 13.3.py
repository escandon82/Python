# How to Modify attributes in class

class Car():
	"""A simple attempt to create a car"""
 	def __init__(self,make,model,year): #__init__: means this will run automatically
 		"""initialize car attribute"""
 		self.make=make
 		self.model=model
 		self.year=year
 
 		#fuel capacity and level in gallons
		self.fuel_capacity=15
		self.fuel_level=0
 
	def fill_tank(self):
		"""fill gas tank to capacity"""
		self.fuel_level=self.fuel_capacity
		print("Fuel tank is full")
 
	def drive(self):
		"""stimulate driving"""
		print("The car is moving")

# let create object of Car class
my_car=Car("Audi","G3",2022)

# calling methods
my_car.drive()

my_car.fill_tank()
