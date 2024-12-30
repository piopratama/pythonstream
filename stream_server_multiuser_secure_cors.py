from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import jwt
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

SECRET_KEY = "my_secret_key"

def generate_stream(user_id):
    """Simulate streaming data chunk by chunk for a specific user."""
    chunks = [
        f"Hello {user_id}, this is the first chunk of your data.\n",
        f"Here is the second chunk for {user_id}.\n",
        f"And finally, this is the last chunk for {user_id}.\n"
    ]
    for chunk in chunks:
        time.sleep(1)  # Simulate delay between chunks
        yield chunk  # Send chunk to the client

@app.route('/stream', methods=['GET'])
def stream():
    """Secure streaming endpoint."""
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Authorization header missing"}), 401

    token = auth_header.split(" ")[1]  # Extract the token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        return Response(generate_stream(user_id), content_type='text/plain')
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

@app.route('/generate_token', methods=['POST'])
def generate_token():
    """Generate a JWT for a user."""
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    token = jwt.encode({
        "user_id": user_id,
        "exp": time.time() + 60  # Token expires in 60 seconds
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({"token": token})

if __name__ == "__main__":
    app.run(debug=True)
