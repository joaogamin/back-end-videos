from models.video import Video


def get_all_videos_service() -> list[Video]:
	videos = Video.query.all()

	return videos
