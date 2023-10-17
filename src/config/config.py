class Config():
    SECRET_KEY = '5039ab4e4c8343970e050da6ab541a62f450'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    
    # HOST = config('HOST')
    # PORT = config('PORT', cast=int)

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True