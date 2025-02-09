import logging

from domain.interfaces.notificacao import Notificacao

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoEmail(Notificacao):

    def notificar(self, nome_usuario: str, message: str):
        NotImplementedError("Tipo de comunicacao nao implementado")
