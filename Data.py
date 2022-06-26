from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

BIENVENIDO 😎 to {}

You can use this bot to convert
1) Sticker to Image
2) Image to Sticker

Send Multiple images or stickers and it will work the same

By @nautaii
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/nautaii")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/nautaii")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/nautaii")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/nautaii")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

1) Send Sticker to get Image
2) Send Image to get Sticker

Note : You can send any amount of images or stickers or both together at once and it will work with same speed and accuracy.

More features in development. Keep track by joining @nautaii.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @nautaii

Source Code : [Iro-bot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @nautaiiProgrammer
    """""ge : [Python](www.python.org)

Developer : @StarkProgrammer
    """""