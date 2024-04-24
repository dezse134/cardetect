FROM python:3.12-slim

RUN apt-get -q update && apt-get -q -y --no-install-recommends install libglib2.0-0 libgl1-mesa-glx && apt-get clean

ENTRYPOINT [ "python" ]

WORKDIR /usr/src/cardetect
COPY cardetect.py haarcascade_cars.xml requirements.txt ./
RUN pip install --root-user-action=ignore --no-cache-dir --progress-bar=off -r requirements.txt
CMD [ "./cardetect.py" ]
