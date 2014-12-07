from flask import Flask
from config import Config
from handler import home_handler
from handler import user_handler
app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
app.register_blueprint(home_handler.home)
app.register_blueprint(user_handler.user)
if __name__ == "__main__":
    app.run(host='0.0.0.0')
