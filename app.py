from static.config import LocalAppConfig, AWSAppConfig
from views.create_app import create_app

app = create_app(AWSAppConfig)

if __name__ == '__main__':
    app.run(**app.config['RUN_SETTINGS'])
