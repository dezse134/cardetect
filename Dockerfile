FROM python:3.12-alpine

ENTRYPOINT [ "python" ]

WORKDIR /usr/src/cardetect
COPY cardetect.py haarcascade_cars.xml requirements.txt ./
RUN pip install --no-cache-dir --progress-bar=off -r requirements.txt
CMD [ ".//cardetect.py" ]
