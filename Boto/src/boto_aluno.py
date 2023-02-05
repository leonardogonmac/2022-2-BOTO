from telegram.ext import *
import handlers_aluno

def main():
    TOKEN = "5971556610:AAFV3WHySq0gAFLGKDWW25-WHZnWyk2fGCs"

    dp = Application.builder().token(TOKEN).build()

    dp.add_handler(CommandHandler("help", handlers_aluno.help_command))
    dp.add_handler(CommandHandler("conteudo", handlers_aluno.conteudo))
    dp.add_handler(CommandHandler("plano_de_ensino", handlers_aluno.plano_de_ensino))
    dp.add_handler(CommandHandler("contato", handlers_aluno.contato_professor))

    dp.add_handler(handlers_aluno.entrada_conversation)

    print("Bot started. . .\n")
    dp.run_polling()
    print("Bot finished. . .\n")


if __name__ == "__main__":
    main()
