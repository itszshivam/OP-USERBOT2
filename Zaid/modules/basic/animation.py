import asyncio
import random

import requests
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from pyrogram.types import Message


from Zaid.helper.basic import edit_or_reply, get_text
from Zaid.helper.constants import MEMES

from Zaid.modules.help import *

DEFAULTUSER = "Man"


NOBLE = [
    "╲╲╲┏━━┓╭━━━╮╱╱╱\n╲╲╲┗┓┏┛┃╭━╮┃╱╱╱\n╲╲╲╲┃┃┏┫┃╭┻┻┓╱╱\n╱╱╱┏╯╰╯┃╰┫┏━╯╱╱\n╱╱┏┻━┳┳┻━┫┗┓╱╱╱\n╱╱╰━┓┃┃╲┏┫┏┛╲╲╲\n╱╱╱╱┃╰╯╲┃┃┗━╮╲╲\n╱╱╱╱╰━━━╯╰━━┛╲╲",
    "┏━╮\n┃▔┃▂▂┏━━┓┏━┳━━━┓\n┃▂┣━━┻━╮┃┃▂┃▂┏━╯\n┃▔┃▔╭╮▔┃┃┃▔┃▔┗━┓\n┃▂┃▂╰╯▂┃┗╯▂┃▂▂▂┃\n┃▔┗━━━╮┃▔▔▔┃▔┏━╯\n┃▂▂▂▂▂┣╯▂▂▂┃▂┗━╮\n┗━━━━━┻━━━━┻━━━┛",
    "┏┓┏━┳━┳━┳━┓\n┃┗┫╋┣┓┃┏┫┻┫\n┗━┻━┛┗━┛┗━┛\n────­­­­­­­­­YOU────",
    "╦──╔╗─╗╔─╔ ─\n║──║║─║║─╠ ─\n╚═─╚╝─╚╝─╚ ─\n╦─╦─╔╗─╦╦   \n╚╦╝─║║─║║ \n─╩──╚╝─╚╝",
    "╔══╗....<3 \n╚╗╔╝..('\../') \n╔╝╚╗..( •.• ) \n╚══╝..(,,)(,,) \n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "░I░L░O░V░E░Y░O░U░",
    "┈┈╭━╱▔▔▔▔╲━╮┈┈┈\n┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈\n╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈\n┈┈┈╲┈╰━━╯┈╱┈┈╳┈\n┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈\n┈╭━╮▔▏┊┊▕▔╭━╮┈╳\n┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈\n┈╰━━━━╲╱━━━━╯┈╳",
    "╔ღ═╗╔╗\n╚╗╔╝║║ღ═╦╦╦═ღ\n╔╝╚╗ღ╚╣║║║║╠╣\n╚═ღ╝╚═╩═╩ღ╩═╝",
    "╔══╗ \n╚╗╔╝ \n╔╝(¯'v'¯) \n╚══'.¸./\n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "╔╗ \n║║╔═╦═╦═╦═╗ ╔╦╗ \n║╚╣╬╠╗║╔╣╩╣ ║║║ \n╚═╩═╝╚═╝╚═╝ ╚═╝ \n╔═╗ \n║═╬═╦╦╦═╦═╦═╦═╦═╗ \n║╔╣╬║╔╣╩╬╗║╔╣╩╣╔╝ \n╚╝╚═╩╝╚═╝╚═╝╚═╩╝",
    "╔══╗ \n╚╗╔╝ \n╔╝╚╗ \n╚══╝ \n╔╗ \n║║╔═╦╦╦═╗ \n║╚╣║║║║╚╣ \n╚═╩═╩═╩═╝ \n╔╗╔╗ ♥️ \n║╚╝╠═╦╦╗ \n╚╗╔╣║║║║ \n═╚╝╚═╩═╝",
    "╔══╗╔╗  ♡ \n╚╗╔╝║║╔═╦╦╦╔╗ \n╔╝╚╗║╚╣║║║║╔╣ \n╚══╝╚═╩═╩═╩═╝\n­­­─────­­­­­­­­­YOU─────",
    "╭╮╭╮╮╭╮╮╭╮╮╭╮╮ \n┃┃╰╮╯╰╮╯╰╮╯╰╮╯ \n┃┃╭┳━━┳━╮╭━┳━━╮ \n┃┃┃┃╭╮┣╮┃┃╭┫╭╮┃ \n┃╰╯┃╰╯┃┃╰╯┃┃╰┻┻╮ \n╰━━┻━━╯╰━━╯╰━━━╯",
    "┊┊╭━╮┊┊┊┊┊┊┊┊┊┊┊ \n━━╋━╯┊┊┊┊┊┊┊┊┊┊┊ \n┊┊┃┊╭━┳╮╭┓┊╭╮╭━╮ \n╭━╋━╋━╯┣╯┃┊┃╰╋━╯ \n╰━╯┊╰━━╯┊╰━┛┊╰━━",
]

