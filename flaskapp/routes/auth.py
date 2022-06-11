import hashlib
import json
from flask import Blueprint, request, jsonify
from shared_functions.user import check_if_user_exists, get_all_users_with_except, parse_user, get_user_from_id
from database.setupDatabase import User, db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

auth = Blueprint('auth', __name__)

LOGGED_IN_USERS = []


@auth.route('/login', methods=['POST'])
def login():
    post_request = request.get_json()

    if post_request is not None and 'email' and 'password' in post_request:
        email = post_request['email']
        password = post_request['password']
        user = check_if_user_exists(email)

        if user and user.password == get_password_hash(password):
            access_token = create_access_token(identity=email)
            LOGGED_IN_USERS.append(access_token)
            return jsonify(access_token=access_token), 200

        return 'Username or password is incorrect', 404

    return 'Request was either missing username or password', 400


@auth.route('/signup', methods=['POST'])
def signup():
    post_request = request.get_json()

    if post_request is not None and 'username' and 'password' and 'email' in post_request:
        if not post_request['username'] or not post_request['password'] or not post_request['email']:
            return "One or more required fields were empty", 401

        username = post_request['username']
        user_exists = check_if_user_exists(username)
        if user_exists:
            return "User does already exist", 400

        password_plain = post_request['password']
        email = post_request['email']
        password = get_password_hash(password_plain)

        new_user = User(username, password, email)
        db.session.add(new_user)
        db.session.commit()

        return "User successfully saved", 200

    return "Required fields are missing", 400


@auth.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    jwt = request.headers.get('Authorization').split(' ')[1]

    if jwt in LOGGED_IN_USERS:
        LOGGED_IN_USERS.remove(jwt)
        return "logged out", 200

    return "User is not logged in", 401


@auth.route('/user', methods=['GET'])
@jwt_required()
def get_current_user():
    user = check_if_user_exists(get_jwt_identity())

    return jsonify(parse_user(user)), 200


@auth.route('/userById', methods=['POST'])
def get_user_by_id():
    post_request = request.get_json()
    if post_request is not None and 'id' in post_request:
        user_id = post_request['id']
        if user_id:
            user = get_user_from_id(user_id)
            if user:
                return jsonify(parse_user(user)), 200
            return "User not found", 404
    return "no id in body", 400


@auth.route('/users', methods=['GET'])
@jwt_required()
def get_all_users_except_logged_in():
    output = []
    users = get_all_users_with_except(get_jwt_identity())

    for user in users:
        to_serialize = check_if_user_exists(user.username)
        output.append(parse_user(to_serialize))

    return jsonify(output), 200


def get_password_hash(password: str) -> str:
    encoded_password = password.encode()
    hashed_pass = hashlib.sha256(encoded_password)
    return hashed_pass.hexdigest()
