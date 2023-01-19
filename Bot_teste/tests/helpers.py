# tests/helpers.py

import random
import string
from time import sleep
from typing import Optional

from telethon.tl.custom.message import Message, MessageButton


# Used to generate random unique names for lists and items.
# This way you do not need to think about clashing names
# when you do not clear DB after each test.
def random_string(length=16):
    """Return random string of ASCII letters in both registers."""
    return ''.join(
        random.choice(string.ascii_letters) for _ in range (length)
    )


# It is useful to pause from time to time, otherwise
# tests may start failing due to weird latency effects.
# Experimentally I arrived at a delay of 0.5 seconds.
def wait():
    """Sleep of fixed duration (in tests.config)."""
    sleep(0.5)


# Simplifies the most frequent action - look for a button
# with a given text either to check that it exists or click it.
def get_button_with_text(
    message: Message, text: str, strict: bool = False
) -> Optional[MessageButton]:
    """Return MessageButton from Message with text or None."""
    if message.buttons is None:
        return None

    for row in message.buttons:
        for button in row:
            if strict:
                is_match = text == button.text
            else:
                is_match = text in button.text
            if is_match:
                return button

    return None