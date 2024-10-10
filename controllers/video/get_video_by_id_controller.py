from flask import make_response

from app import app
from services.Videos.get_video_by_id_service import get_video_by_id_service


@app.route('/videos/<video_id>', methods=["GET"])
def get_video_by_id_controller(video_id):
	"""
		    Get a video by ID
		    ---
		    parameters:
		      - name: video_id
		        in: path
		        type: string
		        required: true
		    responses:
		      200:
		        description: Video found
		        schema:
		          type: object
		          properties:
		            status:
		              type: integer
		              example: 200
		            video:
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
		      404:
		        description: Video not found
		    """
	
	video = get_video_by_id_service(video_id)

	if not video:
		res = make_response({"status": 404, "message": f"Video with id = {video_id}, not found"})
		res.status_code = 200

		return res

	res = make_response({"status": 200, "video": video.to_json()})
	res.status_code = 200

	return res
