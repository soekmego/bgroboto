#! python3
# mouseNow.py - Displays the mouse cursor's current position.
#

import pyautogui

print("Press Ctrl-C to quit.")
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr, end="")
        print("\b" * len(positionStr), end = "", flush=True)
	#the end = "" argument to print prevents a newline character.
	#flush=True has to be called when a backspace character is used,
	#otherwise the screen might not update the text
except KeyboardInterrupt:
    print("\nDone.")
