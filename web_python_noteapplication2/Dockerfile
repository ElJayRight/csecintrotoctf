FROM python:3.8-slim-buster

COPY ./src/ /app
WORKDIR /app

RUN pip3 install flask

EXPOSE 2536

CMD ["python3", "main.py", "8080"]
