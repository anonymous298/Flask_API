# Simple Flask API - Dynamic Name Input

This is a basic Flask API that takes a name dynamically via the URL and returns the name in a JSON response.

## Features:
- **Dynamic Input**: The API accepts a name as part of the URL and returns the name in JSON format.
- **JSON Response**: The name is returned as a JSON object, making it easy to use in various applications.
- **Dockerized**: The Flask app is containerized using Docker, enabling easy deployment anywhere.
- **Docker Hub**: The Docker image has been pushed to Docker Hub, making it easy for others to pull and use.

## Requirements
- Docker (for containerization and easy deployment)
- Python (for local development)
- Flask (for building the API)

## Installation and Running Locally

### 1. Clone the Repository
  ```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Install Dependencies
Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Running the Flask App Locally
Once the dependencies are installed, run the Flask app with:
```bash
python app.py
```
The app will be accessible at http://127.0.0.1:80.

### 4. Test the API
You can now test the API by sending a GET request to:
```bash
http://127.0.0.1:80/api/<name>
```
