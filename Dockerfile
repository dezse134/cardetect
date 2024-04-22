FROM python:3.12-alpine

COPY hello.py /root/

ENTRYPOINT [ "python" ]
CMD [ "/root/hello.py" ]
