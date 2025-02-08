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

    body = json.loads(event['Records'][0]['body'])

    nome_usuario = body.get('nome_usuario')
    tipo_comunicacao = body.get('tipo_comunicacao')
    mensagem = body.get('mensagem')

    if not tipo_comunicacao or not mensagem:
        logger.error("Payload inválido. Campos necessários: tipo_notificacao, mensagem, destinatario.")
        return

    try:
        result = notification_service.process_notification(nome_usuario, tipo_comunicacao, mensagem)
        logger.info(f"Notificação enviada com sucesso: {result}")
    except ValueError as e:
        logger.error(f"Erro: {str(e)}")

    return {"statusCode": 200, "body": "Processamento concluído"}


if __name__ == '__main__':
    event = {
        "Records": [
            {
                "body": '{"nome_usuario":"gustavozenke", "mensagem": "mensagem teste", "tipo_comunicacao": "Email"}',
            }
        ]
    }
    lambda_handler(event, None)
