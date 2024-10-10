from database import db


class Video(db.Model):
	id = db.Column(db.String(11), primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	duration = db.Column(db.String(10), nullable=False)
	channel = db.Column(db.String(80), nullable=False)
