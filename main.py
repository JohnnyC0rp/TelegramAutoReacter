from pyrogram import Client, filters
import os
from api_info import *

if not os.path.exists("pyrogram_session"):
    os.makedirs("pyrogram_session")


app = Client(
    "my_session",
    workdir="pyrogram_session/",
    api_hash=api_hash,
    api_id=api_id,
)

CHAT_ID = input("Enter chat id: ")
REACTION = input("Enter valid reaction: (eg 🗿)")

@app.on_message(filters.chat(CHAT_ID))
def handle_group_messages(client, message):
    if not message.from_user.is_self:
        app.send_reaction(message.chat.id, message.id, REACTION)


app.run()
