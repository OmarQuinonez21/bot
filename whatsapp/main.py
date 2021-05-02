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
    # Copia el mensaje recibido
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
    # Retorna el mensaje recibido
    return whatsapp_message


# Posts
def post_response(message):
    global x, y
    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.5)
    x = position[0]
    y = position[1]
    # puede que a este punto no funcione por las dimenciones de la pantalla y las coordenadas
    # necesita estar en las coordenadas de inicio
    pt.moveTo(x + 27, y - 47, duration=.05)
    pt.click()
    # Aqui comienza a escribir
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n", interval=.01)


# Processes response
def process_response(message):
    random_no = random.randrange(3)
    # Si no hay un ? en el mensaje, se saca un numero al azar y se responde dependiendo de ello
    if "?" in str(message).lower():
        return "Gracias por contactarnos, en un momento su duda será solucionada"
    else:
        if random_no == 0:
            return "hola"
        elif random_no == 1:
            return "Que onda"
        else:
            return "Que rollo"


# Da un enter entre las lineas de whatsapp
def enter_function():
    pt.keyDown('shift')
    pt.press('enter')
    pt.keyUp('shift')


# Check for new messages
def check_for_new_messages():
    pt.moveTo(x + 2, y - 55, duration=.5)

    while True:
        #Continuosly checks for green dots
        try:
            position = pt.locateOnScreen("whatsapp/green_circle.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)
                #este except no esta funcionando.
        except(Exception):
            print("No new messages located")
        if pt.pixelMatchesColor(int(x+2), int(y-55), (255,255,255), tolerance=10):
            print("is white")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("no new messages yet...")
        sleep(5)


check_for_new_messages()
# processed_message = process_response(get_message())
# post_response(processed_message)
