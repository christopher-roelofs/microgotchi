import board
import analogio
import math

import os
import busio
import digitalio
import board
import storage
import adafruit_sdcard

class Colors:
    red = 0xff0000
    orange = 0xffa500
    yellow = 0xffff00
    green = 0x008000
    blue = 0x0000FF
    purple = 0x800080
    pink = 0xffc0cb
    white = 0xFFFFFF
    black = 0x000000
    
    
    
def get_battery_level():
    voltage_pin = analogio.AnalogIn(board.A6)
    battery_level = (((voltage_pin.value * 3.3) / 65536 * 2)/4)* 100
    voltage_pin.deinit()
    return math.ceil(battery_level)

def writeFile(filename,data):
    SD_CS = board.SD_CS  # setup for M0 Adalogger; change as needed
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    cs = digitalio.DigitalInOut(SD_CS)
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    try:
        os.remove("/sd/" + filename)
    except Exception as e:
        print('Unable to delete previous save: {}'.format(e))

    with open("/sd/" + filename, "w+") as f:
        f.write(data)
    storage.umount("/sd")
    spi.deinit()
    cs.deinit()
    
def readFile(filename):
    data = ''
    SD_CS = board.SD_CS  # setup for M0 Adalogger; change as needed
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    cs = digitalio.DigitalInOut(SD_CS)
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    with open("/sd/" + filename, "r") as f:
        data = f.read()
    storage.umount("/sd")
    spi.deinit()
    cs.deinit()
    return data






colors = Colors()
