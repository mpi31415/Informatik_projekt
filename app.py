import os

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps
from quests import generate_math, generate_quest
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
migrate = Migrate()
cors = CORS(app)

app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key',
    SQLALCHEMY_DATABASE_URI=(
            'sqlite:///' + os.path.join(app.instance_path, 'project.db')),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    CORS_HEADERS='Content-type'
)

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    admin = db.Column(db.Boolean)


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = "ayo"

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], ["HS256"])
            current_user = Users.query.filter_by(public_id=data['public_id']).first()

        except:
            return jsonify({'message': 'token is invalid'})
        return f(current_user, *args, **kwargs)

    return decorator


@app.route('/register', methods=['GET', 'POST'])
@cross_origin()
def signup_user():

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'registered successfully'})


@app.route('/login', methods=['GET', 'POST'])
@cross_origin()
def login_user():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

    user = Users.query.filter_by(name=auth.username).first()

    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        print(token)
        test = token
        return jsonify({'token': token})

    return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})


@app.route('/user', methods=['GET'])
@cross_origin()
def get_all_users():
    users = Users.query.all()

    result = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin

        result.append(user_data)

    return jsonify({'users': result})


@app.route('/get_math', methods=['GET'])
@token_required
@cross_origin()
def generate_maths(current_user):
    return jsonify({'quest': generate_math()})


@app.route('/get_quest', methods=['GET'])
@token_required
@cross_origin()
def generate_quests(current_user):
    return jsonify({'quest': generate_quest()})


@app.route('/')
@cross_origin()
def index():
    return "<h1> Running</h1>"


if __name__ == '__main__':
    print(os.path.join(app.instance_path, 'project.db'))
    # db.init_app(app)
    db.create_all()
    migrate.init_app(app, db)
    app.run(threaded=True, port=5000)
