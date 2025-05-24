FROM python:3.11-alpine

RUN apk update && apk add --no-cache \
    bash \
    py3-pip \
    py3-setuptools \
    py3-cryptography \
    fortune \
    && rm -rf /var/cache/apk/*

RUN pip install pycryptodome Flask

WORKDIR /app

COPY fortune.py /app/fortune.py
COPY source.py /app/source.py

EXPOSE 5000

CMD ["python", "source.py"]
