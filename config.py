from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True
