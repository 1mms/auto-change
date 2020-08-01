import pyautogui, time, keyboard
##Program by xtradanylz
autokill = False
while autokill == False:
	pixel = pyautogui.pixel(1913, 210)
	if pixel[0] == 224 and pixel[1] == 224 and pixel[2] == 224:
		pyautogui.press('4')
	else:
		pyautogui.press('3')
	time.sleep(.01)

	if keyboard.is_pressed('End'):
		autokill = True

#