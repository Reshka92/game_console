import time
import random
class Snake:
    def __init__(self, width, height):
        self.speed = 1
        self.time = 0.00
        self.record = 0
        # about Snake
        self.positionX = random.randist(0, width)
        self.positionY = random.randist(0, height)

        self.sizeX = 8
        self.sizeY = 8

        self.directions = [top, right, bottom, left]
        self.direction_now = right

    def delete_apple 
    def rutine_moove(self):
        if self.direction_now = right:
            self.positionX += 8
        if self.direction_now = left:
            self.positionX -= 8
        if self.direction_now = top:
            self.positionY += 8
        if self.direction_now = bottom:
            self.positionY -= 8

        if self.possition_apple_x = self.positionX and self.possition_apple_y = self.positionY:
            delete_apple(self)
            generated_apple(self)
            
        

    
   
