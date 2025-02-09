import json
import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from application.usecases.notificacao_sms import NotificacaoSms
from infraestructure.repositories.cognito_repository_impl import CognitoRepositoryImpl
from application.entrypoint.lambda_handler import lambda_handler


class TestLambdaHandler(unittest.TestCase):

    @patch.object(NotificacaoSms, "notificar")
    @patch.object(CognitoRepositoryImpl, "__init__")
    def test_lambda_handler_sucesso(self, mock_cognito_repo, mock_notificacao):
        # Arrange
        event = {
            "Records": [
                {
                    "body": json.dumps({
                        "nome_usuario": "teste_usuario",
                        "tipo_comunicacao": "SMS",
                        "mensagem": "Teste de notificação"
                    })
                }
            ]
        }
        mock_notificacao.return_value = None
        mock_cognito_repo.return_value = None

        # Act
        response = lambda_handler(event, None)

        # Assert
        self.assertEqual(response, {"statusCode": 200, "body": "Processamento concluído"})

    @patch.object(CognitoRepositoryImpl, "__init__")
    def test_lambda_handler_payload_invalido(self, mock_cognito_repo):
        # Arrange
        event = {"Records": [{"body": json.dumps({"tipo_comunicacao": "SMS"})}]}
        mock_cognito_repo.return_value = None

        # Act
        response = lambda_handler(event, None)

        # Assert
        self.assertIsNone(response)
