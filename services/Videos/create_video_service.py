from database import db
from models.video import Video


def create_video_service(id: str, title: str, duration: str, channel: str) -> Video | None:
	video_already_exists = Video.query.get(id)

	if video_already_exists:
		return None

	video = Video(id=id, title=title, duration=duration, channel=channel)

	db.session.add(video)
	db.session.commit()

	return video
