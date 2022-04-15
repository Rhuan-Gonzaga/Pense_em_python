import turtle
import math

def quadrado(turt,tamanho):
    print(turt)
    for i in range(4):
        turt.fd(tamanho)
        turt.lt(90)
    turtle.mainloop()

def polygon(turt,n,tamanho):
    print(turt)
    angulo = 360/n
    for i in range(n):
        turt.fd(tamanho)
        turt.lt(angulo)
    turtle.mainloop()

def circle(t, r):
    circumference = 2 * math.pi * r
    n= 50
    length = circumference / n
    polygon(t, n, length)


quad = turtle.Turtle()
#quadrado(quad,100)
polygon(quad,7,70)