class DogMother:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
class Dog(DogMother):
    def __init__(self, name, habitat,breed):
        super().__init__(name,habitat)
        self.breed = breed
class Dog1(DogMother):
    def __init__(self, name, habitat,breed):
        super().__init__(name,habitat)
        self.breed = breed    
d = Dog("Coder","Home","Labrador")
print(d.name)
print(d.breed)    
d1 = Dog1("Coder1","Home1","golden Retrivrer")
print(d1.name)
print(d1.breed)     

        