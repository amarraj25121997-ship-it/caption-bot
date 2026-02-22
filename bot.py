from telethon import TelegramClient, events
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
channel_id = int(os.environ["CHANNEL"])

old_text = os.environ["OLD"]
new_text = os.environ["NEW"]

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=channel_id))
async def handler(event):
    if event.message.text:
        if old_text in event.message.text:
            new_caption = event.message.text.replace(old_text, new_text)
            await event.message.edit(new_caption)
            print("Caption Edited")

client.start()
client.run_until_disconnected()
