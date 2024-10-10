import os

from flask import Flask, make_response

from database import db, init_db

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

db.init_app(app)

with app.app_context():
	init_db(db)


@app.route("/")
def hello_world():
	res = make_response({"status": 200, "message": "Hello World!"}, 200)

	return res
