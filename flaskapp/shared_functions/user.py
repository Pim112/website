from database.setupDatabase import User, db


def get_user_from_name(name) -> User:
    return User.query.filter_by(username=name).first()


def check_if_user_exists(email) -> User:
    return User.query.filter_by(email=email).first()


def get_all_users_with_except(exception) -> []:
    return db.session.query(User).filter(User.username != exception).all()


def get_user_from_id(id) -> User:
    return User.query.filter_by(id=id).first()


def parse_user(user) -> {}:
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email_address
    }
