from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from hashlib import md5
from models import User

app_user = Blueprint('app_user', __name__)

@app_user.route('/user', methods=['GET'])
def posts():
	return jsonify({'data': list(User.select().dicts())}), 201

@app_user.route('/user', methods=['POST'])
def new_user():
	params = request.get_json() #dict
	charlie = User.create(email=params['email'], password=md5(params['password']).hexdigest())
	charlie.save()
	return jsonify({'data': model_to_dict(charlie) }), 201

@app_user.route('/user/<id>', methods=['PUT'])
def update_user(id):
	params = request.get_json() #dict
	charlie = User.get(id=id)
	charlie.email = params['email']
	charlie.password = params['password']
	charlie.save()#recree luser sil n'existe pas
	return jsonify({'data': model_to_dict(charlie) }), 201

@app_user.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
	q = User.delete().where(User.id == id)
	q.execute()  # remove the rows
	return jsonify({'data': True }), 201