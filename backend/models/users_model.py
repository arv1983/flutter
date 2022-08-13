from config.db import db
from sqlalchemy import Column, String, Integer,DateTime
from sqlalchemy.sql.sqltypes import Date
from flask_jwt_extended import create_access_token
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

@dataclass
class UsersModel (db.Model):
    __tablename__ = "user"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    email = Column('email', String(255), nullable=False)
    password = Column('password', String(255), nullable=False)
    created_at = Column('created_at', DateTime)

    
    @property
    def password(self):
        return {"Error password cannot be accessed"}
    @password.setter
    def password(self, password):
        self.senha = generate_password_hash(password=password, salt_length=10)

    def check_password(self, password_compare):
        return check_password_hash(self.senha, password_compare)


    def serialized(self):
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
        }
        
        return data

    def login():
        
        users = []
        for user in UsersModel().query.all():
            users.append(UsersModel.serialized(user))
        return users


    def get_user_by_id(id: str):

        user = UsersModel.query.filter_by(id=id).first()

        return user

    
