from telegram import Update, InputMediaPhoto
from telegram.ext import *
import logging
from uteis import pega_caption_e_divide, messagem_para_algo_de_errado, verifica_matricula_e_senha_professor
from conexaoDataBase.enviar_conteudos import enviar_planilha_banco
import emoji
from PIL import Image


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

PLANILHA, ENVIA = range(2)

async def enviar_planilha (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Envie a planilha:")
    await update.message.reply_text("Na mensagem junto ao documento insira sua matricula e senha.\nExemplo: ")
    return PLANILHA

async def recebe_planilha (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    try:
        planilha = await update.message.document.get_file()

        matricula_e_senha = pega_caption_e_divide(update,context)
        matricula_inserida = matricula_e_senha[0]
        senha_inserida = matricula_e_senha[1]

        dados_corretos = await verifica_matricula_e_senha_professor(matricula_inserida,senha_inserida)

        if dados_corretos:
            await planilha.download_to_drive(f"conexaoDataBase/PlanilhasPreenchidas/{matricula_inserida}.xlsx")
            await enviar_planilha_banco(matricula_inserida)
            await update.message.reply_text("Tudo certo. " + emoji.emojize(':winking_face:'))
        else:
            await update.message.reply_text(
                "Parece que você não esta cadastrado ou digitou sua matricula/senha erradas.\n"
                "Tente novamente /enviar_planilha")

    except Exception as e:
        texto = "Tente Novamente: seu arquivo xlsx e sua matricula no comentario."
        await messagem_para_algo_de_errado(update, context, e, texto)
        return PLANILHA

    return ConversationHandler.END