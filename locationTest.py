import pyautogui as pag
x, y = pag.position()
print((x,y))

from PIL import ImageGrab
screen = ImageGrab.grab()
print(screen.getpixel(pag.position()))