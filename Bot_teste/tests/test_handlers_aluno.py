# import unittest
# from unittest.mock import patch
# from telegram import *
# from src import handlers_aluno as ha
# from pytest import *
#
# class TestHandlersAluno(unittest.TestCase):
#     def test_alunoEntrada(self):
#         #nao funciona
#         # define mocked_update como a variavel que contem a mensagem do usuario
#         with patch('update') as mocked_update:
#             with patch('context') as mocked_context:
#                 mocked_update.return_value.message.text = "123456789"
#                 mocked_update.return_value.from_user.first_name = "Joao"
#                 mocked_update.return_value.from_user.last_name = "Silva"
#                 nome = "Joao"
#                 sobrenome = "Silva"
#                 matr = "123456789"
#
#                 info = {"First_Name": nome, "Last_Name": sobrenome,
#                     "Matrícula": matr}
#
#                 self.assertEqual(ha.alunoEntrada(mocked_update, mocked_context), info)
#
#
#
# if __name__ == '__main__':
#     unittest.main()
#
# from pytest import *
# from telethon import TelegramClient
# from telethon.tl.custom.message import Message
# from src import handlers_aluno
#
# @mark.asyncio
# async def test_help_command(client: TelegramClient):
#     #Criar um papo
#     with client.conversation("@myReplicaLikeBot", timeout=5) as conv:
#         #send a command
#         await conv.send_message("/help")
#         #get resposta
#         resp: Message = await conv.get_response()
#         #verifica se tta certo
#         assert "@myReplicaLikeBot" in resp.raw_text
#         assert "Eu posso te ajudar a enviar e acessar conteúdos e materiais.\nVocê pode utilizar os seguintes comandos:\n\n/novo_conteudo - envia um link de um novo conteúdo para a base de dados;\n/acessar_conteudo - acessa um conteúdo existente na base de dados;\n/deletar_conteudo - apaga um conteudo na base de dados;\n/editar_conteudo - altera um conteudo existente na base de dados.\n/contatosProfessor - exibe formas de entrar em contato com o professor."