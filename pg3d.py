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
        
select = Tk()
start = Button(select, text="Start",startCallBack)
debugger_label(select, text="Debugger")
debugger = Entry(select)
debugger
