from microbit import *

import audio
import utime
import music

start = utime.ticks_ms()
tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]

while True:

    display.scroll('CALIBAN', delay=175, wait=False, loop=False)
    while utime.ticks_ms() < start + 7000 :
        if button_a.was_pressed():
            while not button_a.was_pressed():
                display.show(Image.SMILE)
                if button_b.was_pressed() is True :
                    speaker.off()
                audio.play(Sound.GIGGLE, wait=False)
                sleep(1000)
                display.show(Image.SQUARE_SMALL)
                sleep(1000)
            break
        if button_b.was_pressed():
            while not button_b.was_pressed():
                display.show(Image.HEART_SMALL)
                if button_a.was_pressed() is True :
                    speaker.off()
                music.pitch(880, 6)
                sleep(500)
                display.show(Image.HEART)
                music.pitch(880, 6)
                sleep(500)
                display.clear()
                sleep(1000)
            break
        pass
    speaker.on()
    start = utime.ticks_ms()
