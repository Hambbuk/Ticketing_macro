from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
from PIL import ImageGrab
from PIL import Image
import time
import keyboard
import cv2 as cv
import pytesseract
import re



def color(RGB):  # RGB 값을 색깔 문자열로 반환하는 함수
    c_p = (124, 104, 238)
    c_g = (28, 168, 20)
    c_c = (23, 179, 255)
    c_o = (251, 126, 79)
    c_r = (255, 68, 15)
    test = (0, 0, 0)
    if RGB == c_p:
        return "purple"
    elif RGB == c_g:
        return "green"
    elif RGB == c_c:
        return "cyan"
    elif RGB == c_o:
        return "orange"
    elif RGB == c_r:
        return "red"
    elif RGB == test:
        return "test"
    else:
        return "other"


SB = 0

print("here!!!!!!!!!!")
while SB == 0:
    if keyboard.is_pressed('2'):
        break
    else:
        pag.click(849, 704)
        time.sleep(0.5)
        screen = ImageGrab.grab()  # 화면 캡쳐
        for j in range(219, 753):
            # for j in range(0, 992):
            for i in range(145, 564):
                #    for i in range(0, 900):
                if i%30==0 and j % 30==0 : pag.click((i,j))
                A = color(screen.getpixel((i, j)))  # 가장왼쪽자리
                if (A == "purple" or A == "green"):  # 5색깔 중 하나 + 두 자리
                    print(A)
                    pag.click((i, j))
                    pag.click((i + 3, j + 3))
                    pag.click(871, 669)  # 좌석선택완료
                    SB = 1
                    break
                if SB == 1:
                    break
            if SB == 1:
                break
input()