from models import Token, User
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from hashlib import md5
app_auth = Blueprint('app_auth', __name__)
@app_auth.route('/auth', methods=['POST'])
def auth():
    params = request.get_json() # Dict
    email = params['email']
    password = md5(params['password']).hexdigest()

    try:
        user = User.get(User.email == email)
        if user.password == password:
            try:
                token = Token.get(Token.user_id == user.id)
                print token.token
                return jsonify({'TOKEN': 'Token does exist'  }), 201
            except:
                token_created = md5(str(user.id) + user.email).hexdigest()
                print token_created
                print user.id
                query = Token.create(token=token_created, user_id=user.id)
                query.save()
                return jsonify({'data': model_to_dict(query) }), 201
        else:
            return jsonify({'PASSWORD': 'Password is invalid'  }), 201
    except:
        return jsonify({'CONNECT': 'User does not exist'  }), 404

