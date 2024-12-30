# HTTP/1.1 Streaming Project

This project is designed to demonstrate the concept of **streaming between a client and a server** using **HTTP/1.1 chunked transfer encoding**. It includes step-by-step examples that build upon each other, starting with basic streaming and progressing to more advanced multi-user and secure implementations. Each step introduces new concepts to help understand how streaming works and its applications.

## **Concept: HTTP/1.1 Streaming**
Streaming in HTTP/1.1 uses **chunked transfer encoding**, a feature that allows the server to send data incrementally as it becomes available, rather than waiting for the entire response to be ready. This enables:

- **Real-time updates**: The client can start processing data as it arrives.
- **Improved performance**: Reduces server memory usage for large responses.
- **Better user experience**: The client sees results immediately without waiting for the full response.

### **Key Features of HTTP/1.1 Streaming**
- **Chunked Transfer Encoding**: Data is sent in chunks, with each chunk preceded by its size in hexadecimal format.
- **Persistent Connection**: The server keeps the connection open until all chunks are sent.
- **Use Cases**: Live data feeds, token-by-token text generation, chat applications, and real-time dashboards.

---

## **Project Structure**

```
streaming-project/
├── stream_server.py               # Basic single-user streaming example
├── stream_client.py               # Basic client to consume the stream
├── stream_server_multiuser.py     # Multi-user streaming example
├── stream_client_multiuser.py     # Client for multi-user streaming
├── stream_server_multiuser_secure.py # Secure multi-user streaming with JWT
├── stream_client_multiuser_secure.py # Secure client with JWT authentication
├── requirements.txt               # Dependencies
├── README.md                      # Project documentation
```

---

## **Examples**

### **1. Single-User Streaming**
- **Files**: `stream_server.py` and `stream_client.py`
- **Description**: Demonstrates the basic concept of streaming data from a server to a single client using HTTP/1.1 chunked transfer encoding.

#### **Run Instructions**
1. Start the server:
   ```bash
   python stream_server.py
   ```
2. Start the client:
   ```bash
   python stream_client.py
   ```

#### **Concepts Covered**
- Sending chunks of data from the server to the client.
- Maintaining a persistent connection until the stream is complete.

---

### **2. Multi-User Streaming**
- **Files**: `stream_server_multiuser.py` and `stream_client_multiuser.py`
- **Description**: Builds on the basic example by supporting multiple users. The server personalizes streams for each user based on their unique identifier.

#### **Run Instructions**
1. Start the server:
   ```bash
   python stream_server_multiuser.py
   ```
2. Start the client:
   ```bash
   python stream_client_multiuser.py
   ```

#### **Concepts Covered**
- Handling multiple concurrent connections.
- Personalizing streams based on user-specific data.

---

### **3. Secure Multi-User Streaming**
- **Files**: `stream_server_multiuser_secure.py` and `stream_client_multiuser_secure.py`
- **Description**: Introduces security using JWT tokens for authentication. The server validates the token before streaming data personalized to the authenticated user.

#### **Run Instructions**
1. Start the server:
   ```bash
   python stream_server_multiuser_secure.py
   ```
2. Generate a token for a user:
   ```bash
   curl -X POST http://127.0.0.1:5000/generate_token -H "Content-Type: application/json" -d '{"user_id": "User1"}'
   ```
3. Use the client to stream data:
   ```bash
   python stream_client_multiuser_secure.py
   ```

#### **Concepts Covered**
- Authenticating users using JWT.
- Securing streaming endpoints to prevent unauthorized access.

---

## **Requirements**

To run the project, you need:

- Python 3.x
- Libraries listed in `requirements.txt`:
  ```plaintext
  Flask==2.2.5
  PyJWT==2.7.0
  requests==2.31.0
  ```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **How Streaming Works in Each Example**

### **1. Basic Streaming**
- **Server**: Uses a generator to send chunks of data incrementally to the client.
- **Client**: Processes each chunk as it arrives, providing real-time updates.

### **2. Multi-User Streaming**
- **Server**: Tracks each user’s request and personalizes the response.
- **Client**: Sends a unique user identifier to receive personalized data.

### **3. Secure Streaming**
- **Server**: Validates JWT tokens to authenticate users before streaming.
- **Client**: Retrieves a token and includes it in the request headers for secure communication.

---

## **Next Steps**
- Add **HTTPS** to encrypt data in transit.
- Implement **token refresh** for long-lived sessions.
- Use **WebSockets** for bidirectional streaming.

---

## **Contributing**
Feel free to fork the repository and submit pull requests with improvements or new examples!

---

## **License**
This project is licensed under the MIT License.

