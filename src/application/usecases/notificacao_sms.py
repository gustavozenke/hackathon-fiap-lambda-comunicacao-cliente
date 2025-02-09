import logging
import os

from twilio.rest import Client

from domain.interfaces.buscar_telefone_usuario import BuscarTelefoneUsuario
from domain.interfaces.notificacao import Notificacao

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoSms(Notificacao):

    def __init__(self, buscar_telefone_usuario_usecase: BuscarTelefoneUsuario):
        self.buscar_telefone_usuario_usecase = buscar_telefone_usuario_usecase

    def notificar(self, nome_usuario: str, message: str):
        telefone = self.buscar_telefone_usuario_usecase.obter_telefone_usuario(nome_usuario)

        logger.info(f"Enviando SMS para o usuario: {nome_usuario} - telefone:{telefone}. Mensagem={message}")

        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_ = os.getenv("TWILIO_PHONE_NUMBER")

        client = Client(account_sid, auth_token)

        response = client.messages.create(
            body=message,
            from_=from_,
            to=telefone
        )

        logger.info(f"Mensagem enviada com sucesso. Response={response}")
