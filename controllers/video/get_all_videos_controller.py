from flask import make_response

from app import app
from services.Videos.get_all_videos_service import get_all_videos_service


@app.route("/videos", methods=["GET"])
def get_all_videos_controller():
	"""
		    Get all videos
		    ---
		    responses:
		      200:
		        description: A list of videos
		        schema:
		          type: object
		          properties:
		            status:
		              type: integer
		              example: 200
		            videos:
		              type: array
		              items:
		                type: object
		                properties:
		                  id:
		                    type: string
		                  title:
		                    type: string
		                  channel:
		                    type: string
		                  duration:
		                    type: string
		    """
	
	videos = get_all_videos_service()

	videos_json = []

	for video in videos:
		videos_json.append(video.to_json())

	res = make_response({"status": 200, "videos": videos_json})
	res.status_code = 200

	return res
