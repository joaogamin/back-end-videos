import os
from typing import Dict, Literal

import requests

from utils.convert_duration import convert_duration


def get_youtube_video_metadata(video_id: str) -> Dict[Literal["id", "title", "channel", "duration"], str] | None:
	if not video_id:
		return

	apiKey = os.getenv("GOOGLE_API_KEY")

	apiUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id=' + video_id + '&key=' + apiKey

	response = requests.get(apiUrl).json()

	if response['pageInfo']["totalResults"] < 1:
		return

	video_info: str = response['items'][0]
	duration: str = video_info['contentDetails']['duration']
	channel: str = video_info['snippet']['channelTitle']
	title: str = video_info['snippet']['title']
	id: str = video_info['id']

	return {
		"duration": convert_duration(duration), "channel": channel, "title": title, "id": id
	}
