import json
import logging

from application.service.notificacao_service import NotificacaoService
from application.usecases.notificacao_email import NotificacaoEmail
from application.usecases.notificacao_sms import NotificacaoSms

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    sms_sender = NotificacaoSms()
    email_sender = NotificacaoEmail()
    notification_service = NotificacaoService(sms_sender, email_sender)

    for record in event['Records']:
        body = json.loads(record['body'])

        nome_usuario = body.get('nome_usuario')
        tipo_comunicacao = body.get('tipo_comunicacao')
        message = body.get('mensagem')

        if not tipo_comunicacao or not message:
            logger.error("Payload inválido. Campos necessários: tipo_notificacao, mensagem, destinatario.")
            continue

        try:
            result = notification_service.process_notification(nome_usuario, tipo_comunicacao, message)
            logger.info(f"Notificação enviada com sucesso: {result}")
        except ValueError as e:
            logger.error(f"Erro: {str(e)}")

    return {"statusCode": 200, "body": "Processamento concluído"}
