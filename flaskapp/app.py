import os
import pathlib

from dotenv import dotenv_values
from flask_cors import CORS
from database.setupDatabase import app
from routes.auth import auth

current_file_path = pathlib.Path(__file__).parent.resolve()
env_file_path = os.path.join(current_file_path, '.env')
env_values = dotenv_values(env_file_path)

CORS(app)
app.register_blueprint(auth, url_prefix="/api")


if __name__ == '__main__':
    app.run()
