# project/config.py


import os


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'testbyyuuki@google.com'
    MAIL_PASSWORD = 'fgrlspuehhaxlhey'


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
