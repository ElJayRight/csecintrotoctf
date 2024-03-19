FROM ubuntu:latest

RUN apt-get update && apt-get install -y && apt-get install python3 -y

EXPOSE 54129

RUN mkdir /app
COPY ./src /app/

WORKDIR /app
CMD ["python3","database.py"]
CMD ["python3","main.py"]