R = "❤️"
W = "🤍"

heart_list = [
    W * 9,
    W * 2 + R * 2 + W + R * 2 + W * 2,
    W + R * 7 + W,
    W + R * 7 + W,
    W + R * 7 + W,
    W * 2 + R * 5 + W * 2,
    W * 3 + R * 3 + W * 3,
    W * 4 + R + W * 4,
    W * 9,
]
joined_heart = "\n".join(heart_list)
heartlet_len = joined_heart.count(R)
SLEEP = 0.1


async def _wrap_edit(message, text: str):
    """Floodwait-safe utility wrapper for edit"""
    try:
        await message.edit(text)
    except FloodWait as fl:
        await asyncio.sleep(fl.x)


async def phase1(message):
    """Big scroll"""
    BIG_SCROLL = "🧡💛💚💙💜🖤🤎"
    await _wrap_edit(message, joined_heart)
    for heart in BIG_SCROLL:
        await _wrap_edit(message, joined_heart.replace(R, heart))
        await asyncio.sleep(SLEEP)


async def phase2(message):
    """Per-heart randomiser"""
    ALL = ["❤️"] + list("🧡💛💚💙💜🤎🖤")  # don't include white heart

    format_heart = joined_heart.replace(R, "{}")
    for _ in range(5):
        heart = format_heart.format(*random.choices(ALL, k=heartlet_len))
        await _wrap_edit(message, heart)
        await asyncio.sleep(SLEEP)


async def phase3(message):
    """Fill up heartlet matrix"""
    await _wrap_edit(message, joined_heart)
    await asyncio.sleep(SLEEP * 2)
    repl = joined_heart
    for _ in range(joined_heart.count(W)):
        repl = repl.replace(W, R, 1)
        await _wrap_edit(message, repl)
        await asyncio.sleep(SLEEP)


async def phase4(message):
    """Matrix shrinking"""
    for i in range(7, 0, -1):
        heart_matrix = "\n".join([R * i] * i)
        await _wrap_edit(message, heart_matrix)
        await asyncio.sleep(SLEEP)


@Client.on_message(filters.command(["heart", "love"], ".") & filters.me)
async def hearts(client: Client, message: Message):
    await phase1(message)
    await asyncio.sleep(SLEEP * 3)
    await message.edit("❤️ I")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love You")
    await asyncio.sleep(3)
    await message.edit("❤️ I Love You <3")


@Client.on_message(
    filters.me & (filters.command(["loveyou"], ".") | filters.regex("^loveyou "))
)
async def _(client: Client, message: Message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble]
    await edit_or_reply(message, reply_text)


@Client.on_message(filters.command("wink", ".") & filters.me)
async def wink(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/animu/wink"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()


@Client.on_message(filters.command("hug", ".") & filters.me)
async def hug(client: Client, message: Message):
    hmm_s = "https://telegra.ph//file/e6eb2b8fbcd70609201d4.gif"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()


@Client.on_message(filters.command("pat", ".") & filters.me)
async def pat(client: Client, message: Message):
    hmm_s = "https://telegra.ph//file/88fab4d09ebe709d93c7a.mp4"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()


@Client.on_message(filters.command("pikachu", ".") & filters.me)
async def pikachu(client: Client, message: Message):
    hmm_s = "https://telegra.ph//file/c88ecea0265fee80aaf30.mp4"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    if image_s.endswith(".png"):
        await client.send_photo(message.chat.id, image_s)
        return
    if image_s.endswith(".jpg"):
        await client.send_photo(message.chat.id, image_s)
        return
    await message.delete()


@Client.on_message(filters.command("hmm", ".") & filters.me)
async def hello_world(client: Client, message: Message):
    mg = await edit_or_reply(
        message,
        "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱━╱▔▔▔▔▔╲━╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰━▏▊▕▕▋▕▕━╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭━━━━╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲\n┈┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈ ",
    )


@Client.on_message(
    filters.me & (filters.command(["ahh"], ".") | filters.regex("^ahh "))
)
async def hello_world(client: Client, message: Message):
    mg = await edit_or_reply(message, "ahh")
    await asyncio.sleep(0.2)
    await mg.edit("aahh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhhh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhhhh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhhhhh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhhhhhh")
    await asyncio.sleep(0.2)
    await mg.edit("aaahhhhhhhh")


@Client.on_message(filters.command("brain", ".") & filters.me)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("brain")
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])


