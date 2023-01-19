# import pytest
# import os
# from telethon import TelegramClient
# from telethon.sessions import StringSession
#
# # Your API ID, hash and session string here
# api_id = int(os.environ["22480539"])
# api_hash = os.environ["e0360692292b271db0bbb4451af9d419"]
# session_str = os.environ["1AZWarzMBu1AnGiNX2umoxcs30xqr1yIi3fY1TDK90sKuREl1QikyhR98ytvJ8lf9XO64CdH5eYjORtQq0M2zzO1GFfV1Cftpgvags02SjlwaMej6dn6Y3VPrl2Nyhb3g9WjXK0SUGlapFo64U4FZkVr0IHdikQOUEStmw21HmDadgExV31X9x1aBre1mHdyg60-weV5H3bE9T4h78Cj7l-e7XXDjxqhT-LTd7yL3iZvlARP16hlfXUcVEeJxPWLUZ-GFhrQ_s2_cx9zquCDDohBQkV8ejv4yGEm1o2cWgqkDJAwL-gfWhskx-lPhnNxxGxA8a2cCX-s7oHcy6Rb9lgn4YOhQK3M="]
#
#
# @pytest.fixture(scope="session")
# def client():
#     return TelegramClient(
#         StringSession(session_str), api_id, api_hash,
#         sequential_updates=True
#     )
# tests/conftest.py

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
