# CloudCart – Production-Ready E-Commerce Application on Kubernetes

## 📸 Project Screenshots

![CloudCart Screenshot 1](screenshots/Screenshot%202026-11-21%20160107.png)

![CloudCart Screenshot 2](screenshots/Screenshot%202026-11-21%20160000.png)

![CloudCart Screenshot 3](screenshots/Screenshot%202026-11-21%20160249.png)

![CloudCart Screenshot 4](screenshots/Screenshot%202026-11-21%20160811.png)
CloudCart is a containerized e-commerce web application deployed on a Kubernetes cluster. It demonstrates containerization, CI/CD automation, orchestration, and application monitoring using industry-relevant DevOps tools.

## Project Overview

CloudCart provides a simple e-commerce interface where users can view available products and their prices. The application is built using Flask and deployed using Docker and Kubernetes.

The project also integrates Jenkins for CI/CD automation and Prometheus with Grafana for monitoring.

## Tech Stack

- **Application:** Python, Flask
- **Containerization:** Docker
- **Container Registry:** Docker Hub
- **Orchestration:** Kubernetes
- **CI/CD:** Jenkins
- **Monitoring:** Prometheus, Grafana
- **Version Control:** Git, GitHub
- **Infrastructure:** AWS EC2

## Key Features

- Product listing through a web interface
- REST API for retrieving product information
- Application health-check endpoint
- Prometheus metrics endpoint
- Docker-based application deployment
- Kubernetes deployment with two replicas
- Rolling update deployment strategy
- Readiness and liveness probes
- CPU and memory resource requests and limits
- Automated CI/CD pipeline using Jenkins
- Monitoring dashboards using Grafana

## Application API Endpoints

| Endpoint | Description |
|---|---|
| `/` | CloudCart home page |
| `/api/products` | Returns product information |
| `/health` | Application health status |
| `/metrics` | Prometheus application metrics |

## CI/CD Pipeline

The Jenkins pipeline automates the application delivery process.

1. **Checkout:** Retrieves source code from GitHub.
2. **Docker Build:** Builds the Docker image.
3. **Docker Hub Push:** Pushes the image to Docker Hub.
4. **Kubernetes Deploy:** Updates the Kubernetes deployment.
5. **Rollout Verification:** Checks deployment rollout status.

Latest verified pipeline: Build #8 – Successful.

## Kubernetes Deployment

The application is deployed in a Kubernetes cluster with:

- 2 application replicas
- RollingUpdate strategy
- NodePort service
- Readiness and liveness probes
- Container resource limits
- Non-root container security context

## Monitoring with Prometheus and Grafana

Prometheus collects application and system metrics, while Grafana provides monitoring dashboards.

The CloudCart monitoring dashboard includes:

- Target Health
- CloudCart CPU Usage
- CloudCart Request Rate
- CloudCart Memory Usage

Prometheus monitors both the CloudCart application and its own service.

## Docker Image

`kedarvhanaje/cloudcart:build-8`

Docker Hub: https://hub.docker.com/r/kedarvhanaje/cloudcart

## GitHub Repository

https://github.com/vhanajekedar-tech/-CloudCart

## Learning Outcomes

Through this project, I gained practical experience in:

- Building and containerizing a Flask application
- Deploying applications on Kubernetes
- Creating Jenkins CI/CD pipelines
- Managing Docker images
- Implementing application monitoring
- Working with AWS EC2 and Linux environments

## 👨‍💻 Author

**Kedar Vhanaje**

Cloud Computing & DevOps Enthusiast

- **GitHub:** [vhanajekedar-tech](https://github.com/vhanajekedar-tech)
- **LinkedIn:** [Kedar Vhanaje](https://linkedin.com/in/kedar-vhanaje-13408a274)

⭐ If you find this project interesting, feel free to explore the repository!
---

**Project:** CloudCart – Production-Ready E-Commerce Application on Kubernetes  
**Focus:** Cloud Computing, DevOps, CI/CD, Kubernetes and Monitoring
