FROM python:3.7.3-alpine3.9
MAINTAINER Harry Daniels
COPY flask_and_postgres/ /flask_and_postgres/
WORKDIR /flask_and_postgres
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache bash
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
## CMD ["python", "app.py"]
