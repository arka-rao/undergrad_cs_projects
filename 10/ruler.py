"""
# Solve the ruler problem here
This program takes user input for the width of a graphics window
and creates a window displaying a "ruler" drawn via a recursive
function that repeatedly calls a line drawing function.

Written by Arka Rao
April 13,2016
"""

from graphics import *
import exceptions

def main():
    while True:
        try:
            width = int(raw_input("Enter the width of the window: "))
            if width < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please enter a valid, nonzero integer")
            
    height = width/2
    center = Point(width/2,height/2)
    size = height
    w = GraphWin("Ruler",width,height)
    w.setBackground("light grey")
    recursiveRuler(center,size,w)
    w.getMouse()

def drawRuler(center,size,w):
    """
    This function takes a point, a line size, and a graphics window,
    and draws a line.
    """
    X = center.getX()
    line = Line(center,Point(X,w.getHeight()))
    line.setFill("black")
    line.draw(w)

def recursiveRuler(center,size,w):
    """
    This function takes an initial center point, the size of the
    middle ruler line, and the graphics window. It then uses
    recursion to draw lines, mimicking a ruler. It scales the
    size and positions of the lines accordingly, and returns (stops)
    once the size has been decreased to a certain point.
    """
    if size<5:
        return
    else:
        size = size/2
        
        drawRuler(center,size,w)
        
        pt = center.clone()
        ptY = size*0.5
        pt.move(size,ptY)
        recursiveRuler(pt,size,w)
        
        pt2 = center.clone()
        pt2Y = size*0.5
        pt2.move(-1*size,pt2Y)
        recursiveRuler(pt2,size,w)
        
        
    
main()
