import os
from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

DATABASE_URI = os.environ.get('DATABASE_URI')

service = Flask(__name__)
service.config['SQLALCHEMY_ECHO'] = True
service.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
service.config['CORS_HEADERS'] = 'Content-Type'
service.config['ENV'] = os.environ.get('APPLICATION_ENVIRONMENT')
service.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
service.config['DEBUG'] = True

db = SQLAlchemy(service)

api = Api(service)