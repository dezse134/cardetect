FROM python:3.12-slim

WORKDIR /usr/src/cardetect
ENTRYPOINT [ "python" ]
CMD [ "./upload_server.py" ]
EXPOSE 5000

RUN apt-get -q update && \
    apt-get -q -y --no-install-recommends install libglib2.0-0 libgl1-mesa-glx && \
    apt-get clean

COPY requirements.txt ./
RUN pip install \
    --root-user-action=ignore \
    --no-cache-dir \
    --progress-bar=off \
    -r requirements.txt

COPY src/cardetect ./