@Client.on_message(filters.command("bomb", ".") & filters.me)
async def gahite(client: Client, message: Message):
    if message.forward_from:
        return
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await message.edit("`RIP PLOXXX......`")
    await asyncio.sleep(2)


@Client.on_message(filters.command("call", ".") & filters.me)
async def hajqag(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 18)
    await message.edit("Calling Pavel Durov (ceo of telegram)......")
    animation_chars = [
        "`Connecting To Telegram Headquarters...`",
        "`Call Connected.`",
        "`Telegram: Hello This is Telegram HQ. Who is this?`",
        f"`Me: Yo this is` {DEFAULTUSER} ,`Please Connect me to my lil bro,Pavel Durov `",
        "`User Authorised.`",
        "`Calling Saitama`  `At +916969696969`",
        "`Private  Call Connected...`",
        "`Me: Hello Sir, Please Ban This Telegram Account.`",
        "`Saitama : May I Know Who Is This?`",
        f"`Me: Yo Brah, I Am` {DEFAULTUSER} ",
        "`Saitama : OMG!!! Long time no see, Wassup cat...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
        "`Me: Thanks, See You Later Brah.`",
        "`Saitama : Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
        "`Me: Is There Any Issue/Emergency???`",
        "`Saitama : Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
        "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
        "`Saitama : Sure Sur \nTC Bye Bye :)`",
        "`Private Call Disconnected.`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 18])


@Client.on_message(filters.command("kill", ".") & filters.me)
async def gahah(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.7
    animation_ttl = range(0, 12)
    await message.edit("ready to die dude.....")
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        "(　･ิω･ิ)︻デ═一-->",
        "---->...........",
        "------>.........",
        "-------->.......",
        "---------->.....",
        "------------>...",
        "-------------->.",
        "--------------->",
        "------>;(^。^)ノ ",
        " (￣ー￣) DEAD ",
        " **Mrr Gya Madharchod lala la 😈.😈.😈.😈.😈.😈.😈......** ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 12])


@Client.on_message(filters.command("wtf", ".") & filters.me)
async def gagahkah(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.8
    animation_ttl = range(0, 5)
    await message.edit("wtf")
    animation_chars = [
        "What",
        "What The",
        "What The F",
        "What The F uck",
        "[𝗪𝗵𝗮𝘁 𝗧𝗵𝗲 𝐅𝐔𝐂𝐊](https://telegra.ph//file/a8ea2adf08c78bccb47a3.jpg)",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 5])


@Client.on_message(filters.command("ding", ".") & filters.me)
async def gkahgagw(client: Client, message: Message):
    animation_interval = 0.3
    animation_ttl = range(0, 30)
    animation_chars = [
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜  [ʂɧı۷ąɱ ＯＰ](https://te.legra.ph/file/ebc3fc421b8776e29ad98.mp4) ⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
    ]
    if message.forward_from:
        return
    await message.edit("ding..dong..ding..dong ...")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 10])


@Client.on_message(filters.command("hypo", ".") & filters.me)
async def okihakga(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 15)
    await message.edit("hypo....")
    animation_chars = [
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
        "[👉🔴👈])",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 15])


@Client.on_message(filters.command(["gangsta", "gang", "gangstar"], ".") & filters.me)
async def gajjajay(client: Client, message: Message):
    await message.edit("EVERyBOdy")
    await asyncio.sleep(0.3)
    await message.edit("iZ")
    await asyncio.sleep(0.2)
    await message.edit("GangSTur")
    await asyncio.sleep(0.5)
    await message.edit("UNtIL ")
    await asyncio.sleep(0.2)
    await message.edit("I")
    await asyncio.sleep(0.3)
    await message.edit("ArRivE")
    await asyncio.sleep(0.3)
    await message.edit("🔥🔥🔥")
    await asyncio.sleep(0.3)
    await message.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥🔥🔥")


@Client.on_message(filters.command("charging", ".") & filters.me)
async def timer_blankx(client: Client, message: Message):
    txt = (
        message.text[10:]
        + "\n\n`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:` "
    )
    j = 10
    k = j
    for j in range(j):
        await message.edit(txt + str(k))
        k = k + 10
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    await message.edit(
        "`Tesla Wireless Charging (beta) Completed...\nDevice Detected: Nokia 1100 (Space Grey Varient)\nBattery Percentage:` [100%](https://telegra.ph/file/a45aa7450c8eefed599d9.mp4) ",
        link_preview=True,
    )


