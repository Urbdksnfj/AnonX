import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from AnonXMusic import app
from config import OWNER_ID
from AnonXMusic.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic.misc import SUDOERS
import sys
from os import getenv

OWNER_ID = getenv("OWNER_ID")
OWNER_USER_NAME = getenv("OWNER_USER_NAME")
ALMORTAGEL = getenv("ALMORTAGEL")

OWNER = getenv("OWNER")

from dotenv import load_dotenv
import re


@app.on_message(filters.command(["كيب", "✭ رجوع"], "") & SUDOERS)

async def crsourceowner(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


REPLY_MESSAGE = "**👋︙مـرحـبـا بـك عـزيـزي الـمـطـور ♥️**\n**✨︙فــي قـائـمـة التحـكـم بـالـبـوت💞**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("✭ WELCOME IN SOUCE ALMORTAGEL ✭"),
    ],
    [
        ("✭ قسم الاذاعه"),
        ("✭ تحكم الحساب المساعد"),
    ],
    [
        
        ("✭ قسم الجروبات"),
        ("✭ قسم المطورين"),
       
    ],
    [
        ("✭ السورس"),
    ],
]



    
@app.on_message(filters.command(["✭ قسم الاذاعه"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ اذاعه عام","✭ اذاعه بالتوجيه"],["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    
@app.on_message(filters.command(["✭ السورس"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ قـنـاة الـسـورس","✭ للتواصل معنآ"], ["✭ مطور السورس"], ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم السورس تحكم بالازار**", reply_markup=kep)
    
@app.on_message(filters.command(["✭ قسم المطورين"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ مـطـوريـنـك","✭ للتواصل معنآ"],  ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم المطورين تحكم بالازار**", reply_markup=kep)

@app.on_message(filters.command(["✭ قسم الجروبات"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ الجروبات المحظوره","✭ الاحصائيات","✭ حـظـر الـجـروبـات"], ["✭ رجوع","✭ جـروبـاتـك النـشـطـه"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الجروبات تحكم بالازار**", reply_markup=kep)




@app.on_message(filters.command(["✭ قـنـاة الـسـورس"], ""))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/AlmortagelTech",
        caption=f"""𝘀𝗼𝘂𝗿𝗰𝗲 ALMORTAGEL.〙𝘁𝗵𝗲 𝗳 𝗶𝗿𝘀𝘁 𝗰𝗵𝗲𝗿𝘂𝗯 𝗶𝗻 𝘁𝗵𝗲 𝗻𝗲𝘅𝘁 𝗽𝗲𝗼𝗽𝗹𝗲 𝗳𝗼𝗹𝗹𝗼𝘄𝗲𝗱 𝗵 𝗶𝘀 𝗸𝗶𝗻𝗴𝘀 𝗮𝗻𝗱 𝗿𝗮𝗻𝗸 𖥳𝗰𝗿𝗲𝗮𝘁𝗼𝗿𝘀 𝗼𝗳 𝗽𝘂𝘀𝗵𝗰𝗵𝗲𝗻𝗸𝘆♬♪""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/AlmortagelTech"),
            ]
         ]
     )
  )
    

@app.on_message(filters.command(["✭ مطور السورس"], ""))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/Almortagel_12",
        caption=f"""[THIS DEV MAIN SOURCE ALMORTAGEL ](https://t.me/Almortagel_12)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/AlmortagelTech"),
            ]
         ]
     )
  )


    


@app.on_message(filters.command(["✭ للتواصل معنآ"], ""))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/AlmortagelTech",
        caption=f"""[لـطـلـب ســورس مـيـوزك خـاص بــك او مــيـزه في ســورس مـيـوزك لا تـتـردد فـي الـتـواصـل مـعـي مـن خـلال الـزر فـي الأسـفـل ♬♪](https://t.me/AlmortagelTech)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/AlmortagelTech"),
                InlineKeyboardButton("𓆩👨‍💻︙مطور الـسـورس 𓆪", url=f"https://t.me/Almortagel_12"),
            ]
         ]
     )
  )
    
@app.on_message(filters.command(["✭ مطور السورس"], ""))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/Almortagel_12",
        caption=f"""[مطور السورس](https://t.me/Almortagel_12)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩👨‍💻︙مطور الـسـورس 𓆪", url=f"https://t.me/Almortagel_12"),
            ]
         ]
     )
  )
    




@app.on_message(filters.command(["رتبتي"], "") & filters.group )
def forward(client: Client, message: Message):
  chat_id = message.chat.id
  user_id = message.from_user.id
  rank = app.get_chat_member(chat_id, user_id)
  rank = rank.status
  if message.from_user.id == {OWNER_ID}:
   app.send_message(chat_id," • رتبتك هي : مطور البوت")
  if message.from_user.id == 5089553588:
   app.send_message(chat_id," • رتبتك هي : مطور السورس")
  if rank == "administrator":
   app.send_message(chat_id," • رتبتك هي : مطور في المجموعه")
  elif rank == "creator":
   app.send_message(chat_id," • رتبتك هي : المطور الاساس")
  elif rank == "member":
   app.send_message(chat_id," • رتبتك هي : العضـو")
  elif rank == "restricted":
   app.send_message(chat_id," • رتبتك هي : متقيد")
  elif rank == "left":
   app.send_message(chat_id,"• رتبتك هي : مغادر")
  elif rank == "kicked":
   app.send_message(chat_id,"• رتبتك هي : محظور")

@app.on_message(filters.command(['استيكر'], prefixes=""))
async def sticker_id(_, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("**رد علي الملصق لجلب الكود 🤗⚡**")
    if not reply.sticker:
        return await message.reply("**رد علي الملصق لجلب الكود 🤗⚡**")
    await message.reply_text(f"<b>تفضل عزيزي المطور هذا هو id الاستيكر الحالي </b> \n`{reply.sticker.file_id}`")
             
@app.on_message(filters.command(["✭ لغة البوت"], "") & filters.private & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن لغات البوت** : **يتم استخدام هذا الامر لعرض لغات البوت فقط🫡**\n**استخدم الامر بهذا الشكل** `لغة` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )


@app.on_message(filters.command(["✭ الـيـوتـيـوب"], "") & filters.private & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن تحميل من اليوتيوب** : **يتم استخدام هذا الامر لتحميل بشكل مباشر من اليوتيوب **\n**استخدم الامر بهذا الشكل** `تنزيل + اسم الاغنية` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )
   


@app.on_message(filters.command(["مطور البوت","مطور"], "")
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat({OWNER_ID})
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{OWNER_ID}")
                ],
            ]
        ),
    )



@app.on_message(filters.command(["✭ المحـظـوريـن"], "") & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن قائمه الحظر❌** : **يتم استخدام هذا الامر لعرض من هم المحظورين من تشغيل البوت من قبل المالك او المطورين الذي تم رفعهم🫡**\n**استخدم الامر بهذا الشكل** `قائمه الحظر` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )
                    


@app.on_message(filters.command(["✭ مـطـوريـنـك"], "") & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن قائمة المطورين👨‍💻** : **يتم استخدام هذا الامر لعرض من هم الذي تم ترقيتهم من قبل مالك البوت🫡**\n**استخدم الامر بهذا الشكل الثانويين **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )


@app.on_message(filters.command(["✭ ايـديـهـك"], "") & filters.private & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن الايدي** : **يتم استخدام هذا الامر لعرض الايدي بصورة من طلب الامر لماذا تم عمل هذا الميزه في خاص البوت بدل من المجموعه ؟! : السبب ان بعض الاشخاص الفاشلين يضعون صور اباحيه ويقوم بكتبه امر ايدي عندم يظهر البوت الصوره يقوم بعمل ابلاغ في المجموعه حتي يقوم تليجرام بأغلاق المجموعه لذلك تم نقل الامر في الخاص ووضع امر ايدي ايضا بدون صوره في المجموعه🫡**\n**استخدم الامر بهذا الشكل** `ايدي` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )




@app.on_message(filters.command(["✭ حـظـر الـجـروبـات"], "") & filters.private & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن حظر جـروب**🔒❌ : **هذا الامر يستخدم لحظر الجروب من التشغيل عن طريق اليوزر او الايدي🫡**\n**استخدم الامر بهذا الشكل** `blacklistchat` **اضغط علي الامر لنسخ والاستخدام واتبع التعليمات**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )


@app.on_message(filters.command(["✭ جـروبـاتـك النـشـطـه"], "") & filters.private & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن 💡︙جـروبـاتـك النـشـطـه︙💡 : **يتم استخدام هذا الامر لعرض من يقوم بتشغيل البوت الان في المحادثه الصوتية🫡**\n**استخدم الامر بهذا الشكل** `اونلاين` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )


@app.on_message(filters.command(["✭ حـظـر الـجـروبـات"], "") & filters.private & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن حظر جـروب**🔒❌ : **هذا الامر يستخدم لحظر الجروب من التشغيل عن طريق اليوزر او الايدي🫡**\n**استخدم الامر بهذا الشكل** `blacklistchat` **اضغط علي الامر لنسخ والاستخدام واتبع التعليمات**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )


@app.on_message(filters.command(["༺┉⊶﴿♡  ALMORTAGEL ĶËŸBÖÄŖĐ ♡﴾⊷┉༻"], "") & filters.private & SUDOERS)
async def almortagel(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن** ALMORTAGEL ĶËŸBÖÄŖĐ **: **ماهو بيتا كيبورد🤔** **هو اصدار اولي قابل لتعديل في اي وقت قابل الاضافة مميزات واضافة جديد في اي وقت بي اختصار قابل لتحديث ولاضافه في اي وقت**🫡""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
                ],
            ]
        ),
    )




