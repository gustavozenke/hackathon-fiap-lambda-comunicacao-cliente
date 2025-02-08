import os

import boto3
from botocore.exceptions import ClientError

from infraestructure.repositories.notificacao_interface import NotificacaoInterface


class NotificacaoService:

    def __init__(self, sms_sender: NotificacaoInterface, email_sender: NotificacaoInterface):
        self.senders = {
            "SMS": sms_sender,
            "EMAIL": email_sender
        }

    def process_notification(self, nome_usuario: str, notification_type: str, message: str):
        sender = self.senders.get(notification_type)
        if not sender:
            raise ValueError(f"Tipo de notificação inválido: {notification_type}")

        to = self.inserir_pais_telefone(self.obter_telefone_usuario(nome_usuario))
        return sender.enviar_notificacao(to, nome_usuario, message)

    @staticmethod
    def obter_telefone_usuario(nome_usuario):
        client = boto3.client('cognito-idp')
        try:
            response = client.admin_get_user(
                UserPoolId=os.getenv("USER_POOL_ID"),
                Username=nome_usuario
            )
            for attribute in response['UserAttributes']:
                if attribute['Name'] == 'phone_number':
                    return attribute['Value']
            return None
        except ClientError as e:
            print(f"Erro ao buscar o usuário: {e}")
            return None

    @staticmethod
    def inserir_pais_telefone(numero: str) -> str:
        if not numero.startswith("+") or len(numero) < 4:
            raise ValueError("Número de telefone inválido")

        return numero.replace("+", "+55", 1)
