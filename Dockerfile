FROM python:3.4-alpine
MAINTAINER Harry Daniels
COPY app/ /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
