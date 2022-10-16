FROM python:alpine3.16

COPY getweather /app/getweather

RUN chmod +x /app/getweather

RUN /app/getweather
