from flask import Flask, Response, request
import time

app = Flask(__name__)

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
    """Endpoint to stream data to the client."""
    user_id = request.args.get('user_id', 'Guest')  # Get user_id from query params, default to 'Guest'
    return Response(generate_stream(user_id), content_type='text/plain', headers={
        "Transfer-Encoding": "chunked"  # Enable HTTP chunked transfer
    })

if __name__ == "__main__":
    app.run(debug=True)
