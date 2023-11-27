from os import environ

class Config:
    SECRET_KEY = ''  # Cambia esto por una clave secreta segura
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'mysql://root:@localhost/presupuestar'
    SQLALCHEMY_TRACK_MODIFICATIONS = False