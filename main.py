import pyautogui
import time
from PIL import Image
from pytesseract import pytesseract
import os

pyautogui.FAILSAFE= True #DONT CHANGE
cornermode = False #Used to find the locations for screenshots
screenshot_mode = False #If enabled it will take a screenshot based on the cords bellow and open it
typing_delay = 0.01 #Delay for how long the bot will take to press each key

x1 = 815
y1 = 633

x2 = 931
y2 = 116

while True:
    if cornermode:
        print(pyautogui.position())
    else:
        break

if screenshot_mode:
    for i in range(1,5):
        time.sleep(1)
        print(f"Get ready {int(i)} / 5")

    myScreenshot = pyautogui.screenshot(region=(x1,y1, x2, y2))
    myScreenshot.save(r'img.png')
    os.system('img.png')
    exit()


for i in range(1,5):
    time.sleep(1)
    print(f"Get ready {int(i)} / 5")


def screenshot():
    myScreenshot = pyautogui.screenshot(region=(x1,y1, x2, y2))
    myScreenshot.save(r'img.png')
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"img.png"
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    return text[:-1]


def fix_text():
    chn1 = screenshot()
    lst=list(chn1)
    str=''
    for i in lst:
        str+=i
    lst1=str.split("\n")
    str1=""
    for i in lst1:
        str1+=i+" "
    return str1


while True:
    pyautogui.write(fix_text(), interval=typing_delay)
