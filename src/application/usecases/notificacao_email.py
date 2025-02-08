import logging

from domain.interfaces.notificacao_usecase_interface import NotificacaoUseCaseInterface

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoUseCaseEmail(NotificacaoUseCaseInterface):

    def enviar_notificacao(self, nome_usuario: str, message: str):
        NotImplementedError("Tipo de comunicacao nao implementado")