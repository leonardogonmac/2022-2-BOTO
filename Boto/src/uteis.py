from telegram import ReplyKeyboardRemove
from conexaoDataBase.uteis import *


async def verificar_se_matricula_tem_9_dig(update, context, matricula) -> int:
    if len(matricula) == 9:
        # Descobrindo informaçôes do usuario atraves da conta dele no telegram
        user_info = update.message
        info = {"First_Name": user_info.from_user.first_name, "Last_Name": user_info.from_user.last_name,
                "Matrícula": matricula}
        print(info)
        await update.message.reply_text(
            "Bem vindo, " + user_info.from_user.first_name + " matricula valida.")
        return True
    else:
        print("deu errado :( ")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Matricula, inválida. Tente novamente\n OBS: A matricula deve ter 9 digitos.")
        return False


def pega_mensagem_quebrada(update, context):
    user_message = update.message.text
    user_message = user_message.split(" ")
    user_text = user_message[1]

    return user_text


def pega_mensagem_e_divide(update, context):
    user_message = update.message.text
    user_message = user_message.split(" ")

    return user_message


def pega_caption_e_divide(update, context):
    user_caption = update.message.caption
    user_caption = user_caption.split(" ")

    return user_caption


async def messagem_para_algo_de_errado(update, context, e, textoDesejado) -> int:
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Algo deu errado. \nException: {e}\n{textoDesejado}",
                                   reply_markup=ReplyKeyboardRemove())


async def verifica_matricula_e_senha_professor(matricula_inserido, senha_inserida) -> int:
    professor_existe = await verifica_se_tem_professor_no_banco(matricula_inserido)
    if professor_existe:
        senha_correta = await verifica_se_senha_prof_esta_correta(senha_inserida, matricula_inserido)
        if senha_correta:
            return True
        else:
            return False
    else:
        return False
