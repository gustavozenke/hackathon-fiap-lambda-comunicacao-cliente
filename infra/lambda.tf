data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "../${path.module}/src"
  output_path = "../${path.module}/lambda.zip"
}

resource "aws_lambda_function" "this" {
  filename      = data.archive_file.lambda.output_path
  source_code_hash = data.archive_file.lambda.output_base64sha256

  function_name = var.function_name
  role          = var.function_role
  handler       = var.handler
  runtime       = var.runtime
  timeout       = var.timeout

  environment {
    variables = {
      env = "prod"
      USER_POOL_ID    = local.user_pool_id
      TWILIO_ACCOUNT_SID = local.twillio_account_sid
      TWILIO_AUTH_TOKEN = local.twillio_auth_token
      TWILIO_PHONE_NUMBER = local.twillio_phone_number
    }
  }

  layers = [aws_lambda_layer_version.lambda_layer.arn]
}