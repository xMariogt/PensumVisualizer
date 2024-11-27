import os
from os.path import dirname, join
from dotenv import load_dotenv

class BaseConfig():
    
    #directory path for environment variables
    dotenv_path  = join(dirname(__file__), ".env")
    
    #load environment variables
    load_dotenv(dotenv_path, override= True)
    
    #CONFIGURAR LA SECRET KEY
    SECRET_KEY =os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = SECRET_KEY
    
    SQLALCHEMY_DATABASE_URI= ""
    
class DeveloperConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")
    
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")