from pyrogram import Client, filters
from HorridAPI import api
from .paste import create_paste

@Client.on_message(filters.command("llama"))
async def llamachat(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
        
    query = " ".join(message.command[1:])
    ai = api.llama(query)
    if len(ai) > 3700:
        result = await create_paste(ai)  
        await message.reply_text(result["url"])
    else:
        await message.reply_text(ai)
