import pyautogui
import time
import PIL
import sys
from pynput import keyboard

def doload():
    i = 0
    while True:
        pos = []
        pos = pyautogui.locateCenterOnScreen('images/load.png')
        if pos:
            print("\nFound match")
            print(str(pos[0]), str(pos[1]))
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click(pos[0],pos[1],clicks=1,interval=0,button='left')
            print('click on: ', str(pos[0]), str(pos[1]))
            break
        if i >=30:
            print('\n\n\nnothing found')
            exit()
        time.sleep(0.2)
        print(".", end="")
        i += 1
def doloadtwo():
    while True:
        pos = []
        pos = pyautogui.locateCenterOnScreen('images/loadtwo.png')
        if pos:
            print("\nFound match")
            print(str(pos[0]), str(pos[1]))
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click(pos[0],pos[1],clicks=1,interval=0,button='left')
            print('click on: ', str(pos[0]), str(pos[1]))
            break
        time.sleep(0.2)
        print("Looping")
def doigcheck():
    i = 3
    while True:
        pos = []
        pos = pyautogui.locateCenterOnScreen('images/igcheck.png')
        if pos:
            print("\nFound match")
            print(str(pos[0]), str(pos[1]))
            print('\nNow ingame')
            break
        elif i <= 0:
            break
        time.sleep(0.2)
        i -= 1
        print("Looping")
def speed():
    pyautogui.keyDown('3')
    pyautogui.keyUp('3')
def dovictorycheck():
    i = 8
    while True:
        pos = []
        pos = pyautogui.locateCenterOnScreen('images/victory.png')
        if pos:
            print("\nFound match")
            print(str(pos[0]), str(pos[1]))
            print('\nVictory!')
            break
        elif i <= 0:
            pyautogui.keyDown('esc')
            pyautogui.keyUp('esc')
            speed()
            break
        time.sleep(0.1)
        i -= 1
        print("Looping")
def dovic():
    while True:
        pos = []
        pos = pyautogui.locateCenterOnScreen('images/ok.png')
        if pos:
            print("\nFound match")
            print(str(pos[0]), str(pos[1]))
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click(pos[0],pos[1],clicks=1,interval=0,button='left')
            print('click on: ', str(pos[0]), str(pos[1]))
            break
        time.sleep(0.2)
        print("Looping")
def doexit():
    while True:
        pos = []
        pos = pyautogui.locateCenterOnScreen('images/exit.png')
        if pos:
            print("\nFound match")
            print(str(pos[0]), str(pos[1]))
            pyautogui.moveTo(pos[0], pos[1])
            print("Exiting")
            pyautogui.click(pos[0],pos[1],clicks=1,interval=0,button='left')
            print('click on: ', str(pos[0]), str(pos[1]))
            break
        time.sleep(0.2)
        print("Looping")   
def dogeneaccept():
    i = 10
    while True:
        pos = []
        pos = pyautogui.locateCenterOnScreen('images/oktwo.png')
        if pos:
            print("\nFound match")
            print(str(pos[0]), str(pos[1]))
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click(pos[0],pos[1],clicks=1,interval=0,button='left')
            print('click on: ', str(pos[0]), str(pos[1]))
            break
        elif i <= 0:
            break
        time.sleep(0.1)
        print("Looping")
        i -= 1

x = pyautogui.prompt('How many times do you want to clear the game: ')
message = pyautogui.confirm(text='Press OK when ready', title='Ready?', buttons=['OK', 'EXIT'])
if message != 'OK':
    sys.exit()
for i in range(0, int(x)):
    print('Load Save game ', end="")
    doload()
    doloadtwo()
    print('Wait for game')
    doigcheck()
    print('Speed up time')
    speed()
    print('Checking for victory')
    dovictorycheck()
    print('Accepting victory')
    dovic()
    print("exitting gamephase")
    doexit()
    print('Accepting new gene if there is any.')
    dogeneaccept()
    print('Done')
    print('Restarting')
    
