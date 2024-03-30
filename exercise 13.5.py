# Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white

class Vehicle:
 
	Color="White"
 
	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

class Bus(Vehicle):
	pass

class Car(Vehicle):
	pass

School_bus=Bus("Volvo",120,23)
print(School_bus.name,School_bus.Color,School_bus.max_speed,School_bus.mileage)

Maruti=Car("Swift",90,41)
print(Maruti.name,Maruti.Color,Maruti.max_speed,Maruti.mileage)