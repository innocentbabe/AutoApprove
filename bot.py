import os, random, traceback
import config

from pyrogram import filters, Client
from pyrogram.types import Message, ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, ChatAdminRequired, UserNotParticipant

from database import add_user, add_group, all_users, all_groups, users, remove_user

app = Client("Auto Approve Bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

welcome=[
    "https://te.legra.ph/file/56ad0cd25443fbba2b931.mp4",
    "https://te.legra.ph/file/dfbd34a9607b1e30b1e7f.mp4",
    "https://te.legra.ph/file/b2ced42696e5a3e2cecfd.mp4",
    "https://te.legra.ph/file/14a5169274a0e709c8213.mp4",
    "https://te.legra.ph/file/79843576cfc427a0c53fe.mp4",
]

#approve 
@app.on_chat_join_request()
async def approval(app: Client, m: ChatJoinRequest):
    usr = m.from_user
    cht = m.chat
    try:
        add_group(cht.id)
        await app.approve_chat_join_request(cht.id, usr.id)
        gif = random.choice(welcome)
        await app.send_animation(chat_id=usr.id, animation=gif, caption=f"ʜᴇʏ ! ᴛʜᴇʀᴇ {usr.first_name}\n➜ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {cht.title}\n\n{usr.first_name} ➜ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {cht.title} ʜᴀs ʙᴇᴇɴ ᴀᴄᴄᴇᴘᴛᴇᴅ ʙʏ {app.me.first_name}")
        add_user(usr.id)
    except (UserIsBlocked, PeerIdInvalid):
        pass
    except Exception as err:
        print(str(err))   

#pvtstart
@app.on_message(filters.command("start") & filters.private)
async def start(app: Client, msg: Message):
    if config.FSUB:
        try:
            await app.get_chat_member(chat_id=config.CHANNEL, user_id=msg.from_user.id)
            add_user(msg.from_user.id)
            await msg.reply_photo(photo="https://te.legra.ph/file/1fcd06207db4d991af38b.jpg", caption=f"ʜᴇʟʟᴏ {msg.from_user.mention},\n\n☉︎ ᴛʜɪs ɪs {app.me.mention},\n\n➲ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠɪɴɢ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs.\n\n➲ ᴊᴜsᴛ ᴀᴅᴅ {app.me.mention} ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ʀɪɢʜᴛs..",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"ᴀᴅᴅ {app.me.first_name}", url=f"https://t.me/{app.me.username}?startgroup=true")], [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{config.CHANNEL}")]]))
        except UserNotParticipant:
            await msg.reply_text(text=f"➜ ᴛᴏ ᴜsᴇ {app.me.mention} ʙᴏᴛ , ʏᴏᴜ ᴍᴜsᴛ sᴜʙsᴄʀɪʙᴇ ᴛᴏ {(await app.get_chat(config.CHANNEL)).title}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❄️ ᴊᴏɪɴ ", url=f"https://t.me/{config.CHANNEL}")], [InlineKeyboardButton ("ᴊᴏɪɴᴇᴅ ❄️", url=f"https://t.me/{app.me.username}?start=start")]]))
        except ChatAdminRequired:
            await app.send_message(text=f"ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ғsᴜʙ ᴄʜᴀᴛ , ᴇɴᴅɪɴɢ ғsᴜʙ......", chat_id=config.OWNER_ID)
    else:
        await msg.reply_photo(
            photo="https://telegra.ph/file/f394c45e5f2f147a37090.jpg",
            caption=f"ʜᴇʟʟᴏ {msg.from_user.mention}.\n\n☉︎ ᴛʜɪs ɪs {app.me.mention} ʙᴏᴛ.\n\n➜ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠɪɴɢ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ɪɴ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ.\n\n➜ ᴊᴜsᴛ ᴀᴅᴅ {app.me.mention} ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘs ᴏʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ʀɪɢʜᴛs.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(f"🌸 ᴀᴅᴅ {app.me.first_name}", url=f"https://t.me/{app.me.username}?startgroup=true")
                    ],
                    [
                        InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ ❄️", url=f"https://t.me/Infinity_Backup")
                    ],
                ]
            )
        )
        add_user(msg.from_user.id)
        

#Gcstart and id
@app.on_message(filters.command("start") & filters.group)
async def gc(app: Client, msg: Message):
    add_group(msg.chat.id)
    add_user(msg.from_user.id)
    await msg.reply_text(text=f"{msg.from_user.mention} sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ...", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🍁 sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ 🌸", url=f"https://t.me/{app.me.username}?start=start")]]))

#stats
@app.on_message(filters.command("stats") & filters.user(config.OWNER_ID))
async def dbtool(app: Client, m: Message):
    xx = all_users()
    x = all_groups()
    await m.reply_text(text=f"➜ sᴛᴀᴛs ғᴏʀ {app.me.mention}\n● **ᴜsᴇʀs :** {xx}\n● **ᴄʜᴀᴛs :** {x}")

#Broadcast
@app.on_message(filters.command("fbroadcast") & filters.user(config.OWNER_ID))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ ᴘʀᴏᴄᴇssɪɴɢ.....`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fbroadcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fbroadcast":
                await m.reply_to_message.forward(int(userid))
        except InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"**➜ sᴜᴄᴄᴇssғᴜʟ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛᴏ {success} ᴜsᴇʀs.\n➜ ғᴀɪʟᴇᴅ ᴛᴏ {failed} ᴜsᴇʀs.\n➜ ғᴏᴜɴᴅ {blocked} ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs. \n➜ ғᴏᴜɴᴅ {deactivated} ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴜsᴇʀs.**")
    


#run
print(f"Starting {app.name}")
try:
    app.run()
except:
    traceback.print_exc()
