#Jeu = https://www.jeu.fr/jeu/piano-magique

import pyautogui
import keyboard
import win32api, win32con
import time

time.sleep(1)

def click(x,y):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(0.01)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("s") == False:
  if pyautogui.pixel(2200, 500)[0] == 0:
    click(2200, 500)
  if pyautogui.pixel(2300, 500)[0] == 0:
    click(2300, 500)
  if pyautogui.pixel(2400, 500)[0] == 0:
    click(2400, 500)
  if pyautogui.pixel(2500, 500)[0] == 0:
    click(2500, 500)