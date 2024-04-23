FROM python:3.12-alpine

COPY cardetect.py haarcascade_cars.xml /usr/src/

ENTRYPOINT [ "python" ]
CMD [ "/usr/src/cardetect.py" ]
