from flask import jsonify
from flask_restplus import Resource
from application.App import api
from domain.AllGreetings import AllGreetings

@api.route('/hello')
class HelloWorld(Resource):
  def get(self):
    try:
      greeting = AllGreetings.read_all()
      return jsonify(greeting)
    except Exception as exc:
      return exc, 5