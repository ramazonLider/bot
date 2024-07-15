from aiogram import Bot, Dispatcher, types
from asyncio import run
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

tugmalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menyu"),
        ],
        [
            KeyboardButton(text="Ovqat"),
            KeyboardButton(text="Sozlamalar")
        ]
    ],
    resize_keyboard=True
)

dp = Dispatcher()

async def echo(message: types.Message, bot: Bot):
    await message.copy_to(chat_id=message.chat.id)

async def answer(message: types.Message):
    await message.answer("Tugmalar", reply_markup=tugmalar)

async def start():
    dp.message.register(echo)
    dp.message.register(answer)

    bot = Bot('7281122628:AAGTWPokuierPgxXfIS2AY0wletQyIdjqfk')
    await dp.start_polling(bot)

run(start())