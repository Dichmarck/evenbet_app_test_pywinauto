import time
import pyautogui

while True:
    print(pyautogui.position())
    if pyautogui.position()[0] == pyautogui.position()[1] == 0:
        break
    time.sleep(0.3)
