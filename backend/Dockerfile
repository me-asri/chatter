FROM python:3.11-slim

EXPOSE 8000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY chatter/ chatter

CMD python -m chatter