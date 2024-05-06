FROM python:3.12-slim

WORKDIR /usr/src/cardetect
ENTRYPOINT [ "python", "-u" ]
CMD [ "./admin.py" ]

RUN pip install \
    --root-user-action=ignore \
    --no-cache-dir \
    --progress-bar=off \
    pika

COPY src/cardetect/admin.py ./
