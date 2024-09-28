from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def StartEngine(self):
        pass
    
    @abstractmethod
    def StopEngine(self):
        pass

class Car(Vehicle):
    def StartEngine(self):
        return "Dvigatelni ishga tushurish uchun StartEngine()"
    def StopEngine(self):
        return "Dvigatelni to'xtatish uchun StopEngine()"

class Motorcycle(Vehicle):
    def StartEngine(self):
        return "Dvigatelni ishga tushurish uchun StartEngine()"
    def StopEngine(self):
        return "Dvigatelni to'xtatish uchun StopEngine()"
    
Car = Car()
Motorcycle = Motorcycle()

print(Car.StartEngine())
print(Car.StopEngine())

print(Motorcycle.StartEngine())
print(Motorcycle.StopEngine())