from domain.interfaces.notificacao_service_interface import NotificacaoServiceInterface
from domain.interfaces.notificacao_usecase_interface import NotificacaoUseCaseInterface


class NotificacaoService(NotificacaoServiceInterface):

    def __init__(self, sender: NotificacaoUseCaseInterface):
        self.sender = sender

    def notificar(self, nome_usuario: str, message: str):
        self.sender.enviar_notificacao(nome_usuario, message)
