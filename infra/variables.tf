variable "vpc_id" {
  description = "ID da VPC"
  type        = string
}

variable "subnet_id" {
  description = "ID da Subnet pública"
  type        = string
}

variable "security_group_id" {
  description = "ID do Security Group liberando porta 8000"
  type        = string
}

variable "ecr_image" {
  description = "URL da imagem no ECR"
  type        = string
}
