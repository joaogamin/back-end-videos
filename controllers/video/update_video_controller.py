from flask import make_response, request

from app import app
from models.video import Video
from services.Videos.update_video_service import update_video_service
from utils.get_youtube_video_metadata import get_youtube_video_metadata


@app.route('/videos/<video_id>', methods=["PATCH"])
def update_video_controller(video_id):
	"""
		    Update a video
		    ---
		    parameters:
		      - name: video_id
		        in: path
		        type: string
		        required: true
		      - name: body
		        in: body
		        required: true
		        schema:
		          type: object
		          properties:
		            id:
		              type: string
		              example: "new_id"
		    responses:
		      200:
		        description: Video updated successfully
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
		return make_response({"status": 404, "message": f"Video with id = {id}, not found on youtube"}, 404)

	video = Video(id=video_data["id"], title=video_data["title"], channel=video_data["channel"], duration=["duration"])

	response = update_video_service(video_id, video)

	if response == 404:
		return make_response({"status": 404, "message": f"Video with id = {id}, not found"}, 404)

	if response == 409:
		return make_response({"status": 409, "message": f"Video with id = {id}, already exists"})

	return make_response({"status": 200}, 200)
