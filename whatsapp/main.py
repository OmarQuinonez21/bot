import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

position1 = pt.locateCenterOnScreen("whatsapp/smiley_paperclip.png", confidence=.5)
x = position1[0]
y = position1[1]


# Gets message
def get_message():
    global x, y
#Copia el mensaje recibido
    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.5)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 27, y - 47, duration=.05)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_message)
#Retorna el mensaje recibido
    return whatsapp_message


# Posts
def post_response(message):
    global x, y
    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.5)
    x = position[0]
    y = position[1]
    # puede que a este punto no funcione por las dimenciones de la pantalla y las coordenadas
    pt.moveTo(x + 27, y - 47, duration=.05)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


post_response(get_message())


