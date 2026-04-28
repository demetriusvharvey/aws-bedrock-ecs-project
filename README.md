# 🚀 AWS Bedrock DevOps Project (ECS + Terraform + CI/CD)

## 📌 Overview

This project demonstrates a **production-style cloud architecture on AWS** that deploys a containerized FastAPI application integrated with AWS Bedrock, using Infrastructure as Code and CI/CD automation.

The system is built to simulate a real-world DevOps environment with load balancing, container orchestration, logging, and automated deployments.

---

## 🧱 Architecture


Internet
↓
Application Load Balancer (ALB)
↓
ECS Fargate (2 Tasks)
↓
Docker Container (FastAPI App)
↓
AWS Bedrock (AI Integration)


---

## ⚙️ Tech Stack

- **Cloud:** AWS  
- **Compute:** ECS Fargate  
- **Load Balancing:** Application Load Balancer (ALB)  
- **Containerization:** Docker  
- **Infrastructure as Code:** Terraform  
- **CI/CD:** GitHub Actions  
- **Logging:** CloudWatch  
- **AI Integration:** AWS Bedrock  
- **Backend:** FastAPI (Python)

---

## 🚀 Features

- ✅ Fully containerized application deployed on ECS Fargate  
- ✅ Load balanced architecture with ALB  
- ✅ High availability with multiple running tasks  
- ✅ CloudWatch logging for observability  
- ✅ Infrastructure fully managed with Terraform  
- ✅ CI/CD pipeline using GitHub Actions  
- ✅ Automatic ECS redeployment on code push  
- ✅ Bedrock-ready AI integration  

---

## 🔁 CI/CD Pipeline

On every push to `main`:

1. GitHub Actions builds Docker image  
2. Image is pushed to Amazon ECR  
3. ECS service is updated with new deployment  
4. New containers are rolled out behind ALB  

---

## 🌐 Live Endpoint


http://bedrock-demo-alb-840953913.us-east-1.elb.amazonaws.com


Example response:

```json
{
  "status": "ok",
  "service": "bedrock-api"
}
🛠️ How to Deploy
1. Clone repo
git clone https://github.com/demetriusvharvey/aws-bedrock-ecs-project.git
cd aws-bedrock-ecs-project/terraform

2. Initialize Terraform
terraform init

3. Deploy infrastructure
terraform apply

📊 Monitoring
Logs are streamed to CloudWatch
ECS tasks are health-checked via ALB
Rolling deployments ensure zero downtime

🧠 Key Concepts Demonstrated
Infrastructure as Code (Terraform)
Container orchestration (ECS)
Load balancing & health checks
CI/CD automation
Cloud logging & monitoring
Scalable microservice deployment
🔮 Future Improvements
Add auto scaling policies
Integrate API Gateway + Lambda version
Add authentication layer
Expand Bedrock integration for real AI responses
Implement Kubernetes (EKS) deployment

👨‍💻 Author
Demetrius Harvey
Cloud & DevOps Engineer