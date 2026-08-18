import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Code1022w's Neon Mandala!")

#Part 2 II
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

#Part3 III
colors = ["red","blue","green","cyan","violet","white","orange","lime"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)
#Part4 IV    
board.penup()
board.goto(0,-60)
board.setheading(90)
board.color("gold","yellow")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()
# part 5 V
board.penup()
board.goto(0, 0)
board.pendown()
petal_colors = ["cyan","lime","violet","orange","deeppink"]    
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)],
                petal_colors[(i + 2) % len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)
turtle.done()     