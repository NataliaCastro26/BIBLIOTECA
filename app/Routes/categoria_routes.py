from flask import Blueprint, render_template, request, redirect, url_for
from app.Model.categoria import Categoria  # Asegúrate de que sea app.Models
from app import db

dp = Blueprint('categoria', __name__)

@dp.route('/categoria', methods=['GET'])
def index():
    categorias = Categoria.query.all()
    return render_template('categorias/index.html', categorias=categorias)



@dp.route('/categoria/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        new_categoria = Categoria(nombre=nombre)
        db.session.add(new_categoria)
        db.session.commit()
        return redirect(url_for('categoria.index'))  # Asegúrate de que sea 'categoria.index'
    
    return render_template('categorias/add.html')




@dp.route('/categoria/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    categoria = Categoria.query.get_or_404(id)
    
    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('categoria.index'))  # Asegúrate de que sea 'categoria.index'
    
    return render_template('categorias/edit.html', categoria=categoria)




@dp.route('/categoria/delete/<int:id>', methods=['POST'])
def delete(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('categoria.index'))  # Asegúrate de que sea 'categoria.index'
