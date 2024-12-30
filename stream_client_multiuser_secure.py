import requests

BASE_URL = "http://127.0.0.1:5000"

def get_token(user_id):
    """Retrieve a JWT token for the specified user."""
    response = requests.post(f"{BASE_URL}/generate_token", json={"user_id": user_id})
    if response.status_code == 200:
        return response.json()["token"]
    else:
        print(f"Failed to get token for {user_id}: {response.json()['error']}")
        return None

def stream_data(user_id):
    """Consume the secure streaming API."""
    token = get_token(user_id)
    if not token:
        return

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/stream", headers=headers, stream=True)

    if response.status_code == 200:
        print(f"Streaming data for {user_id}:\n")
        for chunk in response.iter_content(chunk_size=None):
            print(chunk.decode('utf-8'), end="")
        print("\n")
    else:
        print(f"Failed to stream data for {user_id}: {response.json()['error']}")

if __name__ == "__main__":
    user_ids = ["User1", "User2"]
    for user_id in user_ids:
        stream_data(user_id)
        print("\n" + "-" * 50 + "\n")  # Separate output for different users
