from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

tugmalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menyu"),
        ],
        [
            KeyboardButton(text="Ovqat"),
            KeyboardButton(text="Sozlamalar"),
        ]
    ],
    resize_keyboard=True
)