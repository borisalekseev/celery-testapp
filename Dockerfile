FROM python:3.8.10
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
WORKDIR /app
