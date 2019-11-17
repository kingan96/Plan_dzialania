#Grafika Turtle

import turtle

#kolor i kształt żółwia Tima

tim = turtle.Turtle()
tim.color('red')
tim.pensize(2)
tim.shape('turtle')

#trasa zółwia Tim'a

tim.forward(100)
tim.left(90)
tim.penup()
tim.forward(100)
tim.right(90)
tim.pendown()
tim.color('orange')
tim.forward(100)
tim.left(90)
tim.penup()
tim.forward(100)
tim.right(90)
tim.pendown()
tim.color('yellow')
tim.forward(100)
tim.right(90)
tim.forward(300)
tim.right(90)
tim.forward(200)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)

#kolor i kształt żółwia Dave'a

dave = turtle.Turtle()
dave.color('navyblue')
dave.pensize(5)

#Trasa żółwia Dave'a

dave.backward(100)
dave.speed(1)
dave.right(90)
dave.penup()
dave.backward(100)
dave.left(90)
dave.pendown()
dave.color('blue')
dave.backward(100)
dave.right(90)
dave.penup()
dave.backward(100)
dave.left(90)
dave.pendown()
dave.color('aqua')
dave.backward(100)
dave.left(90)
dave.backward(300)
dave.left(90)
dave.backward(200)
dave.right(90)
dave.backward(100)
dave.right(90)
dave.backward(100)
dave.left(90)
dave.forward(100)
