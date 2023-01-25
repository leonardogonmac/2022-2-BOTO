from telegram.ext import *
import handlers_aluno

TOKEN = ""

def main():

    TOKEN = ""

    dp = Application.builder().token(TOKEN).build()

    dp.add_handler(CommandHandler("start", handlers_aluno.start))
    dp.add_handler(CommandHandler("help", handlers_aluno.help_command))

    dp.add_handler(CommandHandler("novo_conteudo", handlers_aluno.not_finished))
    dp.add_handler(CommandHandler("acessar_conteudo", handlers_aluno.not_finished))
    dp.add_handler(CommandHandler("deletar_conteudo", handlers_aluno.not_finished))
    dp.add_handler(CommandHandler("editar_conteudo", handlers_aluno.not_finished))

    dp.add_handler(CommandHandler("matricula", handlers_aluno.alunoEntrada))
    dp.add_handler(CommandHandler("contatosProfessor", handlers_aluno.contatosProfessor))
    dp.add_handler(CommandHandler("plano_de_ensino", handlers_aluno.plano_de_ensino))

    dp.add_handler(MessageHandler(filters.text, handlers_aluno.handle_message))

    print("Bot started. . .\n")
    dp.run_polling()
    print("Bot finished. . .\n")


if __name__ == "__main__":
    main()
