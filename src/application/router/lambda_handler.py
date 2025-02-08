import json
import logging

from application.service.buscar_telefone_usuario_usecase import BuscarTelefoneUsuarioUseCase
from application.service.notificacao_service import NotificacaoService
from application.usecases.notificacao_email import NotificacaoUseCaseEmail
from application.usecases.notificacao_sms import NotificacaoUseCaseSms
from infraestructure.repositories.cognito_repository import CognitoRepository

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cognito_repository = CognitoRepository()
buscar_telefone_usuario_usecase = BuscarTelefoneUsuarioUseCase(cognito_repository)

senders = {
    "EMAIL": NotificacaoUseCaseEmail(),
    "SMS": NotificacaoUseCaseSms(buscar_telefone_usuario_usecase)
}


def lambda_handler(event, context):
    body = json.loads(event['Records'][0]['body'])
    nome_usuario = body.get('nome_usuario')
    tipo_comunicacao = body.get('tipo_comunicacao', "EMAIL")
    mensagem = body.get('mensagem')

    if not nome_usuario or not mensagem:
        logger.error("Payload inválido. Campos necessários: nome_usuario, mensagem.")
        return

    sender = senders.get(tipo_comunicacao)
    try:
        notificacao_service = NotificacaoService(sender)
        notificacao_service.notificar(nome_usuario, mensagem)
        logger.info(f"Notificação enviada com sucesso")
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
