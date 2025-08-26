# ---------------------------
# Provider AWS
# ---------------------------
provider "aws" {
  region = "us-east-1"
}

# ---------------------------
# ECS Cluster
# ---------------------------
resource "aws_ecs_cluster" "jwt_cluster" {
  name = "jwt-api-cluster"
}

# ---------------------------
# IAM Role para ECS Task Execution
# ---------------------------
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

# Policy gerenciada para permitir ECS puxar imagens do ECR
resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# ---------------------------
# ECS Task Definition
# ---------------------------
resource "aws_ecs_task_definition" "jwt_task" {
  family                   = "jwt-api-task"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"

  # <-- EXECUTION ROLE ADICIONADO
  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([{
    name      = "jwt-api"
    image     = var.ecr_image
    essential = true
    portMappings = [{
      containerPort = 8000
      protocol      = "tcp"
    }]
  }])
}

# ---------------------------
# ECS Service
# ---------------------------
resource "aws_ecs_service" "jwt_service" {
  name            = "jwt-api-service"
  cluster         = aws_ecs_cluster.jwt_cluster.id
  task_definition = aws_ecs_task_definition.jwt_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [var.subnet_id]
    security_groups  = [var.security_group_id]
    assign_public_ip = true
  }
}

# ---------------------------
# Output do IP público da Task ECS Fargate
# ---------------------------
output "jwt_task_public_ip" {
  value       = aws_ecs_service.jwt_service.network_configuration[0].assign_public_ip
  description = "IP público atribuído à task ECS Fargate (true/false)"
}