print("Hello world!")

import turtle

my_turtle = turtle

for i in range(12):
	my_turtle.forward(100)
	my_turtle.left(90)
	my_turtle.forward(10)
	my_turtle.right(10)
	my_turtle.pencolor("red")
	my_turtle.forward(56)
	my_turtle.left(100)
	my_turtle.forward(5)
	my_turtle.left(30)
	my_turtle.forward(120)
	my_turtle.pencolor("black")

turtle.done()	