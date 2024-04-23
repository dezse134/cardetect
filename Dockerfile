FROM python:3.12-alpine

ENTRYPOINT [ "python" ]

COPY cardetect.py haarcascade_cars.xml requirements.txt /usr/src/cardetect/
RUN pip install --no-cache-dir --progress-bar=off -r requirements.txt
CMD [ "/usr/src/cardetect/cardetect.py" ]
