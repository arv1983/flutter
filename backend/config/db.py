from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from models.users_model import UsersModel
    from models.cart_model import CartModel
    from models.products_model import ProductModel
    
    with app.app_context():
        db.drop_all()
        db.create_all()
