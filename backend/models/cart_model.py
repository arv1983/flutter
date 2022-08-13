from flask import Flask, request, jsonify
from config.db import db
from sqlalchemy import Column, Date, ForeignKey, String, Integer, Float
from sqlalchemy.sql.sqltypes import DateTime


class CartModel (db.Model):
    __tablename__ = "cart"
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('user.id'), nullable=False)
    product_id = Column('product_id', ForeignKey('product.id'), nullable=False)
    qty = Column('qty', Float, nullable=False)

    
