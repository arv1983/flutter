from flask import Flask, request, jsonify
from config.db import db
from sqlalchemy import Column, Date, ForeignKey, String, Integer, Float
from sqlalchemy.sql.sqltypes import DateTime

class ProductModel (db.Model):
    __tablename__ = "product"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    item_description = Column('item_description', String(255), nullable=False)
    item_prince = Column('item_prince', Float, nullable=False)
