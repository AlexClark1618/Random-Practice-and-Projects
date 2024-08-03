import time
import threading
from pynput.mouse import Controller, Button
import keyboard

clicking = False  
mouse = Controller()

def clicker(): 
    while True:
        if clicking==True:
            mouse.click(Button.left, 1)
        time.sleep(0.001) #Time between clicks

def toggle():  
    global clicking

    while True: 
        if keyboard.is_pressed('t + c'):
            clicking = not clicking #Flips clicking value when t+c are pressed
            while keyboard.is_pressed('t + c'): #Prevents continually toggling while keys are pressed
                pass
        time.sleep(0.1)

#Allows for both the clicker and toggle function to run simultaneously 
clicking_thread = threading.Thread(target = clicker)
clicking_thread.start()

toggle_thread = threading.Thread(target = toggle)
toggle_thread.start()

