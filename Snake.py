import time
import random
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import ili9341
from Joy import Joy
class Snake:
    def __init__(self, device):
        self.speed = 1
        self.time = 0.00
        self.record = 0
        self.device = device
        # about Snake
        self.positionX = random.randint(0, device.width)
        self.positionY = random.randint(0, device.height)

        self.sizeX = 8
        self.sizeY = 8
        controller = Joy(5,6,13)

        self.direction_now = "right"

    def generated_apple(self):
        self.possition_apple_x = random.randint(0, device.width)
        self.possition_apple_y = random.randint(0, device.height)

    def checking_vector(self):
        self.pressed = controller.return_pressed_button()

        if "Нажата кнопка Up" in self.pressed:
            self.direction_now = "up"
        if "Нажата кнопка Down" in self.pressed:
            self.direction_now = "down"
        if "Нажата кнопка Left" in self.pressed:
            self.direction_now = "left"
        if "Нажата кнопка Right" in self.pressed:
            self.direction_now = "right"

    def rutine_moove(self):
        if self.direction_now == "right":
            self.positionX += 8
        if self.direction_now == "left":
            self.positionX -= 8
        if self.direction_now == "top":
            self.positionY += 8
        if self.direction_now == "down":
            self.positionY -= 8

        # if self.possition_apple_x == self.positionX and self.possition_apple_y == self.positionY:
        #     delete_apple(self)
        #     generated_apple(self)
        
    def run(self):
        try:
            while True:
                with canvas(self.device) as draw:
                    # Start
                    self.checking_vector()
                    print(self.direction_now)
                    draw.rectangle((self.positionX, self.positionY, self.positionX + self.sizeX, self.positionY + self.sizeY), fill="green", outline="white")
                    # rutine
                    self.rutine_moove()
                    time.sleep(1)
        
        except KeyboardInterrupt:
            print("END")

            
        

    
   
