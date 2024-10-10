from typing import Literal, Dict

from database import db


class Video(db.Model):
	id = db.Column(db.String(11), primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	duration = db.Column(db.String(10), nullable=False)
	channel = db.Column(db.String(80), nullable=False)

	def to_json(self) -> Dict[Literal["id", "title", "channel", "duration"], str]:
		return {
			"id": self.id,
			"title": self.title,
			"channel": self.channel,
			"duration": self.duration
		}
