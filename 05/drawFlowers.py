"""
# drawFlowers.py
This program creates a window in which the user can draw flowers in a meadow
using a series of mouse clicks. The program takes data from the mouse clicks
and draws the flower between those clicks. Once the user is done, they can click
on the black border of the window and exit the program.

Written by Arka Rao
February 27th, 2016
"""
#step1 - import graphics and random libraries
#step2 - create main program and a window with a sky color background
#step3 - create a function that makes a rectangle half the size of window, green
#step4 - create a function that makes a small border, black
#step5 - create while loop that breaks when user clicks in the black border
#step6 - create a skeleton using a click from the loop passed through makeFlower
#step7 - color the flower bulb and a small circle inside it as well as stem
#step8 - undraw the bulb and redraw it over the stem for aesthetics
#step9 - create the leaves using getCenter() on the stem
#fixed bug that created a flower before quitting instead of quitting immediately
#added text in window to inform user on how to draw flowers

from graphics import *
from random import *

def main():

    width = 500
    height = 500
    w = GraphWin("meadow",width,height)
    w.setBackground("aqua")

    text = "Click twice to draw a flower! Click in the border to quit."
    message = Text(Point(250,50),text)
    message.draw(w)

    grass = makeGrass(w)
    grass.draw(w)
    grass.setFill("light green")
    
    border = makeBorder(w)
    border.draw(w)
    border.setFill("black")

    
    while True:
        click = w.getMouse()
        Y = click.getY()
        borderHeight = (0.95)*height
        if Y > borderHeight:
            break
        makeFlower(w,click)

def makeGrass(w):

    width = w.getWidth()
    height = w.getHeight()
    R1 = Rectangle(Point(0,height/2),Point(width,height))
    return R1

def makeBorder(w):

    width = w.getWidth()
    height = w.getHeight()
    newHeight = height*(.05)
    borderHeight = height - newHeight
    R2 = Rectangle(Point(0,borderHeight),Point(width,height))
    return R2

def makeFlower(w,click):
    
    CX = click.getX()
    CY = click.getY()
    width = 500
    Cradius = width - width*.95
    smallRadius = Cradius*.20
    C1 = Circle(Point(CX,CY),Cradius)
    C2 = Circle(Point(CX,CY),smallRadius)
    randColor1=color_rgb(randrange(256),randrange(256),randrange(256))
    randColor2=color_rgb(randrange(256),randrange(256),randrange(256))
    C1.draw(w)
    C1.setFill(randColor1)
    C2.draw(w)
    C2.setFill(randColor2)
    click2 = w.getMouse()
    LX = click2.getX()
    LY = click2.getY()
    L1 = Line(Point(CX,CY),Point(LX,LY))
    L1.draw(w)
    L1.setOutline("black")
    L1.setWidth(3)
    C1.undraw()
    C2.undraw()
    C1.draw(w)
    C2.draw(w)
    center = L1.getCenter()
    OX = center.getX()
    OY = center.getY()
    OXL = OX-20
    OXR = OX+20
    OYL = OY-20
    OYR = OY-20
    leafL = Oval(Point(OX, OY),Point(OXL,OYL))
    leafL.setFill("green")
    leafL.draw(w)
    leafR = Oval(Point(OX,OY),Point(OXR,OYR))
    leafR.setFill("green")
    leafR.draw(w)
    
main()
