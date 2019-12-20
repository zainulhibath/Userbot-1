# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
""" Userbot module for other small commands. """

from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, UPSTREAM_REPO_URL
from userbot.events import register


@register(outgoing=True, pattern="^.random")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit("**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" +
                     itemo[index] + "`")


@register(outgoing=True, pattern="^.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if " " not in time.pattern_match.group(1):
        await time.reply("Syntax: `.sleep [seconds]`")
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit("`I am sulking and snoozing....`")
        await sleep(2)
        if BOTLOG:
            await time.client.send_message(
                BOTLOG_CHATID,
                "You put the bot to sleep for " + str(counter) + " seconds",
            )
        await sleep(counter)
        await time.edit("`OK, I'm awake now.`")


@register(outgoing=True, pattern="^.shutdown$")
async def killdabot(event):
    """ For .shutdown command, shut the bot down."""
    await event.edit("`Goodbye *Windows XP shutdown sound*....`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n"
                                        "Bot shut down")
    await bot.disconnect()


@register(outgoing=True, pattern="^.restart$")
async def killdabot(event):
    await event.edit("`BRB... *PornHub intro*`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n"
                                        "Bot Restarted")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)


# Copyright (c) Gegham Zakaryan | 2019
@register(outgoing=True, pattern="^.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        f"Click [here]({UPSTREAM_REPO_URL}) to open my userbot's repository.")


@register(outgoing=True, pattern="^.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            "`Check the userbot log for the decoded message data !!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`")
            
@register(outgoing=True, pattern="^.myusernames$")
async def _(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)
            
            
            @register(outgoing=True, pattern="^.community$")
async def bot_community(community):
    """ For .support command, just returns the group link. """
    if not community.text[0].isalpha() and community.text[0] not in ("/", "#", "@", "!"):
        await community.edit("Join the awesome Paperplane UserBot Community: @Crackers_xD\nBe warned that this is a fork of their project and you may get limited support for bugs.")

@register(outgoing=True, pattern="^.support$")
async def bot_support(wannahelp):
    """ For .support command, just returns the group link. """
    if not wannahelp.text[0].isalpha() and wannahelp.text[0] not in ("/", "#", "@", "!"):
        await wannahelp.edit("Join the Paperplane Extended Channel: @PaperplaneExtended")

@register(outgoing=True, pattern="^.creator$")
async def creator(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[Spyder #DerpGang](https://t.me/Spyderzzz/)")

@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("You might want to have a look at the [README.md](https://github.com/spyderzz/Userbot/blob/master/README.md) file.")

#
# Copyright (c) Gegham Zakaryan | 2019
#


CMD_HELP.update({
    'random':
    '.random <item1> <item2> ... <itemN>\
\nUsage: Get a random item from the list of items.'
})

CMD_HELP.update({
    'sleep':
    '.sleep <seconds>\
\nUsage: Userbots get tired too. Let yours snooze for a few seconds.'
})

CMD_HELP.update({
    "shutdown":
    ".shutdown\
\nUsage: Sometimes you need to shut down your bot. Sometimes you just hope to\
hear Windows XP shutdown sound... but you don't."
})

CMD_HELP.update({
    'repo':
    '.repo\
\nUsage: If you are curious what makes the userbot work, this is what you need.'
})

CMD_HELP.update({
    "readme":
    ".readme\
\nUsage: Provide links to setup the userbot and it's modules."
})

CMD_HELP.update({
    "repeat":
    ".repeat <no.> <text>\
\nUsage: Repeats the text for a number of times. Don't confuse this with spam tho."
})

CMD_HELP.update({"restart": ".restart\
\nUsage: Restarts the bot !!"})

CMD_HELP.update({
    "raw":
    ".raw\
\nUsage: Get detailed JSON-like formatted data about replied message."
})
