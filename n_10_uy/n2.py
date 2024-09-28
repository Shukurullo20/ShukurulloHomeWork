from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class tiger(Animal):
    def sleep(self):
        return "Tiger uhlayapti"
    def eat(self):
        return "Tiger ovqatlanyapti"

class deer(Animal):
    def sleep(self):
        return "Deer uhlayapti"
    def eat(self):
        return "Deer Ovqatlanyapti"

class lion(Animal):
    def sleep(self):
        return "Lion uhlayapti"
    def eat(self):
        return "Lion ovqatlanyapti"


tiger = tiger()
deer = deer()
lion = lion()

print(tiger.sleep())
print(tiger.eat())

print(deer.sleep())
print(deer.eat())

print(lion.sleep())
print(lion.eat())