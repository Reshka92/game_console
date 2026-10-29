from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import ili9341

from Joy import Joy

controller = Joy(5,6,13)

serial = spi(port=0,device = 0, gpio_DC=24, gpio_RST=25)
device = ili9341(serial)
withX = device.width // 2
withY = device.height // 2

list_games = [
    {"name": "Mario", "fill": "yellow"},
    {"name": "Doom", "fill": "white"},
]
try:
    while True:
        with canvas(device) as draw:
            draw.text((withX, withY + 30),"Select the game!", fill="white", anchor = "mm")
            draw.text((withX, withY), f"{list_games[0]['name']}", fill=f"{list_games[0]['fill']}", anchor = "mm")
            draw.text((withX, withY - 40), f"{list_games[1]['name']}", fill=f"{list_games[1]['fill']}", anchor = "mm")

        pressed = controller.return_pressed_button()

        
        if "Нажата кнопка Down" in pressed:
            index_yellow = [i for i, game in enumerate(list_games) if game["fill"] == "yellow"][0]
            if index_yellow < len(list_games) - 1:
                list_games[index_yellow]["fill"] = "white"
                list_games[index_yellow + 1]["fill"] = "yellow"

        if "Нажата кнопка Up" in pressed:
            index_yellow = [i for i, game in enumerate(list_games) if game["fill"] == "yellow"][0]
            if index_yellow > 0:
                list_games[index_yellow]["fill"] = "white"
                list_games[index_yellow - 1]["fill"] = "yellow"

except KeyboardInterrupt:
    print("Выход из программы")
        

input("da")
