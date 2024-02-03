import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(filters.command(["اصدار"], ""))
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""⩹━𓍹𓋹𓍻⊷⌯ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⌯⊶𓍹𓋹𓍻━⩺\nمرحبا بك عزيزي {message.from_user.mention}\n
𓍹𓋹𓍻᚜ اسم سورس:-المرتجل ميوزك
𓍹𓋹𓍻᚜ نوعه:-ميوزك
𓍹𓋹𓍻᚜ للغه برمجه:- بايثون
𓍹𓋹𓍻᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
𓍹𓋹𓍻᚜ الاصدار 2.1 pyrogram 
𓍹𓋹𓍻᚜ تاريخ تاسيس:-21-2-2020
𓍹𓋹𓍻᚜ مبرمج السورس :- [ᴍʀ ᴇʟᴍᴏʀᴛᴀɢᴇʟ](from_user_id=OWNER)
⩹━𓍹𓋹𓍻⊷⌯ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⌯⊶𓍹𓋹𓍻━⩺""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⩹━𓍹𓋹𓍻⊷⌯ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⌯⊶𓍹𓋹𓍻━⩺ ", url=f"https://t.me/huntersource"), 
                 ],[
                  InlineKeyboardButton(
                text="✯ᴍʀ ᴇʟᴍᴏʀᴛᴀɢᴇʟ✯", url=f"https://t.me/Almortagel_12"
            )
               ],
          ]
        ),
    )


