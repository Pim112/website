from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def testdb():
    return '<h1>hello world.</h1>'


if __name__ == '__main__':
    app.run()
