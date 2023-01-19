from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from telegram.ext import *
import handlers_prof

def main():

    TOKEN = "5956872551:AAFIafHdQR08vlx5d4B9PnjCxXlpUXEU3oo"


    dp =  Application.builder().token(TOKEN).build()

    dp.add_handler(CommandHandler("help", handlers_prof.help_command))
    dp.add_handler(CommandHandler("plano_de_ensino", handlers_prof.plano_de_ensino))
    dp.add_handler(CommandHandler("cadastrar_conteudo", handlers_prof.cadastrar_conteudo))

    dp.add_handler(handlers_prof.entrada_conversation)
    dp.add_handler(handlers_prof.enviar_planilha_conversation)

    print("Bot started. . .\n")
    dp.run_polling()
    print("Bot finished. . .\n")

if __name__ == "__main__":
    main()
