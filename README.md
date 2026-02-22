[![DOI](https://zenodo.org/badge/909941984.svg)](https://doi.org/10.5281/zenodo.18732285)

# HTTP/1.1 Streaming Project

This project is designed to demonstrate the concept of streaming between a client and a server using HTTP/1.1 chunked transfer encoding. It includes step-by-step examples that build upon each other, starting with basic streaming and progressing to more advanced multi-user and secure implementations.

## Concept: HTTP/1.1 Streaming

Streaming in HTTP/1.1 uses chunked transfer encoding, which allows the server to send data incrementally instead of waiting for the entire response to be ready.

This enables:

- Real-time updates
- Improved performance
- Better user experience

### Key Features

- Chunked Transfer Encoding
- Persistent HTTP connection
- Real-time streaming use cases

---

## Project Structure

```
streaming-project/
├── stream_server.py
├── stream_client.py
├── stream_server_multiuser.py
├── stream_client_multiuser.py
├── stream_server_multiuser_secure.py
├── stream_client_multiuser_secure.py
├── requirements.txt
├── README.md
```

---

## Examples

### 1. Single-User Streaming

Files:
- stream_server.py
- stream_client.py

Run:

```bash
python stream_server.py
```

```bash
python stream_client.py
```

Concepts:
- Generator-based streaming
- Persistent connection

---

### 2. Multi-User Streaming

Files:
- stream_server_multiuser.py
- stream_client_multiuser.py

Run:

```bash
python stream_server_multiuser.py
```

```bash
python stream_client_multiuser.py
```

Concepts:
- Concurrent connections
- Personalized streams

---

### 3. Secure Multi-User Streaming

Files:
- stream_server_multiuser_secure.py
- stream_client_multiuser_secure.py

Run server:

```bash
python stream_server_multiuser_secure.py
```

Generate token:

```bash
curl -X POST http://127.0.0.1:5000/generate_token \
-H "Content-Type: application/json" \
-d '{"user_id": "User1"}'
```

Run client:

```bash
python stream_client_multiuser_secure.py
```

Concepts:
- JWT authentication
- Secure streaming endpoints

---

## Requirements

Python 3.x

Dependencies:

```
Flask==2.2.5
PyJWT==2.7.0
requests==2.31.0
```

Install:

```bash
pip install -r requirements.txt
```

---

## How Streaming Works

Basic:
- Server yields chunks.
- Client processes incrementally.

Multi-user:
- Server personalizes response per user.

Secure:
- JWT token validation before streaming.

---

## Citation

If you use this project in academic work, please cite:

Pratama, I. W. P. (2026). HTTP/1.1 Streaming Project [Software]. https://doi.org/10.5281/zenodo.18732285

---

## License

This project is licensed under the MIT License.
