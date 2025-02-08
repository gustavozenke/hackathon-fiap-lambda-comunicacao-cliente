import logging

import boto3

from infraestructure.repositories.notificacao_interface import NotificacaoInterface

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NotificacaoSms(NotificacaoInterface):

    def __init__(self, aws_region: str = "us-east-1"):
        self.sns_client = boto3.client("sns", region_name=aws_region)

    def enviar_notificacao(self, nome_usuario: str, message: str):
        recipient = ""  # Buscar telefone no cognito
        try:
            response = self.sns_client.publish(
                PhoneNumber=recipient,
                Message=message
            )
            logger.info(f"SMS enviado com sucesso para {recipient}. MessageId: {response['MessageId']}")
            return {"status": "success", "method": "SMS", "recipient": recipient, "messageId": response["MessageId"]}

        except Exception as e:
            logger.error(f"Erro ao enviar SMS para {recipient}: {str(e)}", exc_info=True)
            raise
