from uteis import *
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import *
from conexaoDataBase.cadastro_aluno import *
from conexaoDataBase.enviar_info import *
from conexaoDataBase.recebe_conteudo import *
from conexaoDataBase.uteis import *
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

"""
Essa parte e para lidar com a comandos extras
"""


async def help_command(update, context) -> int:
    await update.message.reply_text("Esses são seus comandos:\n"
                                    "/conteudo 'sua matricula'\n"
                                    "/plano_de_ensino 'sua matricula'\n"
                                    "/contato 'sua matricula'\n"
                                    "Observe que os seus comandos devem ter o /comando e a sua matricula separada por um espaço: Ex: /contato 123456789")


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

    return ENTRADA


async def alunoEntrada(update, context) -> int:
    try:
        matricula = update.message.text

        tem_9_digitos = await verificar_se_matricula_tem_9_dig(update, context, matricula)
        if not tem_9_digitos:
            return ENTRADA
        else:
            user_info = update.message
            nome = user_info.from_user.first_name + user_info.from_user.last_name

            tem_no_banco = await coloca_aluno_no_banco(matricula, nome)
            if tem_no_banco:
                user_info = update.message
                await update.message.reply_text("Esses são seus comandos:\n"
                                    "/conteudo 'sua matricula'\n"
                                    "/plano_de_ensino 'sua matricula'\n"
                                    "/contato 'sua matricula'\n"
                                    "Observe que os seus comandos devem ter o /comando e a sua matricula separada por um espaço: Ex: /contato 123456789")
                await update.message.reply_text(
                    "Para receber seu conteudo digite: /conteudo 'sua_matricula'.\nExemplo: /conteudo 123456789")
                return ConversationHandler.END
            else:
                await update.message.reply_text("Digite a matricula do seu professor:")

    except Exception as e:
        await messagem_para_algo_de_errado(update, context, e, " ")
        return ConversationHandler.END

    return PROFESSOR


async def cadastro_matricula_professor(update, context):
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
        await update.message.reply_text(
            "Esse professor não foi encontrado, digite novamente a matricula do seu professor:")

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
Essa parte lida com o envio de conteudo ao aluno
"""


async def mensagem_conteudo(update, context, conteudo) -> int:
    if conteudo:
        titulo_conteudo = conteudo[1]
        link_principal = conteudo[2]
        link_extra = conteudo[3]
        await update.message.reply_text(f"Seu conteudo é: {titulo_conteudo} \n {link_principal}")

        if link_extra is not None:
            await update.message.reply_text(f"Link extra:{link_extra}")
    else:
        await update.message.reply_text(f"Você terminou todos os conteudos.")


async def conteudo(update, context) -> int:
    try:
        user_matricula = pega_mensagem_quebrada(update, context)

        existe_matricula = await verifica_se_matricula_aluno_tem_no_banco(user_matricula)

        if existe_matricula:
            conteudo = await buscar_professor_conteudo(user_matricula)

            await mensagem_conteudo(update, context, conteudo)

        else:
            await update.message.reply_text(
                "Parece que você digitou sua matricula errado.\nTente Novamente: /conteudo 'sua matricula'.")


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
            coluna = "plano_de_ensino"
            plano_de_enc = await busca_professor(user_matricula, coluna)

            if plano_de_enc == None:
                await update.message.reply_text(f"Seu plano de ensino não está cadastrado")
            else:
                await update.message.reply_text(f"Seu plano de ensino: \n {plano_de_enc}")

        else:
            await update.message.reply_text(
                "Parece que você digitou sua matricula errado.\nTente Novamente: /plano_de_ensino 'sua matricula'.")


    except Exception as e:
        texto = "Tente Novamente: /plano_de_ensino 'sua matricula'"
        await messagem_para_algo_de_errado(update, context, e, texto)


async def contato_professor(update, context) -> int:
    try:
        user_matricula = pega_mensagem_quebrada(update, context)

        existe_matricula = await verifica_se_matricula_aluno_tem_no_banco(user_matricula)

        if existe_matricula:
            coluna = "contato"
            contato = await busca_professor(user_matricula, coluna)

            if contato == None:
                await update.message.reply_text(f"O contato do seu professor não está cadastrado")
            else:
                await update.message.reply_text(f"O contato do seu professor(a) : \n {contato}")

        else:
            await update.message.reply_text(
                "Parece que você digitou sua matricula errado.\nTente Novamente: /contato 'sua matricula'.")


    except Exception as e:
        texto = "Tente Novamente: /contato 'sua matricula'"
        await messagem_para_algo_de_errado(update, context, e, texto)
