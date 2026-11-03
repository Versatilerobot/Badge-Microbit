# Imports go at the top
from microbit import *

import audio
import utime
import music

# Code in a 'while True:' loop repeats forever
while True:
    set_volume(255)
    start = utime.ticks_ms()
    display.scroll('CALIBAN', delay=175, wait=False, loop=False)
    while utime.ticks_ms() < start + 8000 :
        if button_a.was_pressed():
            while not button_a.was_pressed():
                display.show(Image.SMILE)
                if button_b.was_pressed() is True :
                    set_volume(0)
                audio.play(Sound.GIGGLE, wait=False)
                sleep(1000)
                display.show(Image.SQUARE_SMALL)
                sleep(1000)
            break
        if button_b.was_pressed():
            while not button_b.was_pressed():
                display.show(Image.HEART_SMALL)
                if button_a.was_pressed() is True :
                    set_volume(0)
                music.pitch(880, 6)
                sleep(500)
                display.show(Image.HEART)
                music.pitch(880, 6)
                sleep(500)
                display.clear()
                sleep(1000)
            break
        pass
   
