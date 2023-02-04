from telegram import ReplyKeyboardRemove, Update
from telegram.ext import *
import logging
import emoji
from uteis import messagem_para_algo_de_errado, pega_mensagem_e_divide, verifica_matricula_e_senha_professor
from cadastro_conteudo import enviar_planilha, recebe_planilha
from conexaoDataBase.prof_plano_ensino import colocar_plano

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
PLANO, ENTRADA, PLANILHA, ENVIA = range(4)

"""
Essa parte e para lidar com a comandos extras
"""


## comando para quando alguma funcao nao esta pronta
def not_finished(update, context):
    update.message.reply_text("Ainda estamos trabalhando nesse comando." + emoji.emojize(':hammer_and_wrench:'))


##menu de comandos
def help_command(update, context):
    update.message.reply_text("Esses são seus comandos:\n"
                              "/cadastrar_conteudo - Para cadastrar o conteudo da sua materia;\n"
                              "/enviar_plano_de_ensino - Para enviar seu plano de ensino;")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Conversa encerrada.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


"""
Essa parte e para lidar o envio de plano de ensino
"""



async def enviar_plano_de_ensino(update, context) -> int:
    await update.message.reply_text(
        "Envie um LINK DRIVE com seu plano de ensino, sua matricula e senha separados por 1 espaço.\nEx: drive.com '123456789' 'password123'")

    return PLANO


async def recebe_plano(update, context) -> int:
    try:
        mensagem = pega_mensagem_e_divide(update, context)

        link_plano = mensagem[0]
        matricula_professor = mensagem[1]
        senha_professor = mensagem[2]

        dados_corretos = await verifica_matricula_e_senha_professor(matricula_professor, senha_professor)

        if dados_corretos:
            await colocar_plano(link_plano, matricula_professor)
            await update.message.reply_text("Recebido " + emoji.emojize(':winking_face:'))
        else:
            await update.message.reply_text(
                "Parece que você não está cadastrado ou digitou sua matrícula/senha errada.")

    except Exception as e:
        texto = "Tente Novamente: seu link, sua matrícula e senha. Separados apenas por 1 espaço."
        await messagem_para_algo_de_errado(update, context, e, texto)
        return PLANO

    return ConversationHandler.END


enviar_plano_conversation = ConversationHandler(
    entry_points=[CommandHandler("enviar_plano_de_ensino", enviar_plano_de_ensino)],
    states={
        PLANO: [MessageHandler(filters.TEXT, recebe_plano)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
"""
Essa parte e para lidar com o /start do professor
"""



async def start(update, context) -> int:
    await update.message.reply_text("Olá, professor faça seu cadastro em: 'inserir link do web'.")
    await update.message.reply_text("Após o cadastro você podera utilizar os comandos:\n"
                                    "/cadastrar_conteudo\n"
                                    "/enviar_plano_de_ensino")
    await update.message.reply_text("Lembre-se de passar sua matricula para os seus alunos terem acesso a seus conteúdo e plano de ensino.")

    return ConversationHandler.END


"""
Essa parte e para lidar com a conversa de envio de conteudo com o professor
"""


async def cadastrar_conteudo(update, context) -> int:
    await update.message.reply_text(
        "Para cadastrar o seu conteudo faça uma copia da planilha abaixo, depois a preencha.")
    await update.message.reply_text("Tome cuidado não inclua nem exclua alguma coluna e nem altere seu nome.")
    await update.message.reply_text("https://1drv.ms/x/s!AkMmeo5LMub_aWBf1UGvt0X_hTs?e=DN43OT")
    await update.message.reply_text("Apos preenche-la digite /enviar_planilha.")

    return ConversationHandler.END




enviar_planilha_conversation = ConversationHandler(
    entry_points=[CommandHandler("enviar_planilha", enviar_planilha)],
    states={
        PLANILHA: [MessageHandler(filters.Document.ALL, recebe_planilha)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
