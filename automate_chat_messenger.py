import pyautogui
import time

# Stroing Data
text = 'Hey, @i_python_star \n I am @Pythonide, The Automation Bot'
# text = ' Data you want to store '

while True:
    time.sleep(3)
    pyautogui.typewrite(text)

    time.sleep(2)
    pyautogui.press('enter')