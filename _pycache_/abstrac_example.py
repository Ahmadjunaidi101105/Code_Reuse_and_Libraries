from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
        
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")
        
def create_vehicle(vehicle_type):
    if vehicle_type == "car":
        return Car()
    elif vehicle_type == "motorcycle":
        return Motorcycle()
    else:
        raise ValueError("Unknown vehicle type")
    
car = create_vehicle("car")
car.start_engine()  # Output: Car engine started
motorcycle = create_vehicle("motorcycle")           
motorcycle.start_engine()  # Output: Motorcycle engine started

    