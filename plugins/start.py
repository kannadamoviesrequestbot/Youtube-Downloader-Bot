from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/BAGURUJOINAGUUKANNADAMOVIES_17")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/beereshbanakards")]
    ])
    welcomed = f"Hey hello 👋<b>{message.from_user.first_name} PLEASE JOIN MY CHANNEL @KANNADAMOVIES_17 </b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
