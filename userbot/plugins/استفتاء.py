#ZedThon

import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from . import Build_Poll


@bot.on(admin_cmd(pattern="استفتاء( (.*)|$)"))
@bot.on(sudo_cmd(pattern="استفتاء( (.*)|$)", allow_sudo=True))
async def pollcreator(zedpoll):
    reply_to_id = None
    if zedpoll.reply_to_msg_id:
        reply_to_id = zedpoll.reply_to_msg_id
    string = "".join(zedpoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["- اه 😊✌️", "- لا 😏😕", "- معرفش 🥱🙄"])
        try:
            await bot.send_message(
                zedpoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="تحبوني ؟",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await zedpoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                zedpoll,
                "⌔∮ الاستفتاء المستخدم مش هينفع (ممكن تكون في معلومات طويله فشخ).",
            )
        except ForbiddenError:
            await edit_or_reply(zedpoll, "⌔∮ هذه الدردشة تحظر استطلاعات الرأي. ")
        except exception as e:
            await edit_or_reply(zedpoll, str(e))
    else:
        zedinput = string.split("|")
        if len(zedinput) > 2 and len(zedinput) < 12:
            options = Build_Poll(zedinput[1:])
            try:
                await bot.send_message(
                    zedpoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=zedinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await zedpoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    icsspoll,
                    "⌔∮ الاستفتاء المستخدم مش هينفع (ممكن تكون في معلومات طويله فشخ).",
                )
            except ForbiddenError:
                await edit_or_reply(zedpoll, "⌔∮ هذه الدردشة تحظر استطلاعات الرأي. ")
            except Exception as e:
                await edit_or_reply(zedpoll, str(e))
        else:
            await edit_or_reply(
                zedpoll,
                "**⌔∮ انت تكتب الامر بشكل خاطئ يجب عليك كتابته بهذا الشكل** `.استفتاء السؤال | الجواب الاول | الجواب الثاني`",
            )


CMD_HELP.update(
    {
        "استفتاء": "**اسم الاضافـه :**`استفتاء`\
        \n\n**╮•❐ الامـر ⦂** `.استفتاء`\
        \n**الشـرح •• **إذا لم تقدم أي مدخلات ، فإنها ترسل استطلاعًا افتراضيًا. إذا كنت ترغب في تخصيصه ، فاستخدم بناء الجملة هذا :\
        \n `.استفتاء السؤال | الجواب الاول | الجواب الثاني`\
        \n '|' هذا الرمز يفصل بين كل خيار وسؤال \
        "
    }
)
