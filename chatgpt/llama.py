from pyrogram import Client, filters
from HorridAPI import api

@Client.on_message(filters.command("llama"))
async def llama(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide the query")
    else:
        query = " ".join(message.command[1:])
        ai = api.llama(query)
        await message.reply_text(ai)
