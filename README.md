# Monkeytype-Cheat
Python based cheat for monkeytype.com

Requirnments
https://github.com/UB-Mannheim/tesseract/wiki
Download the installer

If you change install dir then make sure to change the dir inside main.py (LINE 41)

run main.py and install any needed imports
https://www.youtube.com/watch?v=7nEp34q_EdU
Shows install more in depth

# Install
You will need tesseract OCR so go to https://github.com/UB-Mannheim/tesseract/wiki and download
the x64 install or x32 if ur a wierdo

Once that is done you might need to install some dependencies with python

After running the script select the setup option and click the two points on your screen with the text you want to scan
NOTE any text inside the screenshot will be typed so dont include anything that you dont want typed. It is also a good
idea to make the html of the website easier to read and it is required to make all text that has already been typed invisible

Once you have it all setup you can choose start 
when prompted for a delay if you choose 0 then you will be asked for a rescan delay
if i use this to type the words
pyautogui.write(words, interval=wpm)
regardless of the number that I put into wpm the max it will go to is 730 words per minute
however if I do this
pyautogui.write(words) 
it fails after the first phrase so I need to add a delay 
![image](https://user-images.githubusercontent.com/72428571/173197290-b000e094-5ba0-4c97-b050-ee1fce5f51bf.png)
The lowest you can set the rescan delay to is 0.2 
When the countdown starts make sure you are tabbed in so the cheat can start typing once the counter runs out


