from models import Token, User, Trans
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
app_trans = Blueprint('app_trans', __name__)
@app_trans.route('/trans', methods=['POST'])
def trans():
    params = request.get_json() # Dict
    token = params['token']
    user_recepteur = params['user_recepteur']
    amount = params['amount']
    try:
        verification = Token.get(Token.token  == token)
        if verification.token == token:
            print token
            user_emeteur = verification.user_id
            print user_recepteur
            print user_emeteur
            trans = Trans.create(user_emeteur = user_emeteur, user_recepteur = user_recepteur, amount = amount)
            trans.save()
            return jsonify({'data': model_to_dict(trans) }), 201
            #return jsonify({'TOKEN': 'Token does exist'}), 201
        else:
            return jsonify({'TOKEN': 'Token does NOT exist'}), 403
    except Exception, e:
        print e
        return jsonify({'TOKEN': 'You need to give params'}), 404