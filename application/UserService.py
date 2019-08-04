from flask import jsonify
from flask_restplus import Resource
from application.App import api
from domain.User import AllUsers

@api.route('/user')
class UserService(Resource):
  def get(self):
    try:
      users = AllUsers.read_all()
      return jsonify(users)
    except Exception as exc:
      return exc, 5

  # def post(self):
  #   try:
  #     admin = User(username='admin', email='admin@example.com')
  #     db.session.add(admin)
  #     db.session.commit()
  #     greeting = User.query.order_by(User.username).all()
  #   except Exception as exc:
  #     return exc, 5