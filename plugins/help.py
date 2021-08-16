from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) please send me Send Youtube Url
JOIN MY CHANNEL
@KANNADAMOVIES_17"
    await message.reply_text(helptxt)
