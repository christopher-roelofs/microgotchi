import board
import displayio
import terminalio
from adafruit_display_text import label
from time import sleep
from util import colors
import util

class Menu:
    def __init__(self,pet):
        self.currentSelection = 0
        self.display = board.DISPLAY
        self.font = terminalio.FONT
        self.color = colors.black
        self.showing = False
        self.debounce = 0
        self.debounceMax  = .05
        self.pet = pet

        self.display_group = displayio.Group(max_size=20)

        color_bitmap = displayio.Bitmap(160, 128, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = colors.white  
        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

        self.display_group.append(bg_sprite)

        # Food label
        food_text = "* Food"
        self.food_label = label.Label(self.font, text=food_text, color=self.color)
        self.food_label.x = 10
        self.food_label.y = 10
        self.display_group.append(self.food_label)

        # Play label
        play_text = "Play  "
        self.play_label = label.Label(self.font, text=play_text, color=self.color)
        self.play_label.x = 10
        self.play_label.y = 25
        self.display_group.append(self.play_label)

        # Bathroom label
        bathroom_text = "Bathroom  "
        self.bathroom_label = label.Label(self.font, text=bathroom_text, color=self.color)
        self.bathroom_label.x = 10
        self.bathroom_label.y = 40
        self.display_group.append(self.bathroom_label)

        # Reset label
        reset_text = "Reset  "
        self.reset_label = label.Label(self.font, text=reset_text, color=self.color)
        self.reset_label.x = 10
        self.reset_label.y = 80
        self.display_group.append(self.reset_label)



    def move(self):
        if self.currentSelection == 0:
            play_text = "* Play"
            self.play_label.text = play_text

            food_text = "Food"
            self.food_label.text = food_text

            self.currentSelection = 1            

        elif self.currentSelection == 1:
            bathroom_text = "* Bathroom"
            self.bathroom_label.text = bathroom_text
            
            play_text = "Play"
            self.play_label.text = play_text

            self.currentSelection = 2

        elif self.currentSelection == 2:
            bathroom_text = "Bathroom"
            self.bathroom_label.text = bathroom_text

            reset_text = "* Reset"
            self.reset_label.text = reset_text

            self.currentSelection = 3

        else:
            reset_text = "Reset  "
            self.reset_label.text = reset_text

            food_text = "* Food"
            self.food_label.text = food_text

            self.currentSelection = 0


    def select(self):

        if self.currentSelection == 0:
            self.pet.update_hunger(-1)
            self.showing = False

        if self.currentSelection == 1:
            self.pet.update_happiness(1)
            self.showing = False

        if self.currentSelection == 2:
            self.pet.update_health(1)
            self.showing = False

        if self.currentSelection == 3:
            self.pet.reset()
            self.showing = False



    def update(self):
        pass

    def draw(self):
        self.showing = True
        self.update()
        self.display.show(self.display_group)