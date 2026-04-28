variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "bedrock-demo"
}

variable "container_port" {
  description = "Port exposed by the application container"
  type        = number
  default     = 8000
}

variable "bedrock_model_id" {
  description = "Amazon Bedrock model ID"
  type        = string
  default     = "amazon.nova-micro-v1:0"
}