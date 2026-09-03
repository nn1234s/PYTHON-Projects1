class DogMother:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
class Dog(DogMother):
    def __init__(self, name, habitat,breed):
        DogMother.__init__(self,name,habitat)
        self.breed = breed
d = Dog("Coder","Home","Labrador")
print(d.name)
print(d.breed)        

        