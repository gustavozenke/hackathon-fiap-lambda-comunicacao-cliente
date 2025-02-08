from infraestructure.repositories.notificacao_interface import NotificacaoInterface


class NotificacaoService:

    def __init__(self, sms_sender: NotificacaoInterface, email_sender: NotificacaoInterface):
        self.senders = {
            "SMS": sms_sender,
            "Email": email_sender
        }

    def process_notification(self, nome_usuario: str, notification_type: str, message: str):
        sender = self.senders.get(notification_type)
        if not sender:
            raise ValueError(f"Tipo de notificação inválido: {notification_type}")

        to_address = ""  # TODO: buscar email no cognito
        return sender.enviar_notificacao(nome_usuario, message, to_address)
