import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI  = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get("DB_USER"), os.environ.get("DB_PASS"), os.environ.get("DB_HOST"), os.environ.get("DB_PORT"), os.environ.get("DB_NAME"))
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False