# CloudShop DevOps Project

## Production-Grade DevOps Project with Microservices Architecture

CloudShop is a production-inspired DevOps project built from scratch to demonstrate modern DevOps practices and cloud-native technologies.

The goal of this project is to simulate the complete Software Development Life Cycle (SDLC), from application development to automated deployment, monitoring, logging, security, and infrastructure provisioning.

---

## Project Objectives

* Build a microservices-based application
* Containerize applications using Docker
* Deploy applications on Kubernetes
* Automate infrastructure using Terraform
* Configure servers using Ansible
* Build CI/CD pipelines using GitHub Actions and Jenkins
* Implement GitOps using ArgoCD
* Monitor applications using Prometheus and Grafana
* Centralize logs using Loki
* Deploy on AWS Free Tier

---

## Architecture

```text
                    GitHub
                       │
                GitHub Actions
                       │
                 Docker Images
                       │
                  Docker Hub
                       │
                    Jenkins
                       │
                    ArgoCD
                       │
                 Kubernetes (k3s)
                       │
        ┌─────────┬─────────┬─────────┬─────────┐
        │         │         │         │
     User      Product    Order   Notification
    Service    Service    Service    Service
```

---

## Microservices

| Service              | Description          | Port |
| -------------------- | -------------------- | ---- |
| User Service         | User management      | 5001 |
| Product Service      | Product management   | 5002 |
| Order Service        | Order management     | 5003 |
| Notification Service | Notification service | 5004 |

---

## Technology Stack

### Programming

* Python
* Flask

### Version Control

* Git
* GitHub

### Containerization

* Docker
* Docker Compose

### Orchestration

* Kubernetes (k3s)
* Helm

### Infrastructure as Code

* Terraform

### Configuration Management

* Ansible

### CI/CD

* GitHub Actions
* Jenkins
* ArgoCD

### Database & Messaging

* PostgreSQL
* Redis
* RabbitMQ

### Monitoring

* Prometheus
* Grafana
* Alertmanager

### Logging

* Loki
* Promtail

### Security

* Trivy
* Gitleaks

### Cloud

* AWS

---

## Project Structure

```text
cloudshop/
│
├── user-service/
├── product-service/
├── order-service/
├── notification-service/
├── terraform/
├── ansible/
├── kubernetes/
├── helm/
├── monitoring/
├── logging/
├── scripts/
├── docs/
└── README.md
```

---

## Project Roadmap

* [x] Phase 1 - Flask Microservices
* [ ] Phase 2 - Docker
* [ ] Phase 3 - Docker Compose
* [ ] Phase 4 - GitHub Repository
* [ ] Phase 5 - AWS Infrastructure using Terraform
* [ ] Phase 6 - Server Configuration using Ansible
* [ ] Phase 7 - Kubernetes (k3s)
* [ ] Phase 8 - Kubernetes Deployments
* [ ] Phase 9 - Ingress & Networking
* [ ] Phase 10 - PostgreSQL, Redis & RabbitMQ
* [ ] Phase 11 - GitHub Actions CI
* [ ] Phase 12 - Jenkins CD
* [ ] Phase 13 - ArgoCD GitOps
* [ ] Phase 14 - Monitoring
* [ ] Phase 15 - Logging
* [ ] Phase 16 - Security Scanning
* [ ] Phase 17 - Autoscaling & Production Features
* [ ] Phase 18 - Documentation & Final Review

---

## Current Status

**Phase 1 Completed**

* Four Flask microservices created
* REST API endpoints implemented
* Health check endpoints added
* Python virtual environments configured
* Dependencies managed using `requirements.txt`
* Git repository initialized

---

## Future Enhancements

* Dockerize all services
* Deploy to Kubernetes
* Implement CI/CD
* Configure monitoring and logging
* Add automated security scanning
* Deploy to AWS Free Tier
