from flask import Flask, Response
import time

app = Flask(__name__)

def generate_stream():
    """Simulate streaming of data chunk by chunk."""
    chunks = [
        "Hello, this is the first chunk of data.\n",
        "Here is the second chunk.\n",
        "And finally, this is the last chunk.\n"
    ]
    for chunk in chunks:
        time.sleep(1)  # Simulate delay between chunks
        yield chunk  # Send chunk to the client

@app.route('/stream')
def stream():
    """Endpoint to stream data to the client."""
    return Response(generate_stream(), content_type='text/plain', headers={
        "Transfer-Encoding": "chunked"  # Enable HTTP chunked transfer
    })

if __name__ == "__main__":
    app.run(debug=True)
