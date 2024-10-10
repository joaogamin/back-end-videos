from sqlalchemy import Delete

from database import db
from models.video import Video


def delete_video_service(id: str) -> bool:
	video_exists = Video.query.get(id)

	if not video_exists:
		return False

	db.session.execute(Delete(Video).where(Video.id == id))
	db.session.commit()

	return True
