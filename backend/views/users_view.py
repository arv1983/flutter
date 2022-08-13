from flask import Flask, request, jsonify, Blueprint
from config.db import db
from services.mask import Masks
from services.validator import Validator
from models.users_model import UsersModel
from datetime import datetime
bp = Blueprint("user_route", __name__)

@bp.route("/", methods=["GET", "POST"])
def create_or_login():


    if request.method == "POST":
        data = request.get_json()
        
        validator_response = Validator.register_validator(data)
        
        if validator_response:
            return jsonify(validator_response)

        data['created_at'] = datetime.now()

        data_serialized = UsersModel(**data)
        db.session.add(data_serialized)
        db.session.commit()

        return jsonify(UsersModel.serialized(data_serialized)),201

    if request.method == "GET":

        data = UsersModel.login()

        return jsonify(data),200


@bp.route("/id/<int:id>", methods=["GET"])
def get_id(id):

    query = UsersModel.get_user_by_id(str(id))
    if not query:
        return '',404
    
    return jsonify(UsersModel.serialized(query)),200
    

@bp.route("/id/<int:id>", methods=["GET", "DELETE", "PATCH"])
def get_cpf(id):

    
    query = UsersModel.get_user_by_id(str(id))
    if not query:
        return '',404

    if request.method == "GET":
        
        return jsonify(UsersModel.serialized(query)),200

    if request.method == "PATCH":

        data = request.get_json()
        
        data['cpf'] = query.cpf
        data['created_at'] = query.created_at
        data['updated_at'] = datetime.now()

        for key, value in data.items():
            setattr(query, key, value)
        
        db.session.add(query)
        db.session.commit()

        return jsonify(UsersModel.serialized(query)),200
    
    if request.method == "DELETE":

        db.session.delete(query)
        db.session.commit()

        return '',200

        
        














        

    
