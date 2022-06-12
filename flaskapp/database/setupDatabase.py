import os
import pathlib

from dotenv import dotenv_values
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

current_file_path = pathlib.Path(__file__).parent.resolve()
env_file_path = os.path.join(current_file_path, '../.env')
env_values = dotenv_values(env_file_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env_values['db_uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt_manager = JWTManager(app)
app.secret_key = 'super_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(125), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


def main():
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    main()
