import os

from flask import Flask

from database import db, init_db

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

db.init_app(app)

with app.app_context():
	init_db(db)

	import controllers

	controllers
