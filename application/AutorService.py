from flask import jsonify, request
from flask_restplus import Resource
from application.App import api
from domain.Autor import AllAutores, Autor

@api.route('/autor')
class AutorService(Resource):
  def get(self):
    try:
      autores = AllAutores.read_autor()
      return jsonify(autores)
    except Exception as exc:
      return exc, 500

  def post(self):
    try:
      attributes = request.get_json()
      autor = AllAutores.create_autor(attributes)
      autor = jsonify(autor)
      autor.status_code = 201
      return autor
    except Exception as exc:
      return exc, 500