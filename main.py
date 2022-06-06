#Importing all needed packages
import cv2
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np


#Loading and displaying image in window
img = cv2.imread('miami.jpg',cv2.IMREAD_COLOR)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


def increasing_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


increasing_brightness()