from flask import Flask
from flask_sqlalchemy  import  SQLAlchemy

db =  SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    
    db.init_app(app)
    
    
    from app.Routes import libro_routes, categoria_routes
    app.register_blueprint(libro_routes.dp)
    app.register_blueprint(categoria_routes.dp)
    
    
    return app
    
