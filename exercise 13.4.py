# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
	def __init__ (self,max_speed,mileage):
		self.max_speed=max_speed
		self.mileage=mileage
 
class Bus(Vehicle):
	pass

School_bus=Bus(70,10)

print(School_bus.max_speed,School_bus.mileage)

# Class Inheritance

class Vehicle:

	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage
 
	def sitting_capacity(self,capacity):
		return f"sitting capacity of bus {self.name} is {capacity} passanger"

class Bus(Vehicle):
	#assign defualt value to capacity 50
	def sitting_capacity(self,capacity=50):
		return super().sitting_capacity(capacity=50)

School_bus=Bus("Volvo",120,23)

School_bus.sitting_capacity()