from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def hello_world():
	res = make_response({"status": 200, "message": "Hello World!"}, 200)
	
	return res
