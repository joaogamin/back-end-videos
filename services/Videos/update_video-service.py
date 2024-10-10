from sqlalchemy import update

from database import db
from models.video import Video


def update_video_service(id: str, video: Video) -> None | Video:
	video_exists = Video.query.get(id)

	if not video_exists:
		return None

	new_video_already_exists = Video.query.get(video.id)

	if new_video_already_exists:
		return None

	updated_video = db.session.execute(update(Video).where(Video.id == id).values(
		id=video.id,
		channel=video.channel,
		duration=video.duration,
		title=video.title
	))
	db.session.commit()
	return updated_video
