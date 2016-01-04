import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'alsdjfal98aw7ef9a87sd9f78s'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SHITTOGETDONE_ADMIN = os.environ.get('SHITTOGETDONE_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'postgresql://skeller:holeysmokes@127.0.0.1/shittogetdone'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://skeller:holeysmokes@127.0.0.1/shittogetdone'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
