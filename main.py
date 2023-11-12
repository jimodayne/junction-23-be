import src
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()


app = Flask(__name__)
cors = CORS(app)
# app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/api/chatbot", methods=["POST"])
def route():
    if request.method != "POST":
        return jsonify(
            isError=True,
            message="Method not supported. Must be GET",
            statusCode=405,
        )

    d = request.get_json()

    if "message" not in d:
        return jsonify(
            isError=True,
            message="JSON must have 'message' key",
            statusCode=405,
        )

    message = d["message"]

    # Start processing
    response = src.process(message)
    response = jsonify(response)
    # response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
