import turtle
from turtle import *
import random

turtle.colormode(255)

bw = [
    [29, 255],
    [208, 255],
    [236, 255]
]

rw = [
    [234, 255],
    [6, 255],
    [6, 255]
]

gw = [
    [47, 255],
    [245, 255],
    [108, 255]
]

yw = [
    [249, 255],
    [243, 255],
    [44, 255]
]

class Drawing:
    def __init__(self, ca, path):
        self.kame = turtle.Turtle(),
        self.kameSpeed = 0,
        self.circles = 6,
        self.path = path,
        self.colorArray = ca

    def drawIt(self):
        colorChangeArray = []
        for cv in self.colorArray:
            difference = abs(cv[1] - cv[0])
            colorChangeArray.append(difference)

        gradient = int(360 / self.circles[0])

        r = self.colorArray[0][0]
        g = self.colorArray[1][0]
        b = self.colorArray[2][0]

        self.kame[0].pencolor(r, g, b)

        rInc = int(colorChangeArray[0] / gradient)
        gInc = int(colorChangeArray[1] / gradient)
        bInc = int(colorChangeArray[2] / gradient)

        for i in range(0, 320):
            if i % self.circles[0] is 0:
                self.kame[0].width(abs(int(i/9) - 40))
                self.kame[0].setheading(i + self.path[0])
                self.kame[0].forward(10)
                r += rInc
                g += gInc
                b += bInc
                self.kame[0].pencolor(r, g, b)

raph = Drawing(bw, 0)
mikey = Drawing(rw, 90)
leo = Drawing(yw, 180)
don = Drawing(gw, 270)


def runAll():
    raph.drawIt()
    mikey.drawIt()
    leo.drawIt()
    don.drawIt()

# listens to events
turtle.listen()

turtle.onkey(don.drawIt, 'd')
turtle.onkey(mikey.drawIt, 'm')
turtle.onkey(raph.drawIt, 'r')
turtle.onkey(leo.drawIt, 'l')

turtle.onkey(runAll, 'a')

# prevents progam from closing
turtle.mainloop()
