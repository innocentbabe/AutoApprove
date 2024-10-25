import os, random, traceback
import config

from pyrogram import filters, Client
from pyrogram.types import Message, ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, ChatAdminRequired, UserNotParticipant

from database import add_user, add_group, all_users, all_groups, users, remove_user

app = Client("Auto Approve Bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

welcome=[
    "https://envs.sh/A3c.mp4",
    "https://envs.sh/A3Z.mp4",
    "https://envs.sh/A3L.mp4",
    "https://envs.sh/A35.mp4",
    "https://envs.sh/A3G.mp4",
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
        await app.send_animation(chat_id=usr.id, animation=gif, caption=f"𝖧𝖾𝗒 ! 𝖳𝗁𝖾𝗋𝖾 {usr.first_name}\n➜ 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 {cht.title}\n\n{usr.first_name} ➜ 𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖳𝗈 𝖩𝗈𝗂𝗇 {cht.title} 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖠𝖼𝖼𝖾𝗉𝗍𝖾𝖽 𝖡𝗒 {app.me.first_name}")
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
            await msg.reply_photo(photo="https://graph.org/file/71a7a627703bdd66fce9b-979259fdebf0b3c196.jpg", caption=f"ʜᴇʟʟᴏ {msg.from_user.mention},\n\n☉︎ ᴛʜɪs ɪs {app.me.mention},\n\n➲ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠɪɴɢ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs.\n\n➲ ᴊᴜsᴛ ᴀᴅᴅ {app.me.mention} ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ʀɪɢʜᴛs..",
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
