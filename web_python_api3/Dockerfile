FROM python:3.8-slim-buster

RUN pip3 install flask  pyjwt

EXPOSE 2534

RUN mkdir /app
COPY ./src /app/

WORKDIR /app
CMD ["python3","database.py"]
CMD ["python3","main.py"]
