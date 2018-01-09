import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = create_app(config_name, APP_ROOT)

if __name__ == '__main__':
    app.run()
