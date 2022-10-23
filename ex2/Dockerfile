FROM python:alpine3.16

WORKDIR /app

COPY scanner.py scanner.py
COPY requirements.txt requirements.txt

RUN apk update && apk add nmap

RUN pip3 install -r requirements.txt

RUN chmod +x /app/scanner.py

ENTRYPOINT ["python3", "-m", "scanner"]
