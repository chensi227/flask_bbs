# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    """
    基类Config中包含通用配置，子类分别定义专用的配置。
    如果需要，还可以添加其他配置类。
    为了让配置方式更灵活且安全，某些配置可以从环境变量中导入，
    例如SECRET_KEY，但也提供一个默认值，以防环境中没有定义。
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string i dont want to change'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 为True时，每次请求结束后会自动提交数据库的变动
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = 'hello flask'
    MAIL_SENDER = os.environ.get('MAIL_SENDER')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/flask"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/test"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/test"

# 在这里config字典中注册了不同的配置环境，而且还注册了一个默认配置。
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}





