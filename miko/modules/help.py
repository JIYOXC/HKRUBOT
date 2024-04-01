from miko import *


@MIKO.UBOT("help", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await help_cmd(client, message)


@MIKO.INLINE("^user_help")
@INLINE.QUERY
async def _(client, inline_query):
    await menu_inline(client, inline_query)


@MIKO.CALLBACK("help_(.*?)")
# @INLINE.DATA
async def _(client, callback_query):
    try:
        await menu_callback(client, callback_query)
    except:
        pass
