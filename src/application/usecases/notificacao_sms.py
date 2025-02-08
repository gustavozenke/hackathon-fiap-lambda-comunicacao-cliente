import logging
import os

from twilio.rest import Client

from infraestructure.repositories.notificacao_interface import NotificacaoInterface

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoSms(NotificacaoInterface):

    def enviar_notificacao(self, to: str, nome_usuario: str, message: str):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_ = os.getenv("TWILIO_PHONE_NUMBER")

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message,
            from_=from_,
            to=to
        )
        print(f"Mensagem enviada com SID: {message.sid}")
