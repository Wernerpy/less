# pip install opencv-python  
# https://docs-opencv-org.translate.goog/3.4/dc/dfc/group__videoio__flags__others.html?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=ru&_x_tr_pto=sc

import cv2
import time
x = 0
while True:
    time.sleep(1)
    #включение камеры

    cap = cv2.VideoCapture(0)

    #сделаем снимок 

    ret, frame = cap.read()

    #записать в фаил
    x = 1+x

    name = "camera" + str(x) + ".jpg " 

    cv2.imwrite(name, frame)

    #отключить камеру

    cap.release()

#print(dir(cv2))
