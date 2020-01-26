from pygame import *
import pygame.midi as midi
from tkinter import *
midi.init()
def eeCallBack():
    io = input("Input/Output")
    if io.upper() == "I":
        while True:
            print(midi.Input)
    else:
        print(dir(midi.Output))
        
