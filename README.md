# 🧮 Flask Calculator DevOps Project

A simple **Flask-based calculator web application** containerized using **Docker** and deployed using **Kubernetes (Minikube)**.  
This project demonstrates a basic **DevOps workflow** including application development, containerization, and deployment.

---

## 📌 Project Overview

This application allows users to enter mathematical expressions such as:

```
10 + 5
```

and instantly receive the calculated result.

The goal of this project is to demonstrate how a simple application can be deployed using modern DevOps tools.

The project includes:

- Python backend development using Flask
- Web interface for user interaction
- REST API for performing calculations
- Docker containerization
- Kubernetes deployment using Minikube
- Source code management using Git and GitHub

---

## ⚙️ Technologies Used

- 🐍 Python – Backend programming  
- 🌶 Flask – Web application framework  
- 🔐 Flask-CORS – Cross-origin request support  
- 🐳 Docker – Containerization  
- ☸ Kubernetes – Container orchestration  
- 🧪 Minikube – Local Kubernetes cluster  
- 🔧 Git – Version control  
- 🌍 GitHub – Code hosting and project management  

---

## ✨ Features

- Web-based calculator interface  
- REST API for performing calculations  
- Supports arithmetic operations:

```
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
```

- Error handling for invalid expressions  
- Division-by-zero protection  
- Containerized using Docker  
- Deployable using Kubernetes  

---

## 📂 Project Structure

```
flask-calculator-devops-project
│
├── app.py
├── Dockerfile
├── requirements.txt
├── deployment.yaml
├── service.yaml
├── .gitignore
└── README.md
```

---

## 🌐 Application Interface

The application provides a simple web interface where users can enter expressions such as:

```
10 + 5
20 * 3
15 - 7
10 / 2
```

The result is displayed immediately on the screen.

---

## 🔗 API Endpoints

### Home Page

```
GET /
```

Displays the calculator web interface.

---

### Calculate Endpoint

```
POST /calculate
```

Example request:

```
{
  "expression": "10 + 5"
}
```

Example response:

```
{
  "result": 15
}
```

Example error response:

```
{
  "error": "Division by zero is not allowed"
}
```

---

## 💻 Running the Application Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the Flask application:

```
python app.py
```

Open browser:

```
http://localhost:5000
```

---

## 🐳 Docker Setup

Build Docker image:

```
docker build -t calculator .
```

Run Docker container:

```
docker run -p 5000:5000 calculator
```

Access application:

```
http://localhost:5000
```

---

## ☸ Kubernetes Deployment

Start Minikube:

```
minikube start
```

Deploy application:

```
kubectl apply -f deployment.yaml
```

Create service:

```
kubectl apply -f service.yaml
```

Check running pods:

```
kubectl get pods
```

Access application:

```
minikube service calculator-service
```

---

## 🏗 DevOps Architecture

```
User Browser
      ↓
Flask Calculator Application
      ↓
Docker Container
      ↓
Docker Hub
      ↓
Kubernetes Deployment
      ↓
Minikube Cluster
```

---

## 🚀 Future Improvements

- Add CI/CD pipeline using GitHub Actions  
- Deploy application to cloud Kubernetes clusters (AWS EKS / GCP GKE)  
- Add advanced UI using React  
- Add automated testing  
- Implement monitoring using Prometheus and Grafana  

---

## 👩‍💻 Author

**Manjushree Bhandary**

GitHub Repository:

```
https://github.com/manju0301/flask-calculator-devops-project
```

---

## ⭐ DevOps Skills Demonstrated

- Python Backend Development  
- Docker Containerization  
- Kubernetes Deployment  
- API Development  
- Git Version Control  
- DevOps Workflow Implementation
