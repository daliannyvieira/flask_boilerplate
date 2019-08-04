import os
from flask import Flask
from flask_restplus import Api

service = Flask(__name__)
service.config['SQLALCHEMY_ECHO'] = True
service.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
service.config['CORS_HEADERS'] = 'Content-Type'
service.config['ENV'] = os.environ.get('APPLICATION_ENVIRONMENT')
service.config['DEBUG'] = True

api = Api(service)