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
        self.positionX = random.randrange(int(self.device.width * 25 / 100), int (self.device.width-(self.device.width * 25 / 100)),8)
        self.positionY = random.randrange(int(self.device.height * 25 / 100), int (self.device.height-(self.device.height * 25 / 100)), 8)
        self.lenght = 1
        self.history_snake_posotion = [(self.positionX, self.positionY)]
        # Apple
        self.possition_apple_x = random.randrange(int(self.device.width * 25 / 100), int (self.device.width-(self.device.width * 25 / 100)), 8)
        self.possition_apple_y = random.randrange(int(self.device.height * 25 / 100), int (self.device.height-(self.device.height * 25 / 100)), 8)

        self.last_apple_spawn = time.monotonic()

        self.sizeX = 8
        self.sizeY = 8
        self.controller = Joy(5,6,13)

        self.direction_now = "right"

    def generated_apple(self):
        self.possition_apple_x = random.randrange(int(self.device.width * 25 / 100), int (self.device.width-(self.device.width * 25 / 100)), 8)
        self.possition_apple_y = random.randrange(int(self.device.height * 25 / 100), int (self.device.height-(self.device.height * 25 / 100)), 8)


    def checking_vector(self):
        self.pressed = self.controller.return_pressed_button()
        print(self.pressed)
        if "Нажата кнопка Up" in self.pressed:
            self.direction_now = "up"
        if "Нажата кнопка Down" in self.pressed:
            self.direction_now = "down"
        if "Нажата кнопка Left" in self.pressed:
            self.direction_now = "left"
        if "Нажата кнопка Right" in self.pressed:
            self.direction_now = "right"

    def rutine_moove(self):
        if self.positionX == self.possition_apple_x and self.positionY == self.possition_apple_y:
            self.generated_apple()
            self.lenght += 1
        if self.direction_now == "right":
            self.positionX += 8
        if self.direction_now == "left":
            self.positionX -= 8
        if self.direction_now == "down":
            self.positionY += 8
        if self.direction_now == "up":
            self.positionY -= 8

        # if self.possition_apple_x == self.positionX and self.possition_apple_y == self.positionY:
        #     delete_apple(self)
        #     generated_apple(self)
        
    def run(self):
        try:
            while True:
                with canvas(self.device) as draw:
                    # Start
                    now = time.monotonic()
                    if now - self.last_apple_spawn >= 5:
                        self.generated_apple()
                        self.last_apple_spawn = now
                    self.checking_vector()
                    print(f"history pos: {self.history_snake_posotion} LENGHT: {self.lenght}")
                    print(f"Позиция змейки:{self.positionX}, {self.positionY} Позиция яблока: {self.possition_apple_x}, {self.positionY}")
                    # SNAKE
                    for i in range(1, self.lenght + 1):
                        x, y = self.history_snake_posotion[-i]
                        draw.rectangle((x, y, x + self.sizeX, y + self.sizeY), fill="green", outline="white")
                    # APPLE
                    draw.rectangle((self.possition_apple_x, self.possition_apple_y, self.possition_apple_x + self.sizeX, self.possition_apple_y + self.sizeY), fill="red", outline="white")
                    self.rutine_moove()
                    self.history_snake_posotion.append((self.positionX, self.positionY))
                    time.sleep(0.25)
        
        except KeyboardInterrupt:
            GPIO.cleanup()
            print("END")

            
        

    
   
