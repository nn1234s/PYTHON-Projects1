from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat
class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)        
        self.breed = breed
d = Dog("Coderr","Home","golden retriver")        
print(d.name)
print(d.breed)
print(d.habitat)