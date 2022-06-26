from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Saludos {}

Que bola men😎 {}

You can use this bot to convert
1) Sticker en Image
2) Image en Sticker

Send Multiple images or stickers and it will work the same

By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ CREADOR DEL BOT✨", url="https://t.me/nautaii")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🤖 ACTUALIZACION🤖", url="https://t.me/chditoo")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
   

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

1) ENVIAME UN STICKER PARA CONVERTIRLO EN IMAGEN
2) ENVIAME UNA IMAGEN PARA CREAR UN SRICKER

Notea : Y vamos a jugar con el negro 😂 tunometecabrasaramambiche

More features in development. Keep track by joining @nautaii.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @nautaii

Source Code : [Click Here](@nautaii 🙄)

Framework : [Pyrogram]

Language : [Python]

Developer : @nautaii
    """ @StarkProgrammer
    """"""created by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/StickerToolsBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """ @StarkProgrammer
    """"""Programmer
    """ @StarkProgrammer
    """"""