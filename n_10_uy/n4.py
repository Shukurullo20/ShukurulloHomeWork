from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def makeSound(self):
        pass

class Eagle(Bird):
    def fly(self):
        return "Burgut osmonda uchadi"

    def makeSound(self):
        return "Burgut qichqiradi"

class Hawk(Bird):
    def fly(self):
        return "Qaldirg'och havo orqali harakatlanadi"

    def makeSound(self):
        return "Qaldirg'och ovoz chiqaradi"

eagle = Eagle()
hawk = Hawk()

print(eagle.fly())
print(eagle.makeSound())

print(hawk.fly())
print(hawk.makeSound())
