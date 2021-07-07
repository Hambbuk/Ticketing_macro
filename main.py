from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pag
from PIL import ImageGrab
from PIL import Image
import time
import keyboard
import cv2 as cv
import pytesseract
import re
import numpy as np


chrome_driver = 'chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)
driver_time = webdriver.Chrome(chrome_driver)

################################네이비즘 서버시간########################################################
driver_time.set_window_size(800, 300)
driver_time.get("https://time.navyism.com/?host=ticket.interpark.com")
driver_time.find_element_by_id("msec_check").click()
#######################################################################
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
################################################################
def capture_start():
    seat1_frame = driver.find_element_by_name("ifrmSeat")
    driver.switch_to_frame(seat1_frame)
    image = driver.find_element_by_id('imgCaptcha')
    image2 = image.screenshot_as_png
    with open("0.png", "wb") as file:
             file.write(image2)
    # for i in range(0, 1):
    #     image2 = image.screenshot_as_png
    #     with open("%d.png" % i, "wb") as file:
    #         file.write(image2)
    #         return image2
        # driver.find_element_by_class_name('refreshBtn').click()

def existsElement():
    try :
        capture_start()
    except :
        return False
    return True

################################로그인#####################################################
driver.set_window_size(1400, 1200)
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login')
driver.implicitly_wait(3)

driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('bin2716') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('gksqls0823!') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)
########################################################################################

#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21002720')
#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21004910')
# 헤드윅
driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21005689')
#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21005562')
# 마리앙투아네트 테스트
#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21004304')

# 날짜 선택은 수동으로!!!!
# #############날짜 선택#################################
# pag.click(979, 929)
# time.sleep(0.2)
# pag.click(1225, 430) #8월
# time.sleep(0.2)
# pag.click(1160, 491) #4일
# time.sleep(0.3)
# #########################################################
# 팝업창 뜨면 끄기
try:
    driver.find_element_by_xpath('//*[@id="popup-prdGuide"]/div/div[3]/button').click()
except:
    pass

MB = True

#예매대기 루프 server_time[4]:분. server_time[5]:초
###########################################################
while True:
    a = driver_time.find_element_by_id('time_area').text
    b = driver_time.find_element_by_id('msec_area').text

    server_time = re.findall("[0-9]+", a)
    ##server_time[4]:분. server_time[5]:초
    #if(server_time[4]=='50' and server_time[5]=='30'):
    if(int(server_time[5])%10==0): # 10초마다 테스트
        msec = re.findall("[0-9]", b)
        if(int(msec[0])>=0):
            break

##########################################################
#driver.find_element_by_xpath('(//*[@id="CellPlayDate"])' + "[" + "20210812" + "]").click()

################날짜 선택############################################################################################
driver.find_element_by_xpath('//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[1]/li[3]').click() # 다음달(8월)
time.sleep(0.1)
driver.find_element_by_xpath('(//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[12])').click() # 12일


while MB:
    resbutton = driver.find_element_by_xpath('//*[@id="productSide"]/div/div[2]/a[1]')
    if(resbutton.text=='예매하기'):
        print('예매')
        resbutton.click()
        MB = False
        break
    else:
        print('새로고침')
        driver.refresh()


time.sleep(1)
# 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
# driver.switch_to.window(driver.window_handles[1])
# driver.get_window_position(driver.window_handles[1])


##########################################################
                  #catcha#
cnt = 0
is_captcha = True
while(is_captcha):
    # 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
    print('start_capthca')
    driver.switch_to.window(driver.window_handles[1])
    driver.get_window_position(driver.window_handles[1])
    
    capture_start()
    #########################OLD_OPENCV##########################################
    # org_img = cv.imread('0.png', cv.IMREAD_GRAYSCALE)
    # # cv.imshow('original', org_img)
    #
    # threshold, mask = cv.threshold(org_img, 150, 255, cv.THRESH_BINARY)
    #
    # # cv.imshow('binary', mask)
    # blur = cv.medianBlur(mask,3)
    # # cv.imshow('median1', blur1)
    # # cv.waitKey(0)
    # # cv.destroyAllWindows()
    #
    # # cv.imwrite('1.png', blur)
    # # # text = pytesseract.image_to_string(Image.open('1.png'), lang='eng')
    # # text = pytesseract.image_to_string(Image.open('1.png')
    # #                                    , config = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # #                                    , lang='eng')
    ###################################################################################################


    #####################################NEW_OPENCV######################################################
    # Load image, grayscale, adaptive threshold
    image = cv.imread('0.png')
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 85, 1)

    # Morph open
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)

    # Remove noise by filtering using contour area
    cnts = cv.findContours(opening, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv.contourArea(c)
        if area < 30:
            cv.drawContours(opening, [c], -1, (0, 0, 0), -1)
    kernel2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    opening = cv.filter2D(opening, -1, kernel2)

    # Invert image for result
    result = 255 - opening
    cv.imwrite('1.png', result)
    ##############################################################################################
    text = pytesseract.image_to_string(result
                                       , config = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                       , lang='eng')
    driver.find_element_by_class_name('validationTxt').click()
    driver.find_element_by_xpath('// *[ @ id = "txtCaptcha"]').send_keys(text)
    # pag.click(441, 535)
    # pag.write(text)
    print(text)



##################captcha 실패시 새로고침#################################
    driver.switch_to.window(driver.window_handles[1])
    driver.get_window_position(driver.window_handles[1])
    is_captcha = existsElement()
    print(is_captcha)

    if(is_captcha==True) :
        cnt += 1
        # 디버깅용 이미지 저장
        cv.imwrite('fail%d.png'%cnt, result)
        driver.find_element_by_class_name('refreshBtn').click()

#########################################################
# while(True):
#     if keyboard.is_pressed('1'):
#        break
#    else:
#        pass



def color(RGB):  # RGB 값을 색깔 문자열로 반환하는 함수
    color_range = (10, 10, 10)
    c_p = (124, 104, 238)
    c_g = (28, 168, 20)
    c_c = (23, 179, 255)
    c_o = (251, 126, 79)
    c_r = (255, 68, 15)
    test = (0,0,0)
    if ((c_p[0]-5 < RGB[0] < c_p[0]+5)
        and (c_p[1]-5 < RGB[1] < c_p[1]+5)
        and (c_p[2]-5 < RGB[2] < c_p[2]+5)) : return "purple"
    elif RGB == c_g: return "green"
    elif RGB == c_c: return "cyan"
    elif RGB == c_o: return "orange"
    elif RGB == c_r: return "red2"
    # elif RGB == test: return "test"
    else: return "other"
SB=0
cnt=0
err = Alert(driver)

print("here!!!!!!!!!!")
# input()
while SB==0:
    if keyboard.is_pressed('2'):
        break
    else:
        #######취켓팅용 새로고침#########
        # pag.click(849, 704)
        # time.sleep(0.5)
        ############Z_###################
        screen = ImageGrab.grab() # 화면 캡쳐
        for j in range(219, 753):
        #for j in range(0, 992):
            for i in range(145, 564):
        #    for i in range(0, 900): 
                # if i%30==0 and j % 30==0 : pag.click((i,j))
                A = color(screen.getpixel((i,j))) # 가장왼쪽자리
                if (A == "purple"): # 보라 또는 초록
                    print(A)
                    pag.click((i+3,j+3))
                    pag.click(871, 669) #좌석선택완료
                    if(IsAlert()):
                        SB = 0
                        screen = ImageGrab.grab()
                    else: SB=1
                if SB==1:
                    break
            if SB==1:
                break
input()