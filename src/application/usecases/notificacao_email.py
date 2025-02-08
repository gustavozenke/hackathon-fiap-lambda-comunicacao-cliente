import logging

from infraestructure.repositories.notificacao_interface import NotificacaoInterface

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoEmail(NotificacaoInterface):

    def enviar_notificacao(self, to_address: str, nome_usuario: str, message: str):
        NotImplementedError("Tipo de comunicacao nao implementado")
