import logging
import os

from twilio.rest import Client

from application.service.buscar_telefone_usuario_usecase import BuscarTelefoneUsuarioUseCase
from domain.interfaces.notificacao_usecase_interface import NotificacaoUseCaseInterface

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoUseCaseSms(NotificacaoUseCaseInterface):

    def __init__(self, buscar_telefone_usuario_usecase: BuscarTelefoneUsuarioUseCase):
        self.buscar_telefone_usuario_usecase = buscar_telefone_usuario_usecase

    def enviar_notificacao(self, nome_usuario: str, message: str):
        telefone = self.buscar_telefone_usuario_usecase.obter_telefone_usuario(nome_usuario)

        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_ = os.getenv("TWILIO_PHONE_NUMBER")

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message,
            from_=from_,
            to=telefone
        )
        print(f"Mensagem enviada com SID: {message.sid}")
