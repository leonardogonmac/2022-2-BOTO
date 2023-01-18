import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# Your API ID, hash and session string here
api_id = int(os.environ["22480539"])
api_hash = os.environ["e0360692292b271db0bbb4451af9d419"]
session_str = os.environ["1AZWarzMBu1AnGiNX2umoxcs30xqr1yIi3fY1TDK90sKuREl1QikyhR98ytvJ8lf9XO64CdH5eYjORtQq0M2zzO1GFfV1Cftpgvags02SjlwaMej6dn6Y3VPrl2Nyhb3g9WjXK0SUGlapFo64U4FZkVr0IHdikQOUEStmw21HmDadgExV31X9x1aBre1mHdyg60-weV5H3bE9T4h78Cj7l-e7XXDjxqhT-LTd7yL3iZvlARP16hlfXUcVEeJxPWLUZ-GFhrQ_s2_cx9zquCDDohBQkV8ejv4yGEm1o2cWgqkDJAwL-gfWhskx-lPhnNxxGxA8a2cCX-s7oHcy6Rb9lgn4YOhQK3M="]


@pytest.fixture(scope="session")
def client():
    return TelegramClient(
        StringSession(session_str), api_id, api_hash,
        sequential_updates=True
    )
