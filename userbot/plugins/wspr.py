from . import reply_id as rd
from userbot.tosh import *


WPIC = "https://telegra.ph/file/dfd7fc05a81748a87761c.jpg"
T = "𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑺𝑬𝑪𝑹𝑬𝑻 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ قائـمه اوامر الهمسه :** \n⪼ `.الهمسه` لعرض كيفيه ارسال الهمسه من بوتك\n⪼ `.همسه` لارسال همسه عن طريق بوت الهمسه  \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n𓆩 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - [قناة السورس](t.me/ZedThon) 𓆪"

@icssbot.on(icss_cmd(pattern="م21"))
async def wspr(kimo):
    await eor(kimo, T)


# Wespr - همسه
@icssbot.on(icss_cmd(outgoing=True, pattern="الهمسه$"))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"اذا تريد ترسل همسه من خلال البوت الخاص بك يجب كتابه اولا #معرف_البوت ثم #secret ثم تكتب #معرف_الي_تريد_تهمسله ثم #الرساله وستضهر ايقونه وتضغط عليها وبس 🖤✨.\n"
        ics_c += f"**- قم بنسخ :**\n `{TBOT} secret @ZedThon الرساله`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)


# Wespr - همسه
@icssbot.on(
    icss_cmd(pattern="همسه ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    bu = "@BYYiBoT"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(bu, wwwspr) 
    await tap[0].click(event.chat_id)
    await event.delete()
