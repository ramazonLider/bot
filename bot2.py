from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from asyncio import run

# Create bot and dispatcher instances
bot = Bot(token='7281122628:AAGTWPokuierPgxXfIS2AY0wletQyIdjqfk')
dp = Dispatcher()

# Translation dictionaries
translations = {
    "rus": {
        "start": "Здравствуйте, {name}",
        "order": "🛍 Сделать заказ",
        "lang": "🌐 Изменить язык",
        "orders": "📦 Мои заказы",
        "settings": "⚙️ Настройки",
        "about": "ℹ️ О нас",
        "feedback": "✍️ Оставить отзыв",
        "choose_category": "С чего начнем?",
        "back": "⬅️ Назад",
        "main_menu": "🏠 Главное меню",
        "about_us": "Наша семья😊 очень давно занимается ресторанной кулинарией🥗🍕🍟🍣🍱. Мы известны великолепной аутентичной кухней, профессиональным шеф-поваром👨🏻‍🍳 и преданным персоналом👩‍🍳🧑‍🍳. Выберите любое блюдо из меню👨‍💻, которое поможет вам ощутить настоящий вкус пиццы🍕❤️."
    },
    "uz": {
        "start": "Assalom alaykum, {name}",
        "order": "🛍 Buyurtma berish",
        "lang": "🌐 Tilni o'zgartirish",
        "orders": "📦 Buyurtmalarim",
        "settings": "⚙️ Sozlamalar",
        "about": "ℹ️ Biz haqimizda",
        "feedback": "✍️ Fikr qoldirish",
        "choose_category": "Nimadan boshlaymiz?",
        "back": "⬅️ Orqaga",
        "main_menu": "🏠 Bosh menyu",
        "about_us": "Наша семья😊очень давно занимается ресторанной кулинарией🥗🍕🍟🍣🍱 Мы известны великолепной аутентичной кухней, профессиональным шеф-поваром👨🏻‍🍳 и преданным персоналом👩‍🍳🧑‍🍳.Выберите любое блюдо из меню👨‍💻, которое поможет вам ощутить настоящий вкус пиццы🍕❤️."
    }
}

# Function to get user language (default is 'uz')
def get_user_language(user_id):
    # Here you can fetch the user language from a database or any other storage
    return "rus"  # Default language is Russian

# Function to get translated text
def t(key, user_id, **kwargs):
    language = get_user_language(user_id)
    return translations[language][key].format(**kwargs)

# Define keyboard layout function
def get_keyboard(user_id):
    language = get_user_language(user_id)
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=t("order", user_id)),
            ],
            [
                KeyboardButton(text=t("orders", user_id)),
                KeyboardButton(text=t("settings", user_id))
            ],
            [
                KeyboardButton(text=t("about", user_id)),
                KeyboardButton(text=t("feedback", user_id))
            ]
        ],
        resize_keyboard=True
    )

def get_set_keyboard(user_id):
    language = get_user_language(user_id)
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=t("lang", user_id)),
            ],
            [
                KeyboardButton(text=t("back", user_id)),
            ],
        ],
        resize_keyboard=True
    )

def get_lang_keyboard(user_id):
    language = get_user_language(user_id)
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇺🇿 O'zbekcha"),
                KeyboardButton(text="🇷🇺 Русский"),
            ],
            [
                KeyboardButton(text=t("back", user_id)),
            ],
        ],
        resize_keyboard=True
    )

# Define category keyboard layout function
def get_category_keyboard(user_id):
    language = get_user_language(user_id)
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🍔 Fast food"),
                KeyboardButton(text="🍕 Pizza"),
            ],
            [
                KeyboardButton(text="🥗 Salatlar"),
                KeyboardButton(text="🍝 Makaron"),
            ],
            [
                KeyboardButton(text="🌶Соусы")
            ],
            [
                KeyboardButton(text=t("back", user_id)),
                KeyboardButton(text=t("main_menu", user_id)),
            ],
        ],
        resize_keyboard=True
    )

# Start command handler
@dp.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(t("start", message.from_user.id, name=user_name), reply_markup=get_keyboard(message.from_user.id))

# Buyurtma berish handler
@dp.message(lambda message: message.text in ["🛍 Buyurtma berish", "🛍 Сделать заказ"])
async def handle_buyurtma_berish(message: types.Message):
    await message.answer(t("choose_category", message.from_user.id), reply_markup=get_category_keyboard(message.from_user.id))

# Biz haqimizda handler
@dp.message(lambda message: message.text in ["ℹ️ Biz haqimizda", "ℹ️ О нас"])
async def handle_biz_haqimizda(message: types.Message):
    await message.answer(t("about_us", message.from_user.id), reply_markup=get_keyboard(message.from_user.id))

# Orqaga handler
@dp.message(lambda message: message.text in ["⬅️ Orqaga", "⬅️ Назад"])
async def handle_orqaga(message: types.Message):
    await message.answer("Orqaga qaytdingiz", reply_markup=get_keyboard(message.from_user.id))

@dp.message(lambda message: message.text in ["⚙️ Sozlamalar", "⚙️ Настройки"])
async def handle_settings(message: types.Message):
    await message.answer("⚙️ Sozlamalar", reply_markup=get_set_keyboard(message.from_user.id))

@dp.message(lambda message: message.text in ["🌐 Tilni o'zgartirish", "🌐 Изменить язык"])
async def handle_langs(message: types.Message):
    await message.answer("Choose", reply_markup=get_lang_keyboard(message.from_user.id))

# Main function
async def main():
    # Register handlers
    dp.message.register(start_command)
    dp.message.register(handle_buyurtma_berish)
    dp.message.register(handle_biz_haqimizda)
    dp.message.register(handle_orqaga)
    dp.message.register(handle_settings)
    dp.message.register(handle_langs)

    # Start polling
    await dp.start_polling(bot)

# Run the bot
run(main())
