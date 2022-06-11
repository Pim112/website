from flask import Blueprint, request, jsonify, session

auth = Blueprint('auth', __name__)

LOGGED_IN_USERS = []

@auth.route('/login', methods=['POST'])
def login():
    post_request = request.get_json()

    if post_request is not None and 'username' and 'password' in post_request:
        username = post_request['username']
        password = post_request['password']
        user = check_if_user_exists(username)

        if user and user.password == get_password_hash(password):
            access_token = create_access_token(identity=username)
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

        preferences = Preferences(None, None, None, None, None, None)
        db.session.add(preferences)
        db.session.commit()

        new_user = User(username, password, email, preferences.id)
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