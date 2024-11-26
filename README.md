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
Replace <name> with any name you want to pass. The response will be a JSON object:
```bash
{
  "name": "<name>"
}
```

## Pulling DockerImage

The application is also Dockerized to make it easy to deploy anywhere.

### 1. To pull the Docker image, use the following command:
```bash
docker pull talha213/flask-api
```

### 2. Running the Docker Container
After pulling the image, you can run the container with:
```bash
docker run -d -p 80:80 talha213/flask-api
```
the app will be accessible at http://localhost:5000.

### 3. Test the API
You can test the API by sending a GET request to:
```bash
http://localhost:80/api/<name>
```

## **About Me**  

Hi! I'm [Talha](https://github.com/anonymous298), a passionate developer and tech enthusiast focused on building impactful projects. I specialize in **AI/ML**, and crafting efficient solutions for complex problems.  

### **Skills**  
- 🧠 Artificial Intelligence & Machine Learning  
- 💻 Web Development (Frontend & Backend)  
- 📊 Data Analysis & Visualization  

### **Connect with Me**  
- [GitHub](https://github.com/anonymous298)  
- [LinkedIn](https://linkedin.com/in/muhmmad-talha937/)
