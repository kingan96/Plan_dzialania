import turtle

class Tim(turtle):
    def __init__(self, position, angle):
         self.color('red')
         self.pensize(2)
         self.shape('turtle')
         self.setangle(angle)
         self.setposition(position)
         self.showturtle()
         self.penup()
         self.pendown() 

def kwadrat(bok):
    for i in range(4):
        turtle.forward(bok)
        turtle.left(90)

turtle.done()
