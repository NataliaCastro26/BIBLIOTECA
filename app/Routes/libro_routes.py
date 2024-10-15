from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.Model.libro import Libro  # Asegúrate de que sea app.Models
from app.Model.categoria import Categoria
from app import db


dp = Blueprint('libro', __name__)  # Cambiado a 'libro' para consistencia

@dp.route('/', methods=['GET'])
def index():
    data = Libro.query.all()
    return render_template('libros/index.html', data=data)

@dp.route('/Inicio', methods=['GET'])
def inicio():
    data = Libro.query.all()
    return render_template('libros/inicio.html', libros=data)  # Cambiado a 'libros=data'

@dp.route('/libro/add', methods=['GET', 'POST'])  # Cambiado a minúsculas
def add():
    if request.method == 'POST':
        print(request.form)  # Agrega esta línea para depuración
        titulo = request.form['titulo']
        genero = request.form['genero']
        
        new_libro = Libro(titulo=titulo, genero=genero)
        db.session.add(new_libro)
        db.session.commit()
        
        return redirect(url_for('libro.inicio'))  # Asegúrate de que esto sea correcto
    
    # Obtener todas las categorías para pasarlas a la plantilla
    categorias = Categoria.query.all()  # Asegúrate de que esto esté correcto
    print(categorias)  # Agrega esta línea para depuración
    return render_template('libros/add.html', categorias=categorias)



@dp.route('/libro/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    libro = Libro.query.get_or_404(id)  # Corregido de get_or_040 a get_or_404
    
    if request.method == 'POST':  # Corregido de 'merhod' a 'method'
        libro.titulo  = request.form['titulo']
        libro.genero  = request.form['genero']
        db.session.commit()
        return redirect(url_for('libro.inicio'))  # Cambiado a 'libro.index'
    
    return render_template('libros/edit.html', libro=libro)  # Pasar el libro a la plantilla
    
    
        
        
        
@dp.route('/libro/delete/<int:id>', methods=['POST'])  
def delete(id):
    libro = Libro.query.get_or_404(id)
    
    db.session.delete(libro)
    db.session.commit()
    
    return redirect(url_for('libro.inicio'))  # Cambiado a 'libro.index'

