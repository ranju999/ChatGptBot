from pymongo import MongoClient  # Make sure to import MongoClient
from pyrogram import Client, filters
from HorridAPI import Mango

mongo_client = MongoClient(DATABASE_URL)
db = mongo_client['hehe']  
users = db['users']

mango = Mango()

@Client.on_message(filters.private)  
async def gpt(client, message):
    l = message.reply_to_message   
    if not users.find_one({"user": message.from_user.id}):
        users.insert_one({"user": message.from_user.id, "token": 1600, "plan": "free", "mode": "assistant", "chat": 5})
        
    k = users.find_one({"user": message.from_user.id})
        
    if k is None:
        await message.reply_text("User  not found in the database.")
        return

    if k["token"] < 100:
        await message.reply_text("You don't have enough Tokens, use /plan to buy your budget and enjoy")
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
    
    response = await mango.chat.completions.create(model=k["chat"], messages=payload)
       
    H = response.text
    await message.reply_text(H)
