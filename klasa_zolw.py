import turtle

dave = turtle.Turtle() 
dave.color('red','yellow')
dave.pensize(2)
dave.shape('turtle')
dave.speed(1)
dave.begin_fill()

class T_Kwadrat:
    
    def __init__(self, bok, angle):
        self.bok = bok
        self.angle = angle
        
    def kwadrat(turtle, bok, angle):
        for i in range(4):
            turtle.forward(bok)
            turtle.left(angle)

T_Kwadrat.kwadrat(dave, 50, 90)        
dave.end_fill()
turtle.done()
