import cv2 as cv
import pytesseract
import os
from PIL import Image

org_img = cv.imread('0.png', cv.IMREAD_GRAYSCALE)
cv.imshow('original', org_img)

threshold, mask = cv.threshold(org_img, 150, 255, cv.THRESH_BINARY)

cv.imshow('binary', mask)
blur = cv.medianBlur(mask,3)
cv.imshow('median', blur)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('1.png', blur)
text = pytesseract.image_to_string(Image.open('1.png'), lang=None)
os.remove('1.png')

print(text)