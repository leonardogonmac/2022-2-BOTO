from telegram import ReplyKeyboardRemove, Update
from telegram.ext import *
from uteis import *
from conexaoDataBase.cadastro_aluno import *
from conexaoDataBase.enviar_info import *
from conexaoDataBase.recebe_conteudo import *
import logging
import emoji

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

"""
Essa parte e para lidar com a comandos extras
"""
async def help_command(update, context) -> int:

    await update.message.reply_text("Eu posso te ajudar a enviar e acessar conteúdos e materiais.\n "
                              "Você pode utilizar os seguintes comandos:\n"
                              "\n"
                              "/novo_conteudo - envia um link de um novo conteúdo para a base de dados;\n"
                              "/acessar_conteudo - acessa um conteúdo existente na base de dados;\n"
                              "/deletar_conteudo - apaga um conteudo na base de dados;\n"
                              "/editar_conteudo - altera um conteudo existente na base de dados.\n"
                              "/contatosProfessor - exibe formas de entrar em contato com o professor.")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Conversa encerrada.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

"""
Essa parte e para lidar com a entrada do aluno
"""

ENTRADA, PROFESSOR = range(2)

async def start(update, context) -> int:
    await update.message.reply_text("Olá, aluno digite sua matricula:")

    return  ENTRADA

async def alunoEntrada(update, context)->int:
    try:
        matricula = update.message.text

        tem_9_digitos = await verificar_se_matricula_tem_9_dig(update,context,matricula)
        if not tem_9_digitos:
            return ENTRADA
        else:
            user_info = update.message
            nome = user_info.from_user.first_name + user_info.from_user.last_name

            tem_no_banco = await coloca_aluno_no_banco(matricula,nome)
            if tem_no_banco:
                user_info = update.message
                await update.message.reply_text("Bem vindo, " + user_info.from_user.first_name +
                                                "!.\nEsses são seus comandos:\n\n/contatos_Professor\n/plano_de_ensino")
                await update.message.reply_text("Para receber seu conteudo digite: /conteudo 'sua_matricula'.\nExemplo: /conteudo 123456789")
                return ConversationHandler.END
            else:
                await update.message.reply_text("Digite a matricula do seu professor:")

    except Exception as e:
        await messagem_para_algo_de_errado(update,context,e," ")
        return ConversationHandler.END

    return PROFESSOR

async def cadastro_matricula_professor(update,context):
    matriculaProfessor = update.message.text

    existe_professor = await verifica_se_tem_professor_no_banco(matriculaProfessor)

    if existe_professor:

        await cadastrando_o_professor_do_aluno(matriculaProfessor)

        user_info = update.message
        await update.message.reply_text("Bem vindo, " + user_info.from_user.first_name +
                                        "!.\nEsses são seus comandos:\n\n/contatos_Professor\n/plano_de_ensino")
        await update.message.reply_text(
            "Para receber seu conteudo digite: /conteudo 'sua_matricula'.\nExemplo: /conteudo 123456789")

        return ConversationHandler.END
    else:
        await update.message.reply_text("Esse professor nao encontrado, digite novamente a matricula do seu professor:")

        return PROFESSOR

entrada_conversation = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        ENTRADA: [MessageHandler(filters.TEXT, alunoEntrada)],
        PROFESSOR: [MessageHandler(filters.TEXT, cadastro_matricula_professor)]
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

"""
Essa parte lida com o envio do contato do professor
"""

async def contatos_Professor(update, context)->int:
    await update.message.reply_text("Estes são os contatos da sua professora:\n\n"
                              "E-mail: carla@boto.com\n"
                              "Telegram: @profa_carla\n" + emoji.emojize(':house:') + " Sala S8, 35 14h-16h")
"""
Essa parte lida com o envio de conteudo ao aluno
"""

async def conteudo(update, context) -> int:
    try:
        user_matricula = pega_mensagem_quebrada(update, context)

        existe_matricula = await verifica_se_matricula_aluno_tem_no_banco(user_matricula)

        if existe_matricula:
            conteudo = await busca_professor_conteudo(user_matricula)
        else:
            await update.message.reply_text("Parece que você digitou sua matricula errado.\nTente Novamente: /conteudo 'sua matricula'.")


    except Exception as e:
        texto = "Tente Novamente: /conteudo 'sua matricula'"
        await messagem_para_algo_de_errado(update, context, e, texto)


"""
Essa parte lida com o envio de plano de ensino ao aluno
"""
async def plano_de_ensino(update, context) -> int:
    try:
        user_matricula = pega_mensagem_quebrada(update, context)

        existe_matricula = await verifica_se_matricula_aluno_tem_no_banco(user_matricula)

        if existe_matricula:
            plano_de_enc = await busca_professor(user_matricula)

            if plano_de_enc == None:
                await update.message.reply_text(f"Seu plano de ensino não esta cadastrado")
            else:
                await update.message.reply_text(f"Seu plano de ensino: \n {plano_de_enc}")

        else:
            await update.message.reply_text("Parece que você digitou sua matricula errado.\nTente Novamente: /plano_de_ensino 'sua matricula'.")


    except Exception as e:
        texto = "Tente Novamente: /plano_de_ensino 'sua matricula'"
        await messagem_para_algo_de_errado(update, context, e, texto)
