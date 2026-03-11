# Calculator DevOps Project

This project is a simple **Python Flask Calculator API** that is containerized using **Docker** and deployed using **Kubernetes (Minikube)**.  
It demonstrates a basic **DevOps workflow** from application development to containerization and deployment.

## 🚀 Technologies Used

- Python (Flask)
- Docker
- Kubernetes
- Minikube
- Git & GitHub

## 📌 Features

- REST API for performing calculator operations
- Docker containerization
- Kubernetes deployment with multiple replicas
- Kubernetes service exposure
- Local Kubernetes cluster using Minikube

## 📂 Project Structure

calculator-devops/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── deployment.yaml
├── service.yaml
├── .gitignore
└── README.md

## 🧮 API Usage

### Home Endpoint

GET /

Returns information about the API.

Example response:

{
  "message": "Calculator API - POST to /calculate with {\"expression\": \"10 + 5\"}"
}

### Calculate Endpoint

POST /calculate

Request body:

{
  "expression": "10 + 5"
}

Example response:

{
  "result": 15
}

---

## 🐳 Docker Setup

Build Docker image:

docker build -t calculator .

Run container:

docker run -p 5000:5000 calculator

---

## ☸ Kubernetes Deployment

Start Minikube:

minikube start

Deploy application:

kubectl apply -f deployment.yaml

Expose service:

kubectl apply -f service.yaml

Check pods:

kubectl get pods

Access service:

minikube service calculator-service

---

## 📈 Future Improvements

- Add CI/CD pipeline using GitHub Actions
- Add frontend UI for calculator
- Deploy to cloud Kubernetes cluster (GKE / EKS / AKS)

---

## 👩‍💻 Author

Manjushree Bhandary
