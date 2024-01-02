import tkinter as tk
from threading import Thread
import random
import keyboard
import time

'''
TODO:
1) Make it dark mode
2) Make the thing look better
3) Add a place to change the keybind for the selection
4) Make it so when the window is closed the console will also be closed
5) Get rid of the console 
6) Try to store the icon in the python source 
'''
COLOR1 = "#333940"
def window_part():
    global to_pick_from
    def class_caller(class_var,button:str):
        ischecker = class_var.get() == 1
        if ischecker:
            to_pick_from.append(button)  
        else:
            to_pick_from.remove(button)
    window = tk.Tk()
    window.title("Spy disguise")
    window.geometry("190x240")
    window.resizable(False, False)
    window.config(bg=COLOR1)
    p1 = tk.PhotoImage(file = '350px-Spytaunt3.png')
    window.iconphoto(False, p1)
    text = ["Scout" , "Soldier" , "Pyro" , "Demoman" , "Heavy" , "Engineer" , "Medic" , "Sniper" , "Spy"]
    vars = []

    to_pick_from = []
    for x in range(len(text)):
        vars.append(tk.IntVar())
        checkbox = tk.Checkbutton(window, text=text[x], variable=vars[x],bg=COLOR1,fg='white',command=lambda x=x+1: class_caller(vars[x-1], str(x))).grid(row=x, sticky=tk.W)
    window.mainloop()

def picking_part():
    while True:
        try:
            if keyboard.is_pressed("4"):
                time.sleep(0.2)
                choice = random.randint(0,len(to_pick_from)-1)
                keyboard.press(to_pick_from[choice])
                time.sleep(0.1)
                keyboard.release(to_pick_from[choice])
        except IndexError:
            ...

picking = Thread(target=picking_part)
windowing = Thread(target=window_part)

picking.start()
windowing.start()

picking.join()
windowing.join()