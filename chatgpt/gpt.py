from .paste import create_paste
from pyrogram.types import *
from config import FSUB_ID
from .fsubb import not_subscribed
from pyrogram import Client, filters
from HorridAPI import Mango

@Client.on_message(filters.command(["gpt", "mango"]))
async def mango_chat(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
        
    query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    mango = Mango()
    response = mango.chat.completions.create(
        model="gpt-3.5",
        messages=[{"role": "user", "content": query}]
    )
    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await msg.edit(result["url"])       
    else:
        await msg.edit(response.text)
