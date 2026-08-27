class fruit:
    taste = 'Sweet'

    def __init__(self,name,color):
        self.name = name
        self.color = color
apple = fruit('Apple','Red')
banana = fruit('Banana','yellow')

print(apple.taste)
print(apple.name, apple.color)
print(banana.name, banana.color)