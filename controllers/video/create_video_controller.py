from flask import make_response, request

from app import app
from services.Videos.create_video_service import create_video_service
from utils.get_youtube_video_metadata import get_youtube_video_metadata


@app.route("/videos", methods=["POST"])
def create_video_controller():
	"""
		    Create a new video
		    ---
		    parameters:
		      - name: body
		        in: body
		        required: true
		        schema:
		          type: object
		          properties:
		            id:
		              type: string
		    responses:
		      201:
		        description: Video created successfully
		      404:
		        description: Video not found
		      409:
		        description: Video already exists
		    """

	data = request.json
	id = data.get("id")

	if not id:
		return make_response({"message": "Video-Id not specified", "status": 400}, 400)

	video_data = get_youtube_video_metadata(id)

	if not video_data:
		return make_response({"message": f"Video with id = {id}, not found", "status": 404})

	video = create_video_service(id=video_data["id"], title=video_data["title"], duration=video_data["duration"],
								 channel=video_data["channel"])

	if not video:
		return make_response({"status": 409, "message": f"Video with id = {id}, already exists"}, 409)

	return make_response({"status": 201}, 201)
