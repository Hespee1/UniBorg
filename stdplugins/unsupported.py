""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("z"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Plugins To Load:**\n\n`.load afk`\n\n`.load telegraph `"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd("repo"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Link To The Custom Forked Repo:** https://github.com/somto811/UniBorg/ "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()"""
Files Batch Uploader Plugin for userbot.
usage:- .upb 
Note:- set TEMP_DIR in Your ENV Vars First.
By:-@Zero_cool7870	
"""
import os 
import asyncio
from uniborg.util import admin_cmd
from telethon import events



@borg.on(events.NewMessage(pattern=r"\.upb", outgoing=True))
async def batch_upload(event):
	if event.fwd_from:
		return   
	temp_dir = Config.TEMP_DIR	
	if os.path.exists(temp_dir):    
		files = os.listdir(temp_dir)
		files.sort()
		await event.edit("Uploading Files on Telegram...")
		for file in files:
			required_file_name = temp_dir+"/"+file
			print(required_file_name)
			await borg.send_file(
					event.chat_id,
					required_file_name,
					force_document=True
				)	
	else:
		await event.edit("Directory Not Found.")
		return		
	await event.edit("Successfull.")"""
Files Batch Uploader Plugin for userbot.
usage:- .upb 
Note:- set TEMP_DIR in Your ENV Vars First.
By:-@Zero_cool7870	
"""
import os 
import asyncio
from uniborg.util import admin_cmd
from telethon import events



@borg.on(events.NewMessage(pattern=r"\.upb", outgoing=True))
async def batch_upload(event):
	if event.fwd_from:
		return   
	temp_dir = Config.TEMP_DIR	
	if os.path.exists(temp_dir):    
		files = os.listdir(temp_dir)
		files.sort()
		await event.edit("Uploading Files on Telegram...")
		for file in files:
			required_file_name = temp_dir+"/"+file
			print(required_file_name)
			await borg.send_file(
					event.chat_id,
					required_file_name,
					force_document=True
				)	
	else:
		await event.edit("Directory Not Found.")
		return		
	await event.edit("Successfull.")