@Client.on_message(filters.command(["koc", "kocok"], ".") & filters.me)
async def kocok(client: Client, message: Message):
    e = await edit_or_reply(message, "8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8===✊D💦")
    await e.edit("8==✊=D💦💦")
    await e.edit("8=✊==D💦💦💦")
    await e.edit("8✊===D💦💦💦💦")
    await e.edit("8===✊D💦💦💦💦💦")
    await e.edit("8==✊=D💦💦💦💦💦💦")
    await e.edit("8=✊==D💦💦💦💦💦💦💦")
    await e.edit("8✊===D💦💦💦💦💦💦💦💦")
    await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
    await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
    await e.edit("8=✊==D That's why it's over?")
    await e.edit("RIP 😭😭😭😭")


@Client.on_message(filters.command(["muth"], ".") & filters.me)
async def muth(client: Client, message: Message):
    e = await edit_or_reply(message, "👉✊💦")
    await e.edit("👉        ✊")
    await e.edit("👉    ✊")
    await e.edit("👉✊")
    await e.edit("👉✊💦")
    await e.edit("👉        ✊")
    await e.edit("👉    ✊")
    await e.edit("👉✊")
    await e.edit("👉✊💦")
    await e.edit("👉        ✊")
    await e.edit("👉    ✊")
    await e.edit("👉✊")
    await e.edit("👉✊💦")
    await e.edit("👉        ✊")
    await e.edit("👉    ✊")
    await e.edit("👉✊")
    await e.edit("👉✊💦")
    await e.edit("👉        ✊")
    await e.edit("👉    ✊")
    await e.edit("👉✊")
    await e.edit("👉✊💦")
    await e.edit("👉        ✊")
    await e.edit("👉    ✊")
    await e.edit("👉✊")
    await e.edit("👉✊💦")
    await e.edit("👉        ✊")
    await e.edit("👉    ✊")
    await e.edit("👉✊")
    await e.edit("👉✊💦")
    await e.edit("RIP 😭😭😭😭"
                 
                 
@Client.on_message(filters.command(["fuck", "fucek"], ".") & filters.me)
async def ngefuck(client: Client, message: Message):
    e = await edit_or_reply(message, ".                       /¯ )")
    await e.edit(".                       /¯ )\n                      /¯  /")
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ "
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              ("
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  "
    )


@Client.on_message(filters.command("hack", ".") & filters.me)
async def hak(client: Client, message: Message):
    await message.edit_text("Looking for WhatsApp databases in targeted person...")
    await asyncio.sleep(2)
    await message.edit_text(
        " User online: True\nTelegram access: True\nRead Storage: True "
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s"
    )
    await asyncio.sleep(2)
    await message.edit_text("Hacking complete!\nUploading file...")
    await asyncio.sleep(2)
    await message.edit_text(
        "Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`"
    )


@Client.on_message(filters.command(["kontol", "kntl"], ".") & filters.me)
async def kontol(client: Client, message: Message):
    emoji = get_text(message)
    kontol = MEMES.GAMBAR_KONTOL
    if emoji:
        kontol = kontol.replace("⡀", emoji)
    await message.edit(kontol)


@Client.on_message(filters.command(["penis", "dick"], ".") & filters.me)
async def titid(client: Client, message: Message):
    emoji = get_text(message)
    titid = MEMES.GAMBAR_TITIT
    if emoji:
        titid = titid.replace("😋", emoji)
    await message.edit(titid)


@Client.on_message(filters.command("dino", ".") & filters.me)
async def adadino(client: Client, message: Message):
    typew = await edit_or_reply(message, "`DIN DINNN.....`")
    await asyncio.sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `Larius`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`HE WAS GETTING CLOSER!!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃       🦖`")
    await typew.edit("`🏃      🦖`")
    await typew.edit("`🏃     🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`Just give up`")
    await asyncio.sleep(1)
    await typew.edit("`🧎🦖`")
    await asyncio.sleep(2)
    await typew.edit("`-DIED-`")


@Client.on_message(filters.command(["loveu", "lover"], ".") & filters.me)
async def zeyenk(client: Client, message: Message):
    e = await edit_or_reply(message, "I LOVEE YOUUU 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("LOVE YOU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("LOVE")
    await e.edit("YOU")
    await e.edit("FOREVER 💕")
    await e.edit("💘💘💘💘")
    await e.edit("LOVE")
    await e.edit("I")
    await e.edit("LOVE YOU")
    await e.edit("BABY")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("LOVE YOU 💞")


@Client.on_message(filters.command("gabut", ".") & filters.me)
async def menggabut(client: Client, message: Message):
    e = await edit_or_reply(message, "`GO AWAY`")
    await e.edit("`THHARA VAI JOGINDER`")
    await e.edit("`BANGBANGG`")
    await e.edit("`GYZZZZ`")
    await e.edit("`DUMMKKK`")
    await e.edit("`JAAAAA NAAA`")
    await e.edit("`RAMDKII`")
    await e.edit("`EMMM RUSSIAN`")
    await e.edit("`FUCKKKK`")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("`BITCH`")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🚶                                 🐢")
    await e.edit("`AHHH TAPATAP`")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("😂")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await asyncio.sleep(1)
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("`GABUT`")


@Client.on_message(filters.command(["helikopter", "heli"], ".") & filters.me)
async def helikopter(client: Client, message: Message):
    await edit_or_reply(
        message,
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Baby :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )


@Client.on_message(filters.command("tembak", ".") & filters.me)
async def dornembak(client: Client, message: Message):
    await edit_or_reply(
        message,
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉\n" r"_/﹋\_" "\n **Do you want to be my boyfriend??!**",
    )


@Client.on_message(filters.command("bundir", ".") & filters.me)
async def ngebundir(client: Client, message: Message):
    await edit_or_reply(
        message,
        "`Drugs Everything...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@Client.on_message(filters.command(["awk", "awikwok"], ".") & filters.me)
async def awikwok(client: Client, message: Message):
    await edit_or_reply(
        message,
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`",
    )


@Client.on_message(filters.command("y", ".") & filters.me)
async def ysaja(client: Client, message: Message):
    await edit_or_reply(
        message,
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )


@Client.on_message(filters.command("tank", ".") & filters.me)
async def tank(client: Client, message: Message):
    await edit_or_reply(
        message,
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )


@Client.on_message(filters.command("babi", ".") & filters.me)
async def babi(client: Client, message: Message):
    await edit_or_reply(
        message,
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


@Client.on_message(filters.command(["ajg", "anjg"], ".") & filters.me)
async def anjg(client: Client, message: Message):
    await edit_or_reply(
        message,
        "╥━━━━━━━━╭━━╮━━┳\n"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n",
    )


@Client.on_message(filters.command("nah", ".") & filters.me)
async def nahlove(client: Client, message: Message):
    typew = await edit_or_reply(
        message, "`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 *This is for you`"
    )
    await asyncio.sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`")


@Client.on_message(filters.command("santet", ".") & filters.me)
async def santet(client: Client, message: Message):
    typew = await edit_or_reply(message, "`Enabling Online Witchcraft Command....`")
    await asyncio.sleep(2)
    await typew.edit("`Searching for This Person's Name...`")
    await asyncio.sleep(1)
    await typew.edit("`Online Witchcraft to be Done Immediately`")
    await asyncio.sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   ▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    await asyncio.sleep(1)
    await typew.edit("**Target Successfully Stuck Online 🥴**")


add_command_help(
    "animation",
    [
        ["fuck", "To display the middle finger animation."],
        ["ular", "To display the ular animation."],
        ["dino", "To display dino chased animation."],
        ["santet", "To display online blackmail animation."],
        ["gabut", "To display the animation gait."],
        ["loveu or lover", "To display the animation dear."],
        ["hack", "To display a fake hacking animation."],
        ["bomb", "To display the Bomb animation."],
        ["brain", "To display the Brain animation 🧠."],
        ["kontol", "To display dick art."],
        ["penis", "To display penis art with emoji."],
        ["tembak", "To display shooting art."],
        ["bundir", "To display bundir art."],
        ["helikopter", "To display helicopter art."],
        ["y", "To display art y sj."],
        ["awk", "to display art awkowkowk."],
        ["nah", "To display art love."],
        ["ajg", "To Display art anjing."],
        ["babi", "To display art babi."],
        ["hug", "To get A Hug Gifs anime."],
        ["hmm", "Get Random Hmmm."],
        ["wink", "To Get A Winking Gifs."],
        ["love", "To Propose Someone."],
        ["loveyou", "It Will Send Random Emojis."],
        ["pat", "To get a pat gifs."],
        ["koc", "To display mutthi."],
        [
            "pikachu",
            "to get a Pikachu Gifs",
        ],
        [
            "kill",
            "To kill Someone randomly",
        ],
        [
            "wtf",
            "Wtf animation",
        ],
        [
            "ding",
            "Get Dong",
        ],
        [
            "gang or gangstar",
            "Animation Gangster",
        ],
        [
            "charging",
            " Tesla animation charging",
        ],
    ],
)
