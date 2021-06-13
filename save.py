import board
import analogio
import math

import os
import busio
import digitalio
import board
import storage
import adafruit_sdcard



def save_state(data):
    SD_CS = board.SD_CS  # setup for M0 Adalogger; change as needed
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    cs = digitalio.DigitalInOut(SD_CS)
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    if 'save.json' in os.listdir("/sd/"):
        os.remove("/sd/save.json")
    with open("/sd/" + 'save.json', "w+") as f:
        f.write(data)
    storage.umount("/sd")
    spi.deinit()
    cs.deinit()
    
def get_sate():
    data = ''
    SD_CS = board.SD_CS  # setup for M0 Adalogger; change as needed
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    cs = digitalio.DigitalInOut(SD_CS)
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    with open("/sd/save.json", "r") as f:
        data = f.read()
    storage.umount("/sd")
    spi.deinit()
    cs.deinit()
    return data


