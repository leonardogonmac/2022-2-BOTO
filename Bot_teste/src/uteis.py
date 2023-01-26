from telegram import ReplyKeyboardRemove
from conexaoDataBase.cadastro_aluno import *
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

async def messagem_para_algo_de_errado(update,context,e,textoDesejado)->int:
    await context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Algo deu errado. \nException: {e}\n{textoDesejado}",
                             reply_markup=ReplyKeyboardRemove())
