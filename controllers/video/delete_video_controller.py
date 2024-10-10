from flask import make_response

from app import app
from services.Videos.delete_video_service import delete_video_service


@app.route('/videos/<video_id>', methods=["DELETE"])
def delete_video_controller(video_id):
	success = delete_video_service(video_id)

	if not success:
		res = make_response({"status": 404, "message": f"Video with id = {video_id}, not found"})
		res.status_code = 404

		return res

	res = make_response({"status": 200})
	res.status_code = 200

	return res
