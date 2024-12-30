import requests

def stream_data():
    """Consume the streaming API and process data chunk by chunk."""
    url = 'http://127.0.0.1:5000/stream'
    response = requests.get(url, stream=True)  # Enable streaming mode

    print("Streaming data from server:\n")
    for chunk in response.iter_content(chunk_size=None):  # Read each chunk as it arrives
        print(chunk.decode('utf-8'), end="")  # Decode and print each chunk

if __name__ == "__main__":
    stream_data()
