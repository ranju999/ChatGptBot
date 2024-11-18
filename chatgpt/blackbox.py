from HorridAPI import Mango
from pyrogram import filters, Client 
from .paste import create_paste

@Client.on_message(filters.command("blackbox"))
async def blackbox(client, message):   
    if len(message.command) < 2:
        await message.reply_text("Give An Input!")
        return
    
    query = " ".join(message.command[1:])
    k = await message.reply_text("🔍")
    mango = Mango()  
    response = mango.chat.completions.create(
        model="blackbox",
        messages=[{"role": "user", "content": query}]
    )

    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await k.edit(result)       
    else:
        await k.edit(response.text)   
