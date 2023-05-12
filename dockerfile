FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN uvicorn main:app 

CMD ["python3", "-m", "uvicorn", "run", "--host=0.0.0.0"]

FROM alpine

WORKDIR /

EXPOSE 8080

ENTRYPOINT ["/spacer"]