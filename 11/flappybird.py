"""
# Implement flappy bird game here

This program uses object oriented programming to allow the user to play
a game of Flappy Bird according to the real game rules!

Written by Arka Rao
April 19th, 2016
"""

from graphics import *
from random import *
from time import sleep

def main():
    width = int(input("Enter a window width: "))  #ask user to define window size
    height = width
    center = Point(width/2,height/2)
    w = GraphWin("FlappyBird",width,height)
    w.setBackground("light blue")

    pipe = Pipe(w)

    dx = width*0.01

    size = 0.05*width
    bird = Bird(w,size)

    dy = 0.05*height
    g = 0

    score = 0
    pText = Point(0.10*width,0.05*height)
    scoreText = Text(pText,"Score: " + str(score))
    scoreText.draw(w)
    
    w.getMouse()
    
    while True:
    
        pipeOut = pipe.offScreen()

        #continue generating and moving pipes while updating score
        if pipeOut == True:
            pipe = Pipe(w)
            scoreText.undraw()
            score += 1
            scoreText.setText("Score: " + str(score))
            scoreText.draw(w)
        else:
            pipe.move(-dx)
            sleep(0.05)

        #check if bird is out of bounds    
        birdOut = bird.onScreen()
        
        if birdOut == False:
            break
        else:
            g += 0.001*height
            bird.move(g)
            key = w.checkKey()
            if key != None:
                if key == 'Up':                 
                    bird.move(-dy)
                    g = 0
                
        birdTouching = bird.touching(pipe)
        if birdTouching == True:
            break
                 
    gameOver = Text(center, "Game Over! Your score was: " + str(score))
    gameOver.setSize(15)
    gameOver.setStyle("bold")
    gameOver.setTextColor("Purple")
    gameOver.draw(w)
    
    w.getMouse()

    
class Pipe(object):
    def __init__(self,w):
        X = w.getWidth()
        Y = w.getHeight()

        rectangleY = randrange(0.30*X,0.60*X,0.05*X)
        
        #top rectangle
        topRec = Rectangle(Point((X)-0.1*X,rectangleY),Point(X,0))
        topRec.setFill("green")
        topRec.draw(w)

        #bottom rectangle
        botRec = Rectangle(Point((X)-0.1*X,rectangleY+(0.2*X)),Point(X,Y))
        botRec.setFill("green")
        botRec.draw(w)

        rectangleList = [topRec,botRec]

        self.rectangleList = rectangleList

#moving the pipes
    def move(self,dx):
        self.rectangleList[0].move(dx,0)
        self.rectangleList[1].move(dx,0)

#check if top pipe has moved off screen based on x coordinate, where P2 is endpoint (x,y) and P2X gets that x coordinate. the rest get any specific coordinates needed
    def offScreen(self):
        topRec = self.rectangleList[0]
        P2 = topRec.getP2()
        P2X = P2.getX()

        if P2X <= 0:
            return True
        else:
            return False

    def getLeftX(self):
        topRec = self.rectangleList[0]
        P1 = topRec.getP1()
        P1X = P1.getX()
        return P1X

    def getRightX(self):
        topRec = self.rectangleList[0]
        P1 = topRec.getP2()
        P1X = P1.getX()
        return P1X

    def getTopY(self):
        topRec = self.rectangleList[0]
        P1 = topRec.getP1()
        P1Y = P1.getY()
        return P1Y

    def getBottomY(self):
        botRec = self.rectangleList[1]
        P1 = botRec.getP1()
        P1Y = P1.getY()
        return P1Y

class Bird(object):
    def __init__(self,w,size):
        X = w.getWidth()
        Y = w.getHeight()

        self.winY = Y
        self.size = size
        
        pBirdX = 0.1*X
        pBirdY = 0.45*Y

        birdBody = Circle(Point(pBirdX,pBirdY),size)
        birdBody.setFill("yellow")
        birdBody.draw(w)

        birdEye = Circle(Point((pBirdX+0.10*pBirdX),pBirdY-0.05*pBirdY),size/3)
        birdEye.setFill("white")
        birdEye.draw(w)

        birdPupil = Circle(Point((pBirdX+0.18*pBirdX),pBirdY-0.05*pBirdY),size/6)
        birdPupil.setFill("black")
        birdPupil.draw(w)

        birdBeak = Rectangle(Point(pBirdX,pBirdY),Point((pBirdX+0.50*pBirdX),pBirdY+0.02*pBirdY))
        birdBeak.setFill("orange")
        birdBeak.draw(w)

        birdParts = [birdBody,birdEye,birdPupil,birdBeak]
        self.birdParts = birdParts

    def move(self,dy):
        for part in self.birdParts:
            part.move(0,dy)

    def onScreen(self):
        birdBody = self.birdParts[0]
        P1 = birdBody.getP1()
        P1Y = P1.getY()

        if P1Y <= 0 or P1Y >= self.winY-2*self.size:
            return False
        else:
            return True

    def touching(self,pipe):
        leftX = pipe.getLeftX()
        rightX = pipe.getRightX()
        topY = pipe.getTopY()
        botY = pipe.getBottomY()

        birdBody = self.birdParts[0]
        birdCenter = birdBody.getCenter()
        birdCenterX = birdCenter.getX()
        birdCenterY = birdCenter.getY()

        topBird = birdCenterY - self.size
        botBird = birdCenterY + self.size

        leftBird = birdCenterX - self.size
        rightBird = birdCenterX + self.size

        if rightBird >= leftX and rightBird <= rightX:
            if topBird <= topY:
                return True
            elif botBird >= botY:
                return True
            else:
                return False
        return False
            
            
        
        
main()
