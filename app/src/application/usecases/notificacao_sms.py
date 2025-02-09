import logging
import os

from twilio.rest import Client

from domain.interfaces.buscar_telefone_usuario import BuscarTelefoneUsuario
from domain.interfaces.notificacao import Notificacao

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoSms(Notificacao):

    def __init__(self, buscar_telefone_usuario_usecase: BuscarTelefoneUsuario):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_ = os.getenv("TWILIO_PHONE_NUMBER")
        self.client = self.abrir_client()
        self.buscar_telefone_usuario_usecase = buscar_telefone_usuario_usecase

    def notificar(self, nome_usuario: str, message: str):
        telefone = self.buscar_telefone_usuario_usecase.obter_telefone_usuario(nome_usuario)
        logger.info(f"Enviando SMS para o usuario: {nome_usuario} - telefone:{telefone}. Mensagem={message}")
        response = self.client.messages.create(
            body=message,
            from_=self.from_,
            to=telefone
        )
        logger.info(f"Mensagem enviada com sucesso. Status={response.status}. Response={response.body}")

    def abrir_client(self):
        return Client(self.account_sid, self.auth_token)
