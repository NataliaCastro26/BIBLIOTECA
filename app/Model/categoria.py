from app import db

class Categoria (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    libro = db.Column(db.Integer, db.ForeignKey('libro.id'))
    