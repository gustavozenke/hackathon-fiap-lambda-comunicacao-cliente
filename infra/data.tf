data "aws_secretsmanager_secret" "email_secret" {
  name = "email-credentials"
}

data "aws_secretsmanager_secret_version" "email_secret_version" {
  secret_id = data.aws_secretsmanager_secret.email_secret.id
}

locals {
  email_user    = jsondecode(data.aws_secretsmanager_secret_version.email_secret_version.secret_string)["EMAIL_USER"]
  email_password = jsondecode(data.aws_secretsmanager_secret_version.email_secret_version.secret_string)["EMAIL_PASSWORD"]
}

output "email_user" {
  value = local.email_user
}

output "email_password" {
  value = local.email_password
}