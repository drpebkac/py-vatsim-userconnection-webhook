FROM python:latest

COPY ./main.py /home/vathooks/

RUN pip install requests

ENTRYPOINT [ "python", "/home/vathooks/main.py" ]
