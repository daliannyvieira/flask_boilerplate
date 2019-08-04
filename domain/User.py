from application.App import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
    return '<User %r>' % self.username

  def to_json(self):
    return {
      'id': self.id,
      'username': self.username,
    }

class AllUsers():
  @staticmethod
  def read_all():
    try:
      users = db.session.query(User).all()
      users_lista = []
      for user in users:
        users_lista.append(user.to_json())
      return users_lista
    except:
      raise