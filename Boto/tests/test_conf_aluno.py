import asyncio
import threading
import pytest
from telethon import TelegramClient
from telethon.sessions import StringSession
from helpers import wait
from telethon.tl.custom.conversation import Conversation
from telethon.tl.custom.message import Message

api_id = ""
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
    async with client.conversation("@boto_tests_aluno_bot", timeout=10, max_messages=10000) as conv:
        yield conv


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.mark.anyio
async def test_start(conv):
    """Test /start bot command."""
    await conv.send_message("/start")
    mensagem: Message = await conv.get_response()
    resposta_start = ("Olá, aluno digite sua matricula:")
    # Check that the message contains necessary text
    assert resposta_start in mensagem.text


@pytest.mark.anyio
async def test_matricula(conv):
    """Test matricula verification"""
    await conv.send_message("123456789")
    mensagem: Message = await conv.get_response()
    resposta_matricula = ("Bem vindo, Ana Beatriz matricula valida.")
    assert resposta_matricula in mensagem.text


@pytest.mark.anyio
async def test_conteudo(conv):
    """Test /conteudo command"""
    await conv.send_message("/conteudo 123456789")
    mensagem: Message = await conv.get_response()
    resposta_conteudo = ("Você terminou todos os conteudos.")
    assert resposta_conteudo in mensagem.text


@pytest.mark.anyio
async def test_contatos(conv):
    """Test /contato command"""
    await conv.send_message("/contato 123456789")
    mensagem: Message = await conv.get_response()
    resposta_contato = ("O contato do seu professor(a) : \n boto@gmail")
    assert resposta_contato in mensagem.text


@pytest.mark.anyio
async def test_plano(conv):
    """Test /plano_de_ensino command"""
    await conv.send_message("/plano_de_ensino 123456789")
    mensagem: Message = await conv.get_response()
    resposta_plano = ("Seu plano de ensino: \n drve.com")
    assert resposta_plano in mensagem.text
