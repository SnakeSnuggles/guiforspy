from tkinter import *
from threading import Thread
import random
from pynput.keyboard import Key, Controller, Listener
import keyboard
import time


#removes '' if  there is something in the list
def checkadd():
    if len(whattopick) == 2:
        for x in whattopick:
            if x == '':
                whattopick.remove('')
#appends '' if there is nothing in the list                
def checkremove():
    if len(whattopick) == 1:
        whattopick.append('')

#coolest function ever
def classcaller(clas,str):

    if clas.get() == 1:
        whattopick.append(str)
        checkadd()
        
    else:
        checkremove()
        whattopick.remove(str)

#The functions that get called when the checkmarks are pressed      
def scout101():
    classcaller(scout,'1')        
def soldier101():
    classcaller(soldier,'2')
def pyro101():
    classcaller(pyro,'3')

def demoman101():
    classcaller(demoman,'4')
def heavy101():
    classcaller(heavy,'5')
def enginer101():
    classcaller(enginer,'6')
    
def medic101():
    classcaller(medic,'7')
def sniper101():
    classcaller(sniper,'8')
def spy101():
    classcaller(spy,'9')

#This is the part where the program picks from whattopick to press a random number
def thepickingpart(): 
    try:
        thethingthatcandostufftrustmeIknowwhatiamdoing = Controller()
        print("We are ready to go!")
        while iswindowgood == True:
            randomcrap = random.randint(0, len(whattopick)-1)
            if keyboard.read_key() == '4':
                time.sleep(0.46)
                

                thethingthatcandostufftrustmeIknowwhatiamdoing.press(whattopick[randomcrap])
                thethingthatcandostufftrustmeIknowwhatiamdoing.release(whattopick[randomcrap])
                time.sleep(0.01)
    except:
        print('idiot')
        thepickingpart()    
   
#this is the window it creates the window
def thewindow():
    global scout
    global soldier
    global pyro
    global demoman
    global heavy
    global enginer
    global medic
    global sniper
    global spy
    master = Tk()
    master.title('SnakeSnuggles super cool random spy thing')
    master.minsize(300, 250)
    p1 = PhotoImage(file = '350px-Spytaunt3.png')
    master.iconphoto(False, p1)

    #The buttons that add the items to randomly pick from
    scout = IntVar()
    Checkbutton(master, text='scout', variable=scout, onvalue = 1, offvalue = 0,command=scout101).grid(row=0, sticky=W)
    soldier = IntVar()
    Checkbutton(master, text='soldier', variable=soldier, onvalue = 1, offvalue = 0,command=soldier101).grid(row=1, sticky=W)
    pyro = IntVar()
    Checkbutton(master, text='pyro', variable=pyro, onvalue = 1, offvalue = 0,command=pyro101).grid(row=3, sticky=W)

    demoman = IntVar()
    Checkbutton(master, text='demoman', variable=demoman, onvalue = 1, offvalue = 0,command=demoman101).grid(row=4, sticky=W)
    heavy = IntVar()
    Checkbutton(master, text='heavy', variable=heavy, onvalue = 1, offvalue = 0,command=heavy101).grid(row=5, sticky=W)
    enginer = IntVar()
    Checkbutton(master, text='engineer', variable=enginer, onvalue = 1, offvalue = 0,command=enginer101).grid(row=6, sticky=W)

    medic = IntVar()
    Checkbutton(master, text='medic', variable=medic, onvalue = 1, offvalue = 0,command=medic101).grid(row=7, sticky=W)
    sniper = IntVar()
    Checkbutton(master, text='sniper', variable=sniper, onvalue = 1, offvalue = 0,command=sniper101).grid(row=8, sticky=W)
    spy = IntVar()
    Checkbutton(master, text='spy', variable=spy, onvalue = 1, offvalue = 0,command=spy101).grid(row=9, sticky=W)
    mainloop()
    
    
#The list that gets appened
whattopick = ['']

iswindowgood = True

prossesofwindow = Thread(target=thewindow)
prossesofpicking = Thread(target=thepickingpart)


prossesofpicking.start()
prossesofwindow.start()


prossesofpicking.join()
prossesofwindow.join()
