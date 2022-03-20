from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

from userbot.utils import admin_cmd


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("**╮ معلش يسط ... مش لاقي الجروب او القناه دي 𓅫╰**")
            return None
        except ChannelPrivateError:
            await event.reply(
                "**╮  لا لا انت فهمت غلط الأمر ده مش هينفع لي لينكات جروبات او قنوات خاصه ...𓅫╰**"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("**╮ معلش يسط ... مش لاقي الجروب او القناه دي 𓅫╰**")
            return None
        except (TypeError, ValueError):
            await event.reply("**╮  رابط الجروب مش شغال يقلبي ..𓅫╰**")
            return None
    return chat_info


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name



@bot.on(admin_cmd(pattern=r"اضافة ?(.*)"))
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        eva = await event.reply("**╮  بضيف اهو .. اصبر بقا شويه ...𓅫╰**")
    else:
        eva = await event.edit("**╮  بضيف اهو .. اصبر بقا شويه ...𓅫╰**.")
    ZEDTHON = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await eva.edit("**╮  مش هينفع أضيف أعضاء هنا  𓅫╰**")
    s = 0
    f = 0
    error = "None"

    await eva.edit(
        "**╮  حـالة الإضافـه :**\n\n**╮  جـاري جـمع معـلومات الاعضـاء ...⏳**"
    )
    async for user in event.client.iter_participants( ZEDTHON.full_chat.id):
        try:
            if error.startswith("Too"):
                return (
                    await eva.edit(
                        f"**حـالة الأضـافة انتـهت مـع الأخـطاء**\n- (**ربـما هـنالك ضغـط عـلى الأمࢪ حاول مججـدا لاحقـا 🧸**) \n**الـخطأ** : \n`{error}`\n\n• اضالـة `{s}` \n• خـطأ بأضافـة `{f}`"
                    ),
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await eva.edit(
                f"**╮ جـاري الإضـافـه...⧑**\n\n• تـم اضافـة `{s}` \n•  خـطأ بإضافـة `{f}` \n\n**× آخـر خـطأ:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await eva.edit(
        f"**⌔∮تـمت الإضافـه بنجـاح ✅** \n\n• تـم اضـافة `{s}` \n• خـطأ بإضافـة `{f}`"
    )


CMD_HELP.update(
    {
        "اضافة اعضاء": "**اسم الاضافـه :**`اضافة اعضاء`\
    \n\n**  ╮•❐ الامـر ⦂** `.اضف + رابط الجروب` )`\
    \n**  •  الشـرح •• **اضافه الأعضاء من جروب لي جروب تاني بص ي صاحبي اول حاجه ابعت الأمر + رابط الجروب الي عاوز تيجيب منو أعضاء و تبعت الأمر مع الرابط الجروب التاني في الجروب الي عاوز تضيف الأعضاء في."
    }
)
