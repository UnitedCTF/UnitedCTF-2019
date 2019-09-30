FROM python:3.7
RUN pip install flask

RUN mkdir /app
COPY ./app.py /app/
COPY ./templates /app/templates

WORKDIR /app
CMD [ "flask", "run", "-h", "0.0.0.0" ]