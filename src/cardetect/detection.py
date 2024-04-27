"""Module for detecting cars on a picture"""

from os import listdir
from os.path import join

import cv2

def detect_cars(input_folder, output_folder):
    """Detect cars on an image"""
    car_counts = {}
    for f in listdir(input_folder):
        img_name = join(input_folder, f)
        car_cascade = cv2.CascadeClassifier('resources/haarcascade_cars.xml')
        img = cv2.imread(img_name)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur_img = cv2.GaussianBlur(gray_img, (5,5), 0)
        cars = car_cascade.detectMultiScale(blur_img, 1.1, 3)

        for (x,y,w,h) in cars:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)

        cv2.imwrite(f'{output_folder}/result_{f}', img)
        car_counts[f] = len(cars)

    return car_counts

if __name__ == '__main__':
    __counts = detect_cars('input', 'output')
    for __file, __count in __counts.items():
        print(f'Found {__count:>3d} cars on {__file}')
