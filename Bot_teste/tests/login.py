# tests/e2e/get_session_string.py

from telethon import TelegramClient
from telethon.sessions import StringSession


api_id = "22480539"
api_hash = "e0360692292b271db0bbb4451af9d419"


with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Session string:", client.session.save())
