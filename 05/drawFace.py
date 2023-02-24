"""
# drawFace.py
This program asks the user to specify a window size and creates a drawing of
a koala inside it. This koala face will scale according to the window size.

Written by Arka Rao
February 27th, 2016
"""

from graphics import *

def main():
    #ask user for dimensions, create window
    width = int(raw_input("enter width of window: "))
    height = int(raw_input("enter height of window: "))
    w = GraphWin("drawFace",width,height)
    w.setBackground("aquamarine")
    radiusCircle = min(width,height)/2.0

    #establish ear radius, build left ear
    earRadius =  radiusCircle * 0.2
    leftX = width/5
    leftY = height/5
    leftEar = Circle(Point(leftX,leftY),earRadius)
    leftEar.setFill("gray")
    leftEar.draw(w)

    #establish earfill radius, build left ear fill
    smallRadius = earRadius * 0.60 
    fillLeft = Circle(Point(leftX,leftY),smallRadius)
    fillLeft.setFill("light gray")
    fillLeft.draw(w)

    #build right ear
    rightX = 0.80*width
    rightY = height/5
    rightEar = Circle(Point(rightX,rightY),earRadius)
    rightEar.setFill("gray")
    rightEar.draw(w)

    #build right ear fill
    fillRight = Circle(Point(rightX,rightY),smallRadius)
    fillRight.setFill("light gray")
    fillRight.draw(w)
    
    #establish faceradius, build face
    faceRadius = min(width,height)/3.0
    faceCircle = Circle(Point(width/2.0, height/2.0),faceRadius)
    faceCircle.setFill("gray")
    faceCircle.draw(w)

    #establish eyeradius, buile left eye
    eyeRadius = earRadius*0.60
    leftEyeX = leftX + 0.80*leftX
    leftEyeY = leftY + 0.80*leftY
    leftEye = Circle(Point(leftEyeX,leftEyeY),eyeRadius)
    leftEye.setFill("white")
    leftEye.draw(w)
    
    #establish eyeballradius, build left eyeball
    eyeballRadius = smallRadius*0.60
    leftEyefill = Circle(Point(leftEyeX,leftEyeY),eyeballRadius)
    leftEyefill.setFill("black")
    leftEyefill.draw(w)

    #build righteye
    rightEyeX = leftEyeX + 0.80*leftEyeX
    rightEyeY = leftEyeY
    rightEye = Circle(Point(rightEyeX,rightEyeY),eyeRadius)
    rightEye.setFill("white")
    rightEye.draw(w)

    #build right eyeball
    rightEyefill = Circle(Point(rightEyeX,rightEyeY),eyeballRadius)
    rightEyefill.setFill("black")
    rightEyefill.draw(w)

    #build nose using an oval, and use move command to adjust position
    noseX1 = leftEyeX+0.70*leftEyeX
    noseX2 = rightEyeX-0.40*rightEyeX
    noseY1 = 1.5*leftEyeY
    noseY2 = 1.5*noseY1
    nose = Oval(Point(noseX1,noseY1),Point(noseX2,noseY2))
    nose.setFill("black")
    nosemoveY = -1*(0.3*faceRadius)
    nose.move(0,nosemoveY)
    nose.draw(w)
    
    
    w.getMouse()
main()
