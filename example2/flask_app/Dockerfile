FROM python:3.7.3-alpine3.9
MAINTAINER Harry Daniels
COPY flask_and_postgres/ /flask_and_postgres/
WORKDIR /flask_and_postgres
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache bash
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
