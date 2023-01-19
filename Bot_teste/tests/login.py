# tests/e2e/get_session_string.py

from telethon import TelegramClient
from telethon.sessions import StringSession


api_id = 27900352
api_hash = "40733d5c93fdb98ef3958af5c71d4663"


with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Session string:", client.session.save())
