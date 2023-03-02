   # Credit @LazyDeveloper.
    # Please Don't remove credit.
        # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
from pyrogram import Client, filters 
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Note: Lazy_Mode active ✅\n\n__𝙶𝚒𝚟𝚎 𝚖𝚎 𝚊 𝚌𝚊𝚙𝚝𝚒𝚘𝚗 𝚝𝚘 𝚜𝚎𝚝.__\n\n𝙴𝚡𝚊𝚖𝚙𝚕𝚎:- `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__** 𝚈𝙾𝚄𝚁 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝚂𝙰𝚅𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 ✅**__")


@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("Note: Lazy_Mode active ✅\n\n😔**Sorry sweetheart ! No Caption found...**😔")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**** Your Caption deleted successfully**✅️")

@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Note: Lazy_Mode active ✅\n\nYour Caption:-**\n\n`{caption}`")
    else:
       await message.reply_text("😔**Sorry ! No Caption found...**😔")
 63  
plugins/rlazy_filedetect.py
@@ -0,0 +1,63 @@
    # Credit @LazyDeveloper.
    # Please Don't remove credit.
        # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply


@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
        new_name = message.text
        await message.delete()
        await message.delete()
        media = await client.get_messages(message.chat.id, message.reply_to_message.id)
        file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
        filename = file.file_name
        types = file.mime_type.split("/")
        mime = types[0]
        mg_id = media.reply_to_message.id
        try:
            out = new_name.split(".")
            out[1]
            out_name = out[-1]
            out_filename = new_name
            await message.reply_to_message.delete()
            if mime == "video":
                markup = InlineKeyboardMarkup([[
                    InlineKeyboardButton("📁 Document", callback_data="upload_document"),
                    InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
            elif mime == "audio":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "📁 Document", callback_data="doc"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
            else:
                markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]])
            # Lazy-WarninG -> Please Dont chnage anything after this Line 
            await message.reply_text(f"**Select the output file type**\n**🎞New Name** :- ```{out_filename}```", reply_to_message_id=mg_id, reply_markup=markup)

        except:
            try:
                out = filename.split(".")
                out_name = out[-1]
                out_filename = new_name + "." + out_name
            except:
                await message.reply_to_message.delete()
                await message.reply_text("**Error** :  No  Extension in File, Not Supporting", reply_to_message_id=mg_id)
                return
            await message.reply_to_message.delete()
            if mime == "video":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
            elif mime == "audio":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
            else:
                markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]])
            # Lazy-WarninG -> Please Dont chnage anything after this Line 
            await message.reply_text(f"**Select the output file type**\n**🎞New Name** :- ```{out_filename}```",
                                     reply_to_message_id=mg_id, reply_markup=markup)
