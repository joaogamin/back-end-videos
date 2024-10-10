from models.video import Video


def get_video_by_id_service(id: str) -> None | Video:
	video = Video.query.get(id)

	return video
