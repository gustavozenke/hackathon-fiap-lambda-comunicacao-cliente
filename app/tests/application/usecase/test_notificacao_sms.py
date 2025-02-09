import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))


from application.usecases.notificacao_sms import NotificacaoSms
from domain.interfaces.buscar_telefone_usuario import BuscarTelefoneUsuario


class TestNotificacaoSms(unittest.TestCase):

    def setUp(self) -> None:
        os.environ.setdefault("TWILIO_ACCOUNT_SID", "account_id")
        os.environ.setdefault("TWILIO_AUTH_TOKEN", "auth_token")
        os.environ.setdefault("TWILIO_PHONE_NUMBER", "phone_number")

    @patch.object(NotificacaoSms, "abrir_client")
    @patch.object(BuscarTelefoneUsuario, "obter_telefone_usuario")
    def test_notificar_sucesso(self, mock_buscar_telefone_usuario, mock_client):

        mock_buscar_telefone_usuario_instance = MagicMock()
        mock_client.return_value = MagicMock()
        mock_buscar_telefone_usuario_instance.obter_telefone_usuario.return_value = "+987654321"

        mock_buscar_telefone_usuario.return_value = mock_buscar_telefone_usuario_instance

        mock_message = MagicMock()
        mock_message.status = "sent"
        mock_message.body = "Message sent"

        notificacao_sms = NotificacaoSms(mock_buscar_telefone_usuario_instance)
        notificacao_sms.notificar("teste_usuario", "Teste de mensagem")

        mock_buscar_telefone_usuario_instance.obter_telefone_usuario.assert_called_once_with("teste_usuario")
