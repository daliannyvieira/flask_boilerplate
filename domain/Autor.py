from application.App import db

class Autor(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
    return '<Autor %r>' % self.username

  def to_json(self):
    return {
      'id': self.id,
      'nome': self.username,
      'email': self.email
    }

class AllAutores():
  @staticmethod
  def read_autor():
    try:
      autores = db.session.query(Autor).all()
      autores_lista = []
      for autor in autores:
        autores_lista.append(autor.to_json())
      return autores_lista
    except:
      raise

  @staticmethod
  def create_autor(attributes):
    try:
      new_autor = Autor()
      new_autor.username = attributes['username']
      new_autor.email = attributes['email']
      db.session.add(new_autor)
      db.session.commit()
      return new_autor.to_json()
    except:
      raise