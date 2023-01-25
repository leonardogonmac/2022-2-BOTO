async def verificar_se_matricula_tem_9_dig(update, context, matricula)->int:
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