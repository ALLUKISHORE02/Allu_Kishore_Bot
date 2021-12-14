import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):ℍ𝕖𝕪 , {mention} , 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕋𝕠
{chatname} ℍ𝕒𝕡𝕡𝕪 𝕋𝕠 𝕊𝕖𝕖 ℍ𝕖𝕣𝕖
	chatid= message.chat.id
	await bot.send_message(text=f"Welcome {message.from_user.mention} to {message.chat.username} ,  Happy to have here",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message): ℍey ,{mention} Have a Nice Day Good Bye!
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , Have a Nice Day",chat_id=chatid)
	

