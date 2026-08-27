class phone:
    def __init__(self,name,color,spec):
        self.name = name
        self.color = color
        self.spec = spec
    def intro(self):
            print("Hi i am a",self.name)
            print("I am colour",self.color)
            print("I have specfication",self.spec)
 #object creation           
samsung = phone('Samsung Galaxy S26 Ultra 5G+', 'Lavender','12gb RAM 1TB Storage')       
samsung.intro()     