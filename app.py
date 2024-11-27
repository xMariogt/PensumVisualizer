import os
from flask import Flask
from src.common.utils import ma, db, jwt, api


app = Flask(__name__)

if os.environ["FLASK_ENV"] == "development":
    app.config.from_object("settings.DeveloperConfig")
elif os.environ["FLASK_ENV"] == "testing":
    app.config.from_object("settings.TestConfig")
    
#Initialize the Api
api.init_app(app)

#Initialize the extensions
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

#Call the routes