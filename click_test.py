import pyautogui as pag
from PIL import ImageGrab
import time
import keyboard


# 경고창 확인 함수#############################################################
def IsAlert():
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert

        alert.accept()
        print("alert clear")
        return True

    except:
        print("no alert")
        return False

def color(RGB):  # RGB 값을 색깔 문자열로 반환하는 함수
    c_p = (124, 104, 238)
    c_g = (28, 168, 20)
    c_c = (23, 179, 255)
    c_o = (251, 126, 79)
    c_r = (255, 68, 15)
    test = (0, 0, 0)
    if ((c_p[0] - 5 < RGB[0] < c_p[0] + 5)
            and (c_p[1] - 5 < RGB[1] < c_p[1] + 5)
            and (c_p[2] - 5 < RGB[2] < c_p[2] + 5)):
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
    screen = ImageGrab.grab()  # 화면 캡쳐
    for j in range(225, 746, 8):
        # for j in range(0, 992):
        for i in range(159, 544, 9):
            #    for i in range(0, 900):
            A = color(screen.getpixel((i, j)))  # 가장왼쪽자리
            if (A == "purple"):  # 5색깔 중 하나 + 두 자리
                print(A)
                print((i,j))
                pag.click((i, j))
                pag.click(747, 674)  # 좌석선택완료
                if (IsAlert()):
                    SB = 0
                    pag.click((i, j))
                    screen = ImageGrab.grab()
                else:
                    SB = 1
            if SB == 1:
                break

        if SB == 1:
                break
input()