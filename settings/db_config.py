class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    SECRET_KEY='SOME-KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///purity.db'
    DEBUG=True

# postgresql://postgres:Brian8053@@127.0.0.1:5432/payrollmanager