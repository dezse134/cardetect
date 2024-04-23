"""Module for detecting cars on a picture"""

from os import listdir

import cv2

if __name__ == '__main__':

    for file in listdir('input'):
        img_name = 'input/' + file

        car_cascade = cv2.CascadeClassifier('haarcascade_cars.xml')
        img = cv2.imread(img_name)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur_img = cv2.GaussianBlur(gray_img, (5,5), 0)
        cars = car_cascade.detectMultiScale(blur_img, 1.1, 3)

        for (x,y,w,h) in cars:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)

        cv2.imwrite(f'output/result_{file}', img)

        print(f'Found {len(cars):>3d} cars on {file}')
