from turtle import *

class Face:
    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.noseSize ='small'
    def setSize(self, radius):
        self.size = radius
    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawOutLine()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()