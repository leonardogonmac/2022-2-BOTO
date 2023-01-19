import asyncio
import threading
from src.handlers_prof import *
import pytest
from telethon import TelegramClient
from telethon.sessions import StringSession
from helpers import wait
from telethon.tl.custom.conversation import Conversation
from telethon.tl.custom.message import Message

api_id = "digite a chave api_id"
api_hash = "digite a api_hash"
session_str = "digite a session_string"
@pytest.fixture(scope="session")
async def conv():
    client = TelegramClient(
        StringSession(session_str), api_id, api_hash,
        sequential_updates=True
    )
    await client.connect()
    await client.get_me()
    await client.get_dialogs()
    async with client.conversation("@boto_testes_bot",timeout=10, max_messages=10000) as conv:
        yield conv

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

async def get_user_lists(conv: Conversation) -> Message:
    """Return message with user's lists and main menu."""
    await conv.send_message("/help")
    wait()
    return await conv.get_response()

@pytest.mark.anyio
async def test_start(conv):
    """Test /start bot command."""
    await conv.send_message("/start")
    mensagem: Message = await conv.get_response()
    resposta_start = ("Olá, professor digite código")
    # Check that the message contains necessary text
    assert resposta_start in mensagem.text
