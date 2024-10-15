from app import db

class Libro (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(255), nullable=False)
    