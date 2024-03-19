FROM python:3.8-slim-buster

COPY ./src/ /app
WORKDIR /app

RUN pip3 install flask

EXPOSE 2535

CMD ["python3", "main.py", "2535"]
