from telethon import TelegramClient, events
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH"))

channel_id = int(os.environ.get("CHANNEL")

old_text = os.environ.get("OLD")
new_text = os.environ.get("NEW")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=channel_id))
async def handler(event):
    if event.message.text and old_text in event.message.text:
        new_caption = event.message.text.replace(old_text, new_text)
        await event.message.edit(new_caption)
        print("Caption Edited")

client.start()
client.run_until_disconnected()
