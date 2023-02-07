import asyncio
import threading
import pytest
from telethon import TelegramClient
from telethon.sessions import StringSession
from helpers import wait
from telethon.tl.custom.conversation import Conversation
from telethon.tl.custom.message import Message
import openpyxl
from telegram import InputFile
from telegram.ext import Updater, CommandHandler
import emoji

api_id = ''
api_hash = ""
session_str = ""


@pytest.fixture(scope="session")
async def conv():
    client = TelegramClient(
        StringSession(session_str), api_id, api_hash,
        sequential_updates=True
    )
    await client.connect()
    await client.get_me()
    await client.get_dialogs()
    async with client.conversation("@boto_testes_bot", timeout=10, max_messages=10000) as conv:
        yield conv


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.mark.anyio
async def test_start(conv):
    """Test /start bot command."""
    await conv.send_message("/start")
    mensagem: Message = await conv.get_response()
    resposta_start = ("Olá, professor faça seu cadastro em: 'inserir link do web'.")
    # Check that the message contains necessary text
    assert resposta_start in mensagem.text


@pytest.mark.anyio
async def test_cadastrar_conteudo(conv):
    await conv.send_message("/cadastrar_conteudo")
    mensagem: Message = await conv.get_response()
    resposta_envio = ("Para cadastrar o seu conteudo faça uma copia da planilha abaixo, depois a preencha.")
    assert resposta_envio in mensagem.text

    mensagem2: Message = await conv.get_response()
    resposta_envio = ("Tome cuidado não inclua nem exclua alguma coluna e nem altere seu nome.")
    assert resposta_envio in mensagem2.text

    mensagem3: Message = await conv.get_response()
    resposta_envio = ("https://1drv.ms/x/s!AkMmeo5LMub_aWBf1UGvt0X_hTs?e=DN43OT")
    assert resposta_envio in mensagem3.text

    mensagem4: Message = await conv.get_response()
    resposta_envio = ("Apos preenche-la digite /enviar_planilha.")
    assert resposta_envio in mensagem4.text


@pytest.mark.anyio
async def test_enviar_planilha(conv):
    await conv.send_message("/enviar_planilha")

    mensagem: Message = await conv.get_response()
    resposta_envio = ("Envie a planilha:")
    assert resposta_envio in mensagem.text

    mensagem2: Message = await conv.get_response()
    resposta_envio = ("Na mensagem/legenda junto ao documento insira sua matrícula e senha.")
    assert resposta_envio in mensagem2.text


@pytest.mark.anyio
async def test_envia_xlsx(conv):
    """Aviso: precisa-se de um arquivo xlsx no modelo enviado para realizar esse teste"""
    await conv.send_file(file="planilha.xlsx", caption="123456 p123")

    mensagem: Message = await conv.get_response()
    resposta_envio = ("Tudo certo. " + emoji.emojize(':winking_face:'))
    assert resposta_envio in mensagem.text


@pytest.mark.anyio
async def test_plano_de_ensino(conv):
    await conv.send_message("/enviar_plano_de_ensino")
    mensagem: Message = await conv.get_response()
    resposta_envio = (
        "Envie um LINK DRIVE com seu plano de ensino, sua matricula e senha separados por 1 espaço.\nEx: drive.com '123456789' 'password123'")
    assert resposta_envio in mensagem.text


@pytest.mark.anyio
async def test_enviar_plano(conv):
    await conv.send_message("drive.com 123456 p123")
    mensagem: Message = await conv.get_response()
    resposta_envio = ("Recebido " + emoji.emojize(':winking_face:'))
    assert resposta_envio in mensagem.text
