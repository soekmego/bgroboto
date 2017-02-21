import pyautogui

#to escape a mouse out of control, move the mouse quickly to the upper-left
#corner of the screen
pyautogui.FAILSAFE = True

width, height = pyautogui.size() #the size function returns two values
				 #the current width & height of the screen
				 #both get assigned to the variables

for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)


