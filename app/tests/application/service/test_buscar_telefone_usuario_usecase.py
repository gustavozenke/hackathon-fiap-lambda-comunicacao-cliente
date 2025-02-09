import os
import sys
import unittest
from unittest.mock import MagicMock

from botocore.exceptions import ClientError

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from application.service.buscar_telefone_usuario_usecase import BuscarTelefoneUsuarioUseCase


class TestBuscarTelefoneUsuarioUseCase(unittest.TestCase):

    def setUp(self):
        self.cognito_repository = MagicMock()
        self.use_case = BuscarTelefoneUsuarioUseCase(self.cognito_repository)

    def test_obter_telefone_usuario_sucesso(self):
        # Arrange
        self.cognito_repository.admin_get_user.return_value = {
            'UserAttributes': [
                {'Name': 'phone_number', 'Value': '+11999999999'}
            ]
        }
        # Act
        telefone = self.use_case.obter_telefone_usuario("usuario_teste")

        # Assert
        self.assertEqual(telefone, "+5511999999999")

    def test_obter_telefone_usuario_sem_numero(self):
        # Arrange
        self.cognito_repository.admin_get_user.return_value = {
            'UserAttributes': []
        }

        # Act
        telefone = self.use_case.obter_telefone_usuario("usuario_teste")

        # Assert
        self.assertIsNone(telefone)

    def test_obter_telefone_usuario_erro_clienterror(self):
        # Arrange
        self.cognito_repository.admin_get_user.side_effect = ClientError(
            {"Error": {"Code": "UserNotFoundException", "Message": "Usuario nao encontrado"}}, "AdminGetUser"
        )
        # Act Assert
        with self.assertRaises(ClientError):
            self.use_case.obter_telefone_usuario("usuario_inexistente")
