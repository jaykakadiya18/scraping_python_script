import pyautogui
import webbrowser as wb
import time
import random

msg = ["Hello", "Hii","Hola"]
wb.open("http://wa.me/XXXXXXXXXXXX")
time.sleep(4)
pyautogui.click(x=671, y=319, clicks=1, interval=2, button='left')
time.sleep(1)
pyautogui.click(x=702, y=392, clicks=1, interval=2, button='left')
print(pyautogui.size())
print(pyautogui.position())
print(pyautogui.position())
pyautogui.Size(width=1366, height=768)
time.sleep(10)
l=0
while l<51:
    pyautogui.write(random.choice(msg))
    pyautogui.click(x=1326, y=686, clicks=1, interval=2, button='left')
    l+=1
print(pyautogui.position())
print("Succes")
