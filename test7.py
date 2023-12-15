import pyautogui
import time
time.sleep(9)
while(1>0):
  pyautogui.write('ok')
pyautogui.FAILSAFE = False
#pyautogui.FAILSAFE_POINTS = [ (1920, 0)]  # Setting failsafe locations to top-left and top-right corners
'''In PyAutoGUI, a failsafe mechanism is in place to prevent accidental infinite loops 
or other problematic situations that might occur while running a script. The failsafe 
feature allows the user to quickly move the mouse cursor to one of the corners of the 
primary screen to trigger a failsafe exit. By default, the failsafe mechanism is 
enabled, and the failsafe coordinates are set to (0, 0), which is the top-left corner
 of the screen.okokokokokokokokokokokokokokokokokokokokok

Here's how the failsafe mechanism works:okokokokokokokokokokok

Failsafe Location: The failsafe feature is triggered when the mouse cursor is moved to
 the failsafe location, which is (0, 0) by default. If you want to change the failsafe 
 location, you can call the pyautogui.FAILSAFE = False statement and set the failsafe
   location to a different coordinate using the pyautogui.FAILSAFE_POINTS list.

For example:'''
