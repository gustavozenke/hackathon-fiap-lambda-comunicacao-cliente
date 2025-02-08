data "aws_secretsmanager_secret" "email_secret" {
  name = "sms-credentials"
}

data "aws_secretsmanager_secret_version" "email_secret_version" {
  secret_id = data.aws_secretsmanager_secret.email_secret.id
}

locals {
  user_pool_id    = jsondecode(data.aws_secretsmanager_secret_version.email_secret_version.secret_string)["USER_POOL_ID"]
  twillio_account_sid = jsondecode(data.aws_secretsmanager_secret_version.email_secret_version.secret_string)["TWILIO_ACCOUNT_SID"]
  twillio_auth_token = jsondecode(data.aws_secretsmanager_secret_version.email_secret_version.secret_string)["TWILIO_AUTH_TOKEN"]
  twillio_phone_number = jsondecode(data.aws_secretsmanager_secret_version.email_secret_version.secret_string)["TWILIO_PHONE_NUMBER"]
}