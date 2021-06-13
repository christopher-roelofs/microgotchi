import board
import displayio
import terminalio
from adafruit_display_text import label
from gamepadshift import GamePadShift
import digitalio
from time import sleep
import time
import pet
import hud
import menu
from util import colors
import util
import systemboard
import json
import save

saveDebounce = 0
saveDebounceMax = 428




# prepare for gamepad buttons
pad = GamePadShift(digitalio.DigitalInOut(board.BUTTON_CLOCK),
                   digitalio.DigitalInOut(board.BUTTON_OUT),
                   digitalio.DigitalInOut(board.BUTTON_LATCH))

myPet = pet.Pet()
 
try:
    petData = json.loads(save.get_sate())
    myPet.load_pet_data(petData)
    print('loaded pet data')
except Exception as e:
    print('Failed to load pet data: {}'.format(e))
    save.save_state(json.dumps(myPet.get_pet_data()))

myHud = hud.Hud(myPet)
myMenu = menu.Menu(myPet)
myBoard = systemboard.SytemBoard('pygamer')  

#import wifi_test

while True:
    pressed = pad.get_pressed()
    myPet.tick()
    if pressed == myBoard.select_button and not myMenu.showing:
        myMenu.showing = True

    if pressed == myBoard.start_button and myMenu.showing:
        if myMenu.debounce < myMenu.debounceMax:
            myMenu.debounce += 1
        else:
            myMenu.move()
            myMenu.debounce = 0

    if pressed == myBoard.a_button and myMenu.showing:
        myMenu.select()
    
    if pressed == myBoard.b_button and myMenu.showing:
        myMenu.showing = False
        
    if not myMenu.showing:
        myHud.draw()

    if myMenu.showing:
        myMenu.draw()

    if saveDebounce == saveDebounceMax:
        save.save_state(json.dumps(myPet.get_pet_data()))
        saveDebounce = 0
        print('saving pet data')
    else:
        saveDebounce += 1

    sleep(.1)


    