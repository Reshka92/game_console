import time
import random
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import ili9341
class Snake:
    def __init__(self, width, height, device):
        self.speed = 1
        self.time = 0.00
        self.record = 0
        # about Snake
        self.positionX = random.randint(0, width)
        self.positionY = random.randint(0, height)

        self.sizeX = 8
        self.sizeY = 8

        self.directions = [top, right, bottom, left]
        self.direction_now = "right"

    def generated_apple(self):
        self.possition_apple_x = random.randint(0, width)
        self.possition_apple_y = random.randint(0, height)
        
    def rutine_moove(self):
        if self.direction_now == right:
            self.positionX += 8
        if self.direction_now == left:
            self.positionX -= 8
        if self.direction_now == top:
            self.positionY += 8
        if self.direction_now == bottom:
            self.positionY -= 8

        # if self.possition_apple_x == self.positionX and self.possition_apple_y == self.positionY:
        #     delete_apple(self)
        #     generated_apple(self)
        
    def run(self):
        try:
            while True:
                with canvas(self.device) as draw:
                    # Start
                    self.draw.rectangle((self.positionX, self.positionY, self.positionX + self.sizeX, self.positionY + self.sizeY), fill="green", outline="white")
                    # rutine
                    rutine_moove()
                    time.sleep(1)
        
        except KeyboardInterrupt:
            print("END")

            
        

    
   
