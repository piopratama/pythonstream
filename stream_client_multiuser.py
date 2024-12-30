import requests

def stream_data(user_id):
    """Consume the streaming API and process data chunk by chunk."""
    url = f'http://127.0.0.1:5000/stream?user_id={user_id}'  # Include user_id in the request
    response = requests.get(url, stream=True)  # Enable streaming mode

    print(f"Streaming data for {user_id} from server:\n")
    for chunk in response.iter_content(chunk_size=None):  # Read each chunk as it arrives
        print(chunk.decode('utf-8'), end="")  # Decode and print each chunk

if __name__ == "__main__":
    user_ids = ["User1", "User2", "Guest"]  # Example users
    for user_id in user_ids:
        stream_data(user_id)
        print("\n" + "-" * 50 + "\n")  # Separate output for different users
