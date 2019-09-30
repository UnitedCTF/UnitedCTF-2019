FROM python:3.6

RUN pip3 install pycrypto

RUN mkdir /app
WORKDIR /app

COPY ./app.py /app/
COPY ./flag.py /app/
COPY ./key /app/

ENTRYPOINT [ "python3", "app.py" ]