FROM docker.io/python:3.11-slim

WORKDIR /app
COPY app.py .
COPY config.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLAG=KibSec{...}

EXPOSE 5000

CMD ["python", "app.py"] 
