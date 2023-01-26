from telegram.ext import *
import handlers_prof

def main():

    TOKEN = "5883178059:AAHKrIoW0mHitBZO9F7HBxMgW1Lpa9nmZAE"

    dp =  Application.builder().token(TOKEN).build()

    dp.add_handler(CommandHandler("help", handlers_prof.help_command))
    dp.add_handler(CommandHandler("cadastrar_conteudo", handlers_prof.cadastrar_conteudo))

    dp.add_handler(handlers_prof.entrada_conversation)
    dp.add_handler(handlers_prof.enviar_planilha_conversation)
    dp.add_handler(handlers_prof.enviar_plano_conversation)

    print("Bot started. . .\n")
    dp.run_polling()
    print("Bot finished. . .\n")

if __name__ == "__main__":
    main()
