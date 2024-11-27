from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_restx import Api

#Initialize the Api with the prefix
api = Api(prefix="/api/pensum1.0/")

#Initialize the extensions
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

