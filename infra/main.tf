terraform {
  backend "s3" {
    bucket = "hackathon-fiap-terraform-tfstate"
    key    = "lambda-comunicacao-cliente.tfstate"
    region = "us-east-1"
  }
}