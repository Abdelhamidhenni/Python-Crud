from flask import Flask, jsonify, request
from models import User
from playhouse.shortcuts import model_to_dict
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/work')#DECORATEUR
def work_app():
	return 'Ici ca taff'

@app.route('/posts', methods=['GET'])
def posts():
	return jsonify({'data': list(User.select().dicts())}), 201

@app.route('/posts', methods=['POST'])
def posts_new():
	params = request.get_json() #dict
	charlie = User.create(email=params['email'], password=params['password'])
	charlie.save()
	return jsonify({'data': model_to_dict(charlie) }), 201

if __name__ == "__main__":
	app.run(debug=True, port=5000)