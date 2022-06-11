import pyautogui
import time
from PIL import Image
from pytesseract import pytesseract
import os
import win32api
import json

pyautogui.FAILSAFE= True
f = open('screenshot_cords.json')
data = json.load(f)

def ypos():
    y1 = str(pyautogui.position())
    y2 = y1.replace("Point(x=","")
    y3 = y2.rsplit(',', 1)[1]
    y4 = y3.replace(" y=", "")
    y5 = y4.replace(")", "")
    return y5


def xpos():
    x1 = str(pyautogui.position())
    x2 = x1.replace("Point(x=","")
    x3 = x2.split(',', 1)[0]
    return x3


def screenshot():
    myScreenshot = pyautogui.screenshot(region=(
        data["x1"],
        data["y1"],
        int(data["x2"]) - int(data["x1"]),
        int(data["y2"]) - int(data["y1"])
        ))
    myScreenshot.save(r'img.png')


def scan_text():
    screenshot()
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"img.png"
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    return text[:-1]

def fix_text():
    chn1 = scan_text()
    lst=list(chn1)
    str=''
    for i in lst:
        str+=i
    lst1=str.split("\n")
    str1=""
    for i in lst1:
        str1+=i+" "
    return str1

os.system('cls')
print("1. Setup\n2. Start")
points = 0
cmd = int(input("> "))
if cmd == 1:
    os.system('cls')
    print("Left click both points on the screen")
    state_left = win32api.GetKeyState(0x01)
    state_right = win32api.GetKeyState(0x02)
    while True:
        if points >= 2:
            break
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)
        if a != state_left:
            state_left = a
            if a < 0:
                points +=1
                if points == 1:
                    print(pyautogui.position())
                    data["x1"] = xpos()
                    data["y1"] = ypos()
                if points == 2:
                    print(pyautogui.position())
                    data["x2"] = xpos()
                    data["y2"] = ypos()
        if b != state_right:
            state_right = b
            if b < 0:
                pass
            else:
                pass
        time.sleep(0.001)
    screenshot()
    with open("screenshot_cords.json", "w") as outfile:
        json.dump(data, outfile)
    os.system('img.png')
    os.system('python main.py')
elif cmd == 2:
    if int(len(data)) < 1:
        print("Please setup the cheat first")
        input("Press Enter to continue")
        os.system('python main.py')
    os.system('cls')
    goal_wpm = float(input("Enter delay\n> "))
    if goal_wpm == 0:
        os.system("cls")
        sleep_del = float(input("Rescan Delay\n> "))
    print("Saved cords:")
    print(f"  [x1 {data['x1']}]")
    print(f"  [y1 {data['y1']}]")
    print(f"  [x2 {data['x2']}]")
    print(f"  [y2 {data['y2']}]")
    input("Press enter to begin")
    for i in range(1,5+1):
        print(f"Get ready {6-i}s left")
        time.sleep(1)
    while True:
        if goal_wpm == 0:
            pyautogui.write(fix_text())
            time.sleep(sleep_del)
        else:
            pyautogui.write(fix_text(), interval=goal_wpm)
