from pymongo import MongoClient  
from pyrogram import Client, filters
from HorridAPI import Mango
from config import DATABASE_URL

# db 

mongo_client = MongoClient(DATABASE_URL)
db = mongo_client['hehe']  
users = db['users']



@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    l = message.reply_to_message   
    if not users.find_one({"user": message.from_user.id}):
        users.insert_one({"user": message.from_user.id, "mode": "assistant", "chat": 5})
    await message.reply_text(START)
        








mango = Mango()

@Client.on_message(filters.private)  
async def gpt(client, message):
    l = message.reply_to_message   
    if not users.find_one({"user": message.from_user.id}):
        users.insert_one({"user": message.from_user.id, "mode": "assistant", "chat": 5})
        
    k = users.find_one({"user": message.from_user.id})
        
    if k is None:
        await message.reply_text("Error: Please Try few seconds.")
        return    

    if l:
        prompt = f"Old conversation: {l.text}\n\n New conversation: {message.text}"
    else:
        prompt = message.text

    payload = {  
        "messages": [
            { 
                "role": "system",
                "content": k["mode"]
            }, 
            {
                "role": "user", 
                "content": prompt  
            }
        ],
    }
    
    response = await mango.chat.completions.create(
        model=k["chat"], 
        messages=payload
    )           
    await message.reply_text(response.text)
