import tkinter as tk
from threading import Thread
import random
import keyboard
import time
import os

'''
TODO:
1) Make it dark mode (D)
2) Make the thing look better (D)
3) Add a place to change the keybind for the selection
4) Make it so when the window is closed the console will also be closed (D)
5) Get rid of the console 
6) Add a instruction menu with what this is used for and how to use it (D)
7) Add the ability to change color 1 and color 2 and color 3
8) Add the ability to change the delay of picking a disguise
9) Change the top, title menu to make it look better
10) Add a settings menu 
'''
# COLOR1 = "#350A0B"
# COLOR2 = "#540D0A"
# COLOR1 = "#0E1721"
# COLOR2 = "#084A5A"
COLOR1 = "#191919"
COLOR2 = "#081E4C"

exit_flag = False
def get_documents_path():
    # Get the path to the Documents folder
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    return documents_path

def readr():
    try:
        documents_path = get_documents_path()
        file_path = "show.txt"
        with open(file_path, "r") as file:
            line = file.readline()
            return line
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write("")
def readw(what_to_write) -> None:
    documents_path = get_documents_path()
    file_path = "show.txt"

    with open(file_path, "w") as file:
        file.write(what_to_write)

def instructions_window():
    instructions = tk.Tk()
    instructions.title("Spy disguise")
    instructions.geometry("400x200")
    instructions.resizable(False, False)
    instructions.config(bg=COLOR1)
    p1 = tk.PhotoImage(file = 'icon.png')
    instructions.iconphoto(False, p1)
    def end_instructions():
        instructions.destroy()
    def end_and_never_show():
        readw("true")
        instructions.destroy()
    text_to_add = '''To use: 
    1) Click on the classes you want to be choosen 
    2) Press 4 and let the program do the rest
    Used for:
    the spy in tf2, this allows for random choosing of spy disguises'''
    title = tk.Label(instructions,text="Snake's Spy Disguises",bg=COLOR1,fg='white')
    content = tk.Label(instructions,text=text_to_add,bg=COLOR1,fg='white')
    continuebut = tk.Button(instructions,text="Continue",command=end_instructions)
    continuebutnev = tk.Button(instructions,text="Continue and never show again",command=end_and_never_show)
    title.pack()
    title.config(font=("Arial", 12))
    content.pack()
    content.config(font=("Arial", 10))
    continuebut.pack(pady=5)
    continuebutnev.pack(pady=5)
    continuebut.config(background=COLOR2,fg='white')
    continuebutnev.config(background=COLOR2,fg='white')    
    instructions.mainloop()

def main_window():
    global to_pick_from,exit_flag
    should_show = readr()
    if should_show != 'true':
        instructions_window()

    def class_caller(class_var,button:str):
        ischecker = class_var.get() == 1
        if ischecker:
            to_pick_from.append(button)  
        else:
            to_pick_from.remove(button)
    window = tk.Tk()
    menu_bar = tk.Menu(window, bg="blue", fg='white')
    menu_bar.add_command(label="Settings", command=lambda:print("HEYO"))

    window.title("Spy disguise")
    window.geometry("190x260")
    window.resizable(False, False)
    window.config(bg=COLOR1)
    window.config(menu=menu_bar)
    p1 = tk.PhotoImage(file = 'icon.png')
    window.iconphoto(False, p1)
    text = ["Scout" , "Soldier" , "Pyro" , "Demoman" , "Heavy" , "Engineer" , "Medic" , "Sniper" , "Spy"]
    vars = []

    to_pick_from = []
    for x in range(len(text)):
        vars.append(tk.IntVar())
        checkbox = tk.Checkbutton(window, text=text[x], variable=vars[x], bg=COLOR1, fg='white',
                                   command=lambda x=x+1: class_caller(vars[x-1], str(x)))
        checkbox.config(font=('Arial', 12), activebackground=COLOR1,activeforeground='white', selectcolor=COLOR2)
        checkbox.grid(row=x, sticky=tk.W)
    window.mainloop()
    exit_flag = True

def picking_part():
    while not exit_flag:
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
windowing = Thread(target=main_window)

picking.start()
windowing.start()

picking.join()
windowing.join()