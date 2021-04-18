FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN splk-py-trace-bootstrap
EXPOSE 5000
CMD [ "splk-py-trace","python3", "app.py"]