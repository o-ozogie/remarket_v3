class LocalAppConfig:
    HOST = '127.0.0.1'
    PORT = 5000
    DEBUG = True
    RUN_SETTINGS = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    }


class AWSAppConfig:
    HOST = '0.0.0.0'
    PORT = 800
    DEBUG = False
    RUN_SETTINGS = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    }
