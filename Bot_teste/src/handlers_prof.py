from telegram import ReplyKeyboardRemove, Update
from telegram.ext import *
import logging
import emoji
from cadastro_conteudo import enviar_planilha, recebe_planilha
from conexaoDataBase.prof_plano_ensino import colocar_plano

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

"""
Essa parte e para lidar com a comandos extras
"""
## comando para quando alguma funcao nao esta pronta
def not_finished(update, context):
    update.message.reply_text("Ainda estamos trabalhando nesse comando." + emoji.emojize(':hammer_and_wrench:'))

##menu de comandos
def help_command(update, context):

    update.message.reply_text("Eu posso te ajudar a enviar e acessar conteúdos e materiais.\n "
                              "Você pode utilizar os seguintes comandos:\n"
                              "\n"
                              "/cadastrar_conteudo - Para cadastrar o conteudo da sua materia;\n"
                              "/enviar_plano_de_ensino - Para enviar seu plano de ensino;\n")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Conversa encerrada.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

"""
Essa parte e para lidar o envio de plano de ensino
"""

PLANO = range(4)

async def enviar_plano_de_ensino (update, context) -> int:
    await update.message.reply_text("Envie um LINK DRIVE com seu plano de ensino:")

    return PLANO

async def recebe_plano(update, context) -> int:
    link_plano = update.message.text
    await colocar_plano(link_plano)
    await update.message.reply_text("Recebido " + emoji.emojize(':winking_face:'))


    return ConversationHandler.END

enviar_plano_conversation = ConversationHandler(
    entry_points=[CommandHandler("enviar_plano_de_ensino", enviar_plano_de_ensino)],
    states={
        PLANO: [MessageHandler(filters.TEXT, recebe_plano)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
"""
Essa parte e para lidar com a entrada do professor
"""
ENTRADA = range(4)

async def start(update, context) -> int:
    await update.message.reply_text("Olá, professor digite código")

    return ENTRADA

## comando para verificar a entrada do professor
async def professorEntrada(update,context)-> int:
    ##Codigo correto professor
    codigoprofessor = "p123"

    try:
        ##Pegando o codigo digitado na mensagem
        user_message = update.message.text
        user_code = user_message

        ##Verificando se o codigo inserido é o desejado
        if user_code == codigoprofessor:
            ##Descobrindo informaçôes do usuario atraves da conta dele no telegram
            user_info = update.message
            info = {"First_Name": user_info.from_user.first_name, "Last_Name": user_info.from_user.last_name,
                    "Código": user_code}
            print(info)
            await update.message.reply_text(
                "Bem vindo, Professora " + user_info.from_user.first_name + "!\n\nEsses são seus comandos:\n/enviar_plano_de_ensino\n/enviar_conteudo\n")

        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text = "Código, incorreto. Tente novamente.\nDigite /start para entrar como aluno ou /professorEntrada e seu código. \nExemplo: '/professorEntrada 123456'",
                                     reply_markup=ReplyKeyboardRemove())


    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                 text= f"Erro. Tente novamente. \nException: {e}",
                                 reply_markup=ReplyKeyboardRemove())


    return ConversationHandler.END


entrada_conversation = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        ENTRADA: [MessageHandler(filters.TEXT, professorEntrada)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

"""
Essa parte e para lidar com a conversa de envio de conteudo com o professor
"""
async def cadastrar_conteudo(update,context) -> int:
    await update.message.reply_text("Para cadastrar o seu conteudo faça uma copia da planilha abaixo, depois a preencha.")
    await update.message.reply_text("Tome cuidado não inclua nem exclua alguma coluna e nem altere seu nome.")
    await update.message.reply_text("https://1drv.ms/x/s!AkMmeo5LMub_aWBf1UGvt0X_hTs?e=DN43OT")
    await update.message.reply_text("Apos preenche-la digite /enviar_planilha")

    return ConversationHandler.END

PLANILHA, ENVIA = range(2)

enviar_planilha_conversation = ConversationHandler(
    entry_points=[CommandHandler("enviar_planilha", enviar_planilha)],
    states={
        PLANILHA: [MessageHandler(filters.Document.ALL, recebe_planilha)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)