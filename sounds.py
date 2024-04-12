import winsound
from threading import Thread

class Sounds:
    def play_sound(self, state_change, state):
        if state_change:
            if state == 'reg':
                thread = Thread(target=make_sound_reg)
            if state == 'pet':
                thread = Thread(target=make_sound_pet)
            if state == 'com':
                thread = Thread(target=make_sound_com)
            if state == 'pok':
                thread = Thread(target=make_sound_pok)
            if state == 'scr':
                thread = Thread(target=make_sound_scr)
            thread.start()
            print('hey')

def make_sound_reg():
    winsound.PlaySound('sounds/reg.wav', winsound.SND_FILENAME)

def make_sound_pet():
    winsound.PlaySound('sounds/pet.wav', winsound.SND_FILENAME)

def make_sound_pok():
    winsound.PlaySound('sounds/pok.wav', winsound.SND_FILENAME)

def make_sound_com():
    winsound.PlaySound('sounds/com.wav', winsound.SND_FILENAME)

def make_sound_scr():
    winsound.PlaySound('sounds/scr.wav', winsound.SND_FILENAME)

