import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_imageload
from time import sleep
from util import colors
import util








class Hud:
    def __init__(self,pet):
        self.pet = pet
        self.display = board.DISPLAY
        self.font = terminalio.FONT
        self.color = colors.black
        self.batter_check_cooldown = 1000
        self.batter_check_timeout = self.batter_check_cooldown

        color_bitmap = displayio.Bitmap(160, 128, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = colors.white  
        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

        self.sprite_sheet, self.palette = adafruit_imageload.load("/avatar-0.bmp",bitmap=displayio.Bitmap,palette=displayio.Palette)
        self.palette.make_transparent(0)

        self.display_group = displayio.Group(max_size=20)

        self.display_group.append(bg_sprite)

        # Battery label
        battery_level = util.get_battery_level()
        battery_text = "Battery: {}".format(battery_level)
        self.battery_text = label.Label(self.font, text=battery_text, color=self.color)
        self.battery_text.x = 85
        self.battery_text.y = 120
        self.display_group.append(self.battery_text)

        # Name label
        name_text = "Name: {}          ".format(self.pet.get_name())
        self.name_label = label.Label(self.font, text=name_text, color=self.color)
        self.name_label.x = 10
        self.name_label.y = 10
        self.display_group.append(self.name_label)
       

        # Age label
        self.age_text = "Age: {}          ".format(self.pet.get_age())
        self.age_label = label.Label(self.font, text=self.age_text, color=self.color)
        self.age_label.x = 10
        self.age_label.y = 25
        self.display_group.append(self.age_label)


        # Health label
        health_text = "Health: {}          ".format(self.pet.health)
        self.health_label = label.Label(self.font, text=health_text, color=self.color)
        self.health_label.x = 10
        self.health_label.y = 40
        self.display_group.append(self.health_label)

        # Happiness Label
        happiness_text = "Happiness: {}          ".format(self.pet.happiness)
        self.happiness_label = label.Label(self.font, text=happiness_text, color=self.color)
        self.happiness_label.x = 10
        self.happiness_label.y = 55
        self.display_group.append(self.happiness_label)

        # Hunger label
        hunger_text = "Hunger: {}          ".format(self.pet.hunger)
        self.hunger_label = label.Label(self.font, text=hunger_text, color=self.color)
        self.hunger_label.x = 10
        self.hunger_label.y = 70
        self.display_group.append(self.hunger_label)

        self.sprite = displayio.TileGrid(self.sprite_sheet, pixel_shader=self.palette,width = 1,height = 1,tile_width = 16,tile_height = 16)
        self.sprite.x = 55
        self.sprite.y = 20
        self.sprite[0] = self.pet.get_avatar()
        self.sprite_group = displayio.Group(scale=2)
        self.sprite_group.append(self.sprite)
        self.display_group.append(self.sprite_group)

    def update(self):

        name_text = "Name: {}".format(self.pet.get_name())
        self.name_label.text = name_text
        
        age_text = "Age: {}".format(self.pet.get_age())
        self.age_label.text = age_text

        hunger_text = "Hunger: {}".format(self.pet.get_hunger())
        self.hunger_label.text = hunger_text

        happiness_text = "Happiness: {}".format(self.pet.get_happiness())
        self.happiness_label.text = happiness_text

        health_text = "Health: {}          ".format(self.pet.get_health())
        self.health_label.text = health_text

        if self.batter_check_timeout < 1:
            battery_level = util.get_battery_level()
            battery_text = "Battery: {}".format(battery_level)
            self.battery_text.text = battery_text
            self.batter_check_timeout = self.batter_check_cooldown
        else:
            self.batter_check_timeout -= 1

        self.sprite[0] = self.pet.get_avatar()




    def draw(self):
        self.update()
        self.display.show(self.display_group)
        
        