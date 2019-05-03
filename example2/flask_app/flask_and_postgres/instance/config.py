import os

user = os.environ.get("POSTGRES_USER", default=None)
pwd = os.environ.get("POSTGRES_PASSWORD", default=None)
db = os.environ.get("POSTGRES_DB", default=None)
host = 'postgres_db'
port = '5432'

SQLALCHEMY_DATABASE_URI =  'postgresql://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)
SECRET_KEY = 'mysecretkey'
