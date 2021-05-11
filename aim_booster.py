#Jeu : http://www.aimbooster.com/

import pyautogui
import keyboard
import win32api, win32con
import time

time.sleep(2)

def click(x,y):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(0.01)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("s") == False:
  origin_x = 2280
  origin_y = 380
  pic = pyautogui.screenshot(region=(origin_x, origin_y, 600, 420))
  pic_width, pic_height = pic.size

  for x in range(0, pic_width, 5):
    for y in range(0, pic_height, 5):
      r, g, b = pic.getpixel((x, y))

      if b == 195:
        click(origin_x + x, origin_y + y)
        time.sleep(0.05)
        break