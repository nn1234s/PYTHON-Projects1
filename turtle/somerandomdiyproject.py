import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Code1022w's Weird Mandala!")

#Part 2 II
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

#Part3 III
colors = ["orange","green","blue","purple","pink","white","chocolate","lime"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(99)
#Part4 IV    
board.penup()
board.goto(0,-60)
board.setheading(90)
board.color("blue","purple")
board.begin_fill()
for i in range(5):
    board.forward(150)
    board.right(155)
board.end_fill()
# part 5 V
board.penup()
board.goto(0, 0)
board.pendown()
petal_colors = ["green","chocolate","violet","orange","purple"]    
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)],
                petal_colors[(i + 2) % len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(65)
        board.right(99)
    board.end_fill()
    board.right(30)
turtle.done()     