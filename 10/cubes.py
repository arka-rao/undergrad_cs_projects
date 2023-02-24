"""
# solve the cubes problem here

This function takes user input for the graphics window size and uses recursion
to draw a 3D cube with mini cube clones at the corners.

Written by Arka Rao
April 12,2016
"""

from math import *
from graphics import *
import exceptions

def main():
    while True:
        try:
            width = int(raw_input("Enter a window width: "))
            height = int(raw_input("Enter a window height: "))
            if width > 0 and height > 0 and width == height:
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter valid, nonzero, symmetrical window parameters")
            
    w = GraphWin("Cubes",width, height)
    w.setBackground("white")
    pt = Point(width/2,height/2)
    size = width/5
    recursiveCubes(pt,size,w)
    w.getMouse()
    
def drawCube(pt,size,w):
    """
    This function takes a center point, a cube size (for one side), and a
    graphics window and draws a cube.
    """
    X = size*cos(radians(-35))
    Y = size*sin(radians(-35))
    
    p1 = pt.clone()
    p1XMove = X
    p1YMove = Y
    p1.move(p1XMove,p1YMove)
    
    p2 = pt.clone()
    p2XMove = 0
    p2YMove = 2*(Y)
    p2.move(p2XMove,p2YMove)

    p3 = pt.clone()
    p3XMove = (-1) * (X)
    p3YMove = Y
    p3.move(p3XMove,p3YMove)

    p4 = pt.clone()
    p4XMove = (-1) * (X)
    p4YMove = (-1) * Y
    p4.move(p4XMove,p4YMove)

    p5 = pt.clone()
    p5XMove = 0
    p5YMove = (-2) * Y
    p5.move(p5XMove,p5YMove)

    p6 = pt.clone()
    p6XMove = X
    p6YMove = (-1) * (Y)
    p6.move(p6XMove,p6YMove)

    #top polygon
    topPolygon = Polygon([pt,p1,p2,p3])
    topPolygon.setFill("light grey")
    topPolygon.draw(w)

    #right polygon
    rightPolygon = Polygon([pt,p5,p6,p1])
    rightPolygon.setFill("grey")
    rightPolygon.draw(w)

    #left polygon
    leftPolygon = Polygon([pt,p3,p4,p5])
    leftPolygon.setFill("black")
    leftPolygon.draw(w)

def recursiveCubes(pt,size,w):
    """
    This function takes a point, a defined size,and a graphics window, and
    uses recursion to draw the cube as well as several smaller cubes after,
    scaled accordingly.
    """
    X = size*cos(radians(-35))
    Y = size*sin(radians(-35))
    
    if size < 5:
        return
    else:
        drawCube(pt,size,w)
        pt2 = pt.clone()
        pt2.move(-2*X,2*Y)
        recursiveCubes(pt2,size/2,w)
        pt3 = pt.clone()
        pt3.move(2*X,2*Y)
        recursiveCubes(pt3,size/2,w)
        pt4 = pt.clone()
        pt4.move(-2*X,-2*Y)
        recursiveCubes(pt4,size/2,w)
        pt5 = pt.clone()
        pt5.move(2*X,-2*Y)
        recursiveCubes(pt5,size/2,w)
        
    
main()
