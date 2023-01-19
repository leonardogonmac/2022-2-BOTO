from telegram import Update
from telegram.ext import *
import logging
from conexaoDataBase.enviar_conteudos import enviar_planilha_banco

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

PLANILHA, ENVIA = range(2)
async def enviar_planilha (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Envie a planilha:")

    return PLANILHA

async def recebe_planilha (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    planilha = await update.message.document.get_file()
    await planilha.download_to_drive("conexaoDataBase/PlanilhasPreenchidas/planilha_preenchida.xlsx")

    await enviar_planilha_banco()

    await update.message.reply_text("Deu Bão!.")

    return ConversationHandler.END