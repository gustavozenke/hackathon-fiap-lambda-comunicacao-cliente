import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from infraestructure.repositories.cognito_repository_impl import CognitoRepositoryImpl


class TestCognitoRepositoryImpl(unittest.TestCase):

    def setUp(self) -> None:
        os.environ.setdefault("USER_POOL_ID", "user pool teste")

    @patch("boto3.client")
    def test_admin_get_user(self, mock_boto3_client):
        # Arrange
        mock_client_instance = MagicMock()
        mock_boto3_client.return_value = mock_client_instance
        mock_client_instance.admin_get_user.return_value = {"Username": "teste_usuario"}

        repository = CognitoRepositoryImpl()

        # Act
        response = repository.admin_get_user("teste_usuario")

        # Assert
        mock_client_instance.admin_get_user.assert_called_once_with(
            UserPoolId="user pool teste",
            Username="teste_usuario"
        )
        self.assertEqual(response, {"Username": "teste_usuario"})