@app.on_callback_query(filters.command(["✭ قـفـل الـكـيـبـورد"], "") & filters.private & SUDOERS)
async def almortagel(_, query: CallbackQuery):
   await callback_query.edit_message_caption(caption =f"""**♬ تــم حــذف الــڪــيــبــورد .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⸥", url=f"https://t.me/AlmortagelTech"),
               ],
            ]
        ),
    )



@app.on_message(filters.command(["قسم التفعيل والتعطيل"], ""))
async def helpercn(client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   userbot = await get_userbot(bot_username)
   me = userbot.me
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([
["تعطيل التواصل","تفعيل التواصل"],
["تعطيل سجل التشغيل","تفعيل سجل التشغيل"],
["تعطيل الاشتراك","تفعيل الاشتراك"],
["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text(f"**♪ مرحبا بك في قسم ⟨ التفعيل والتعطيل ⟩ 🚦 .**", reply_markup=kep,quote=True)

@app.on_message(filters.command(["قسم التعيين"], ""))
async def cast(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([
["تعين اسم البوت"],
["تعين قناة البوت","تعين مجموعة البوت"],
["تعين قناة السورس","تعين مجموعة السورس"],
["تعين لوجو السورس","تعين يوزر مطور السورس"], 
["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**♪ مرحبا بك في قسم ⟨ التعيين ⟩ ⚡ .**", reply_markup=kep)

@app.on_message(filters.command(["قسم البوت"], ""))
async def A_q_lp(client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  chat = message.chat.id
  uesr = message.chat.username
  if chat == dev or uesr in OWNER:
    kep = ReplyKeyboardMarkup([
["الاحصائيات","المكالمات النشطه"],
["المجموعات","المستخدمين"],
["تغير مكان سجل التشغيل"],
["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text(f"**♪ مرحبا بك في قسم ⟨ البوت ⟩  💎 .**", reply_markup=kep,quote=True)
    
@app.on_message(filters.command(["تعين اسم البوت"], ""))
async def set_bot(client: Client, message):
   NAME = await client.ask(message.chat.id,"**♪ ارسل اسم البوت الجديد  💎 .**", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("**♪ تم تعين اسم البوت بنجاح  💎 .**")


@app.on_message(filters.command(["بوت", "البوت"], ""))
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)

@app.on_message(filters.command(["تعين لوجو السورس"], ""))
async def set_vi_so(client: Client, message):
   NAME = await client.ask(message.chat.id,"**♪ ارسل رابط لوجو السورس  💎 .\n♪ مثال ⟨ https://telegra.ph/file/5052303e233d674acebd1.jpg ⟩  💎 .**", filters=filters.text, timeout=30)
   VID_SO = NAME.text
   bot_username = client.me.username
   await set_video_source(bot_username, VID_SO)
   await message.reply_text("**♪ تم تعين لوجو السورس  بنجاح  💎 .**")
   
   
   
@app.on_message(filters.command(["تعين يوزر مطور السورس"], ""))
async def set_dev_username(client: Client, message):
   NAME = await client.ask(message.chat.id,"**♪ ارسل معرف المطور الجديد  💎 .**", filters=filters.text, timeout=300)
   CH_DEV_USER = NAME.text
   bot_username = client.me.username
   await set_dev_user(bot_username, CH_DEV_USER)
   await message.reply_text("**♪ تم تعين المطور بنجاح  💎 .**")

  
@app.on_message(filters.text)
async def bott(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    if message.text == BOT_NAME:
      bar = random.choice(bot).format(BOT_NAME)
      await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
    message.continue_propagation()


@app.on_message(~filters.private)
async def booot(client: Client, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(client, chat_id):
       try:
        await add_served_chat(client, chat_id)
        chats = len(await get_served_chats(client))
        bot_username = client.me.username
        dev = await get_dev(bot_username)
        gr = await get_groupsr(client.me.username)
        username = f"https://t.me/{message.chat.username}" if message.chat.username else None
        mention = message.from_user.mention if message.from_user else message.chat.title
        await client.send_message(dev, f"**تم تفعيل محادثة جديدة تلقائياً واصبحت {chats} محادثة**\nNew Group : [{message.chat.title}]({username})\nId : {message.chat.id} \nBy : {mention}", disable_web_page_preview=True)
        Almortagel_12 = InlineKeyboardMarkup([[InlineKeyboardButton("♪ قناة البوت  💎 .", url="t.me/"+gr)]])
        await client.send_message(chat_id,f"**♪ تم تفعيل البوت تلقائيا  💎 .**",reply_markup=Almortagel_12)
        return 
       except:
          pass
    message.continue_propagation()
    
@app.on_message(filters.command(["تعين قناة البوت"], ""))
async def set_botch(client: Client, message):
   NAME = await client.ask(message.chat.id, "**♪ ارسل رابط القناه البوت الجديدة 💎 .**", filters=filters.text)
   channel = NAME.text
   bot_username = client.me.username
   await set_channel(bot_username, channel)
   await message.reply_text("**♪ تم تعين قناه البوت بنجاح 💎 .**")

@app.on_message(filters.command(["تعين مجموعة البوت"], ""))
async def set_botgr(client: Client, message):
   NAME = await client.ask(message.chat.id, "**♪ ارسل رابط الجروب الجديد 💎 .**", filters=filters.text)
   group = NAME.text
   bot_username = client.me.username
   await set_group(bot_username, group)
   await message.reply_text("**تم تعين مجموعه البوت بنجاح 💎 .**")


@app.on_message(filters.command(["تعين قناة السورس"], ""))
async def set_botchsr(client: Client, message):
   NAME = await client.ask(message.chat.id, "**♪ ارسل رابط القناه البوت الجديدة 💎 .**", filters=filters.text)
   channelsr = NAME.text
   bot_username = client.me.username
   await set_channelsr(bot_username, channelsr)
   await message.reply_text("**♪ تم تعين قناه السورس بنجاح 💎 .**")

@app.on_message(filters.command(["تعين مجموعة السورس"], ""))
async def set_botgrsr(client: Client, message):
   NAME = await client.ask(message.chat.id, "**♪ ارسل رابط الجروب الجديد 💎 .**", filters=filters.text)
   groupsr = NAME.text
   bot_username = client.me.username
   await set_groupsr(bot_username, groupsr)
   await message.reply_text("**♪ تم تعين مجموعه السورس بنجاح 💎 .**")
   
async def set_must(bot_username: dict, m: str):
    if m == "تعطيل الاشتراك":
      ii = "معطل"
    else:
      ii = "مفعل"
    must[bot_username] = ii
    mustdb.update_one({"bot_username": bot_username}, {"$set": {"getmust": ii}}, upsert=True)
    
@app.on_message(filters.command(["تعطيل الاشتراك", "تفعيل الاشتراك"], ""))
async def set_join_must(client: Client, message):
   bot_username = client.me.username
   m = message.command[0]
   await set_must(bot_username, m)
   if message.command[0] == "تعطيل الاشتراك":
     await message.reply_text("**تم تعطيل الاشتراك بنجاح 💎 .**")
   else:
     await message.reply_text("**تم تفعيل الاشتراك بنجاح 💎 .**")
     
@app.on_message(filters.command(["قسم المساعد"], ""))
async def helpercn(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   userbot = await get_userbot(bot_username)
   me = userbot.me
   i = f"@{me.username} : {me.id}" if me.username else me.id
   b = await client.get_chat(me.id)
   b = b.bio if b.bio else "لا يوجد بايو"
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([
["فحص المساعد"],
["تغير الاسم الاول", "تغير الاسم الثاني"], 
["تغير البايو"], 
["تغير اسم المستخدم"], 
["اضافه صوره", "ازالة الصور"],
["دعوه المساعد الي الانضمام"],
 ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text(f"**♪ مرحبا بك في قسم ⟨ المساعد ⟩ 👤 .\n♪ name : {me.mention}  💎 .\n♪ user , id : {i}  💎 .\n♪ bio : {b}  💎 .**", reply_markup=kep)
   

@app.on_message(filters.command(["فحص المساعد"], ""))
async def userrrrr(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in OWNER:
    client = await get_userbot(bot_username)
    mm = await message.reply_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = client.me
    usere = Meh.mention
    async for dialog in client.get_dialogs():
        type = dialog.chat.type
        if enums.ChatType.PRIVATE == type:
            u += 1
        elif enums.ChatType.BOT == type:
            b += 1
        elif enums.ChatType.GROUP == type:
            g += 1
        elif enums.ChatType.SUPERGROUP == type:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status == enums.ChatMemberStatus.ADMINISTRATOR or user_s.status == enums.ChatMemberStatus.OWNER:
                a_chat += 1
        elif enums.ChatType.CHANNEL == type:
            c += 1
        else:
          print(type)

    end = datetime.now()
    ms = (end - start).seconds
    await mm.edit_text(
        """**ꜱᴛᴀᴛꜱ ꜰᴇᴀᴛᴄʜᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ .**
.**ʏᴏᴜ ʜᴀᴠᴇ {} ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ᴄʜᴀɴɴᴇʟꜱ.**
🏷️**ʏᴏᴜ ᴀʀᴇ ᴀᴅᴍɪɴꜱ ɪɴ {} ᴄʜᴀᴛꜱ.**
🏷️**ʙᴏᴛꜱ ɪɴ ʏᴏᴜʀ ᴘʀɪᴠᴀᴛᴇ = {}**
⚠️**ꜰᴇᴀᴛᴄʜᴇᴅ ʙʏ ᴜꜱɪɴɢ {} **""".format(
            ms, u, g, sg, c, a_chat, b, usere
        )
    )

@app.on_message(filters.command(["تغير الاسم الاول"], ""))
async def changefisrt(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "**♪ ارسل الان الاسم الجديد  💎 .**")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(first_name=name)
    await message.reply_text("**♪ تم تغير اسم الحساب المساعد بنجاح  💎 .**")
   except Exception as es:
     await message.reply_text(f"**♪ حدث خطأ أثناء تنفيذ الامر  💎 .\n♪ نوع الخطأ : {es}  💎 .**")


@app.on_message(filters.command(["تغير الاسم الثاني"], ""))
async def changelast(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "**♪ ارسل الان الاسم الجديد  💎 .**")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(last_name=name)
    await message.reply_text("**♪ تم تغير اسم الحساب المساعد بنجاح  💎 .**")
   except Exception as es:
     await message.reply_text(f"**♪ حدث خطأ أثناء تنفيذ الامر  💎 .\n♪ نوع الخطأ : {es}  💎 .**")


@app.on_message(filters.command(["تغير البايو"], ""))
async def changebio(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "**♪ ارسل الان البايو الجديد  💎 .**")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(bio=name)
    await message.reply_text("**♪ تم تغير البايو بنجاح  💎 .**")
   except Exception as es:
     await message.reply_text(f"**♪ حدث خطأ أثناء تنفيذ الامر  💎 .\n♪ نوع الخطأ : {es}  💎 .**")


@app.on_message(filters.command(["تغير اسم المستخدم"], ""))
async def changeusername(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "*♪ ارسل الان اسم المستخدم الجديد  💎 .**")
    name = name.text
    client = await get_userbot(bot_username)
    await client.set_username(name)
    await message.reply_text("**♪ تم تغير اسم المستخدم بنجاح  💎 .**")
   except Exception as es:
     await message.reply_text(f"**♪ حدث خطأ أثناء تنفيذ الامر  💎 .\n♪ نوع الخطأ : {es}  💎 .**")


@app.on_message(filters.command(["اضافه صوره"], ""))
async def changephoto(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    m = await client.ask(message.chat.id, "**♪ قم بإرسال الصوره الجديده الان  💎 .**")
    photo = await m.download()
    client = await get_userbot(bot_username)
    await client.set_profile_photo(photo=photo)
    await message.reply_text("**♪ تم تغير صوره الحساب المساعد بنجاح  💎 .**") 
   except Exception as es:
     await message.reply_text(f"**♪ حدث خطأ أثناء تنفيذ الامر  💎 .\n♪ نوع الخطأ : {es}  💎 .**")

@app.on_message(filters.command(["ازالة الصور"], ""))
async def changephotos(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
       try:
        client = await get_userbot(bot_username)
        photos = await client.get_profile_photos("me")
        await client.delete_profile_photos([p.file_id for p in photos[1:]])
        await message.reply_text("**♪ تم ازاله صوره بنجاح  💎 .**")
       except Exception as es:
         await message.reply_text(f"**♪ حدث خطأ أثناء تنفيذ الامر  💎 .\n♪ نوع الخطأ : {es}  💎 .**")


@app.on_message(filters.command(["دعوه المساعد الي الانضمام"], ""))
async def joined(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "**♪ ارسل الان الرابط  💎 .**")
    name = name.text
    if "https" in name:
     if not "+" in name: 
       name = name.replace("https://t.me/", "")
    client = await get_userbot(bot_username)
    await client.join_chat(name)
    await message.reply_text("**♪ تم انضمام الحساب المساعد بنجاح  💎 .**")
   except Exception as es:
     await message.reply_text(f"**♪ حدث خطأ أثناء تنفيذ الامر  💎 .\n♪ نوع الخطأ : {es}  💎 .**")



@app.on_message(filters.command(["تغير مكان سجل التشغيل", "تفعيل سجل التشغيل", "تعطيل سجل التشغيل"], ""))
async def set_history(client: Client, message):
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
  if message.command[0] == "تغير مكان سجل التشغيل":
   ask = await client.ask(message.chat.id, "**♪ قم بارسال يوزرنيم أو ايدي الذي تريد تعيينه  💎 .**", timeout=30)
   logger = ask.text
   if "@" in logger:
     logger = logger.replace("@", "")
  Botts = Bots.find({})
  for i in Botts:
      bot = client.me
      if i["bot_username"] == bot.username:
        dev = i["dev"]
        token = i["token"]
        session = i["session"]
        bot_username = i["bot_username"]
        loogger = i["logger"]
        logger_mode = i["logger_mode"]
        if message.command[0] == "تغير مكان سجل التشغيل":
         if i["logger"] == logger:
           return await ask.reply_text("**♪ هذا هو مكان السجل بالفعل  💎 .**")
         else:
          try:
           user = await get_userbot(bot_username)
           await client.send_message(logger, "**♪ جاري الفحص  💎 .**")
           await user.send_message(logger, "**♪ جاري تغير مكان السجل  💎 .**")
           d = {"bot_username": bot_username}
           Bots.delete_one(d)
           asyncio.sleep(2)
           aha = {"bot_username": bot_username, "token": token, "session": session, "dev": dev, "logger": logger, "logger_mode": logger_mode}
           Bots.insert_one(aha)
           log[bot_username] = logger
           await ask.reply_text("**♪ تم تغير سجل التشغيل بنجاح  💎 .**")
          except Exception:
            await ask.reply_text("**♪تاكد من اضافه البوت والمساعد وترقيتهم مشرف  💎 .**")
        else:
         mode = "ON" if message.command[0] == "تفعيل سجل التشغيل" else "OFF"
         if i["logger_mode"] == mode:
           m = "مفعل" if message.command[0] == "تفعيل سجل التشغيل" else "معطل"
           return await message.reply_text(f"**♪ سجل التشغيل {m} من قبل  💎 .**")
         else:
          try:
           hh = {"bot_username": bot_username}
           Bots.delete_one(hh)
           h = {"bot_username": bot_username, "token": token, "session": session, "dev": dev, "logger": loogger, "logger_mode": mode}
           Bots.insert_one(h)
           logm[bot_username] = mode
           m = "تفعيل" if message.command == "تفعيل سجل التشغيل" else "تعطيل"
           await message.reply_text(f"**♪ تم {m} سجل التشغيل بنجاح  💎 .**")
          except Exception as es:
            await message.reply_text(f"**♪ تمت الاذاعه بنجاح  💎 .\n♪ تمت الاذاعه الي : {dn}  💎 .\n♪ وفشل : {fd}  💎 .**")
