from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from asyncio import run

# Create bot and dispatcher instances
bot = Bot(token='7281122628:AAGTWPokuierPgxXfIS2AY0wletQyIdjqfk')
dp = Dispatcher()

# In-memory storage for user language preferences and greeting status
user_data = {}

# Translation dictionaries
translations = {
    "rus": {
        "meal": "Блюда 🍜",
        "drink": "Напитки 🍷",
        "salads": "Салаты 🥗",
        "desert": "Десерты 🍰",
        "tea": "Чаи 🫖",
        "start": "Здравствуйте, {name}",
        "hello": "Здравствуйте",
        "order": "🛍 Сделать заказ",
        "lang": "🌐 Изменить язык",
        "orders": "📦 Мои заказы",
        "settings": "⚙️ Настройки",
        "about": "ℹ️ О нас",
        "feedback": "✍️ Оставить отзыв",
        "choose_category": "С чего начнем?",
        "back": "⬅️ Назад",
        "main_menu": "🏠 Главное меню",
        "about_us": "Наша семья😊 очень давно занимается ресторанной кулинарией🥗🍕🍟🍣🍱. Мы известны великолепной аутентичной кухней, профессиональным шеф-поваром👨🏻‍🍳 и преданным персоналом👩‍🍳🧑‍🍳. Выберите любое блюдо из меню👨‍💻, которое поможет вам ощутить настоящий вкус пиццы🍕❤️.",
        "comment_prompt": "Для оформления заказа воспользуйтесь кнопкой «Заказать» в главном меню. \n Мы очень ценим ваш отзыв! После оформления заказа вы можете оставить здесь свои комментарии и отзывы.:",
        "comment_received": "Спасибо за ваш отзыв!",
        "category_items": {
            "meal": "Вот список блюд...",
            "drink": "Вот список напитков...",
            "salads": "Вот список салатов...",
            "desert": "Вот список десертов...",
            "tea": "Вот список чаев..."
        }
    },
    "uz": {
        "tea": "Choylar 🫖",
        "salads": "Salatlar 🥗",
        "desert": "Shirinliklar 🍰",
        "drink": "Ichimliklar 🍷",
        "meal": "Ovqatlar 🍜",
        "start": "Assalom alaykum, {name}",
        "hello": "Assalom alaykum",
        "order": "🛍 Buyurtma berish",
        "lang": "🌐 Tilni o'zgartirish",
        "orders": "📦 Buyurtmalarim",
        "settings": "⚙️ Sozlamalar",
        "about": "ℹ️ Biz haqimizda",
        "feedback": "✍️ Fikr qoldirish",
        "choose_category": "Nimadan boshlaymiz?",
        "back": "⬅️ Orqaga",
        "main_menu": "🏠 Bosh menyu",
        "about_us": "Наша семья😊очень давно занимается ресторанной кулинарией🥗🍕🍟🍣🍱 Мы известны великолепной аутентичной кухней, профессиональным шеф-поваром👨🏻‍🍳 и преданным персоналом👩‍🍳🧑‍🍳.Выберите любое блюдо из меню👨‍💻, которое поможет вам ощутить настоящий вкус пиццы🍕❤️.",
        "comment_prompt": "Buyurtma berish uchun asosiy menyudagi “Buyurtma” tugmasidan foydalaning. \n Biz sizning fikr-mulohazalaringizni juda qadrlaymiz! Buyurtma berganingizdan so'ng, o'z fikr va mulohazalaringizni shu yerda qoldirishingiz mumkin",
        "comment_received": "Fikringiz uchun rahmat!",
        "category_items": {
            "meal": "Ovqatlar ro'yxati...",
            "drink": "Ichimliklar ro'yxati...",
            "salads": "Salatlar ro'yxati...",
            "desert": "Shirinliklar ro'yxati...",
            "tea": "Choylar ro'yxati..."
        }
    }
}

# Product information
product_info = {
    "Mastava": {
        "description": "Мастава, цена: 20 000 сум",
        "image_url": "https://i2.wp.com/rusuz.com/wp-content/uploads/2017/09/Mastava-scaled.jpg?fit=1200%2C800&ssl=1"
    },
    "Qaynatma sho'rva(mol go'shti)": {
        "description": "Qaynatma sho'rva(mol go'shti), цена: 25 000 сум",
        "image_url": "https://i.ytimg.com/vi/WcNK5w5doxY/maxresdefault.jpg"
    },
    "Qaynatma sho'rva(qo'y go'shti)": {
        "description": "Qaynatma sho'rva(qo'y go'shti), цена: 20 000 сум",
        "image_url": "https://i.ytimg.com/vi/WcNK5w5doxY/maxresdefault.jpg"
    },
    # Add more product details as needed
}

# Function to get user language (default is 'uz')
def get_user_language(user_id):
    return user_data.get(user_id, {}).get("language", "uz")  # Default language is Uzbek

# Function to get translated text
def t(key, user_id, **kwargs):
    language = get_user_language(user_id)
    return translations[language][key].format(**kwargs)

# Define keyboard layout function
def get_keyboard(user_id):
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

def get_orqaga(user_id):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=t("back", user_id)),
            ],
        ],
        resize_keyboard=True
    )

def get_set_keyboard(user_id):
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

def get_meals_keyboard(user_id):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Qaynatma sho'rva(mol go'shti)"),
                KeyboardButton(text="Qaynatma sho'rva(qo'y go'shti)"),
            ],
            [
                KeyboardButton(text="Mastava"),
            ],
            [
                KeyboardButton(text=t("back", user_id)),
            ],
        ],
        resize_keyboard=True
    )


def get_lang_keyboard(user_id):
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
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=t("meal", user_id)),
                KeyboardButton(text=t("drink", user_id)),
            ],
            [
                KeyboardButton(text=t("salads", user_id)),
                KeyboardButton(text=t("desert", user_id)),
            ],
            [
                KeyboardButton(text=t("tea", user_id))
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
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if user_id not in user_data:
        user_data[user_id] = {"language": "uz", "greeted": False, "waiting_for_comment": False}

    if not user_data[user_id]["greeted"]:
        await message.answer(t("start", user_id, name=user_name), reply_markup=get_keyboard(user_id))
        user_data[user_id]["greeted"] = True
    else:
        await message.answer(t("hello", user_id), reply_markup=get_keyboard(user_id))

# Buyurtma berish handler
@dp.message(lambda message: message.text in [t("order", message.from_user.id)])
async def handle_buyurtma_berish(message: types.Message):
    await message.answer(t("choose_category", message.from_user.id), reply_markup=get_category_keyboard(message.from_user.id))

# Category handlers
@dp.message(lambda message: message.text in [t("meal", message.from_user.id)])
async def handle_meal(message: types.Message):
    await message.answer(translations[get_user_language(message.from_user.id)]["category_items"]["meal"], reply_markup=get_meals_keyboard(message.from_user.id))

@dp.message(lambda message: message.text in [t("drink", message.from_user.id)])
async def handle_drink(message: types.Message):
    await message.answer(translations[get_user_language(message.from_user.id)]["category_items"]["drink"], reply_markup=get_category_keyboard(message.from_user.id))

@dp.message(lambda message: message.text in [t("salads", message.from_user.id)])
async def handle_salads(message: types.Message):
    await message.answer(translations[get_user_language(message.from_user.id)]["category_items"]["salads"], reply_markup=get_category_keyboard(message.from_user.id))

@dp.message(lambda message: message.text in [t("desert", message.from_user.id)])
async def handle_desert(message: types.Message):
    await message.answer(translations[get_user_language(message.from_user.id)]["category_items"]["desert"], reply_markup=get_category_keyboard(message.from_user.id))

@dp.message(lambda message: message.text in [t("tea", message.from_user.id)])
async def handle_tea(message: types.Message):
    await message.answer(translations[get_user_language(message.from_user.id)]["category_items"]["tea"], reply_markup=get_category_keyboard(message.from_user.id))

# Biz haqimizda handler
@dp.message(lambda message: message.text in [t("about", message.from_user.id)])
async def handle_biz_haqimizda(message: types.Message):
    await message.answer(t("about_us", message.from_user.id), reply_markup=get_keyboard(message.from_user.id))

# Orqaga handler
@dp.message(lambda message: message.text in [t("back", message.from_user.id)])
async def handle_orqaga(message: types.Message):
    await message.answer(t("main_menu", message.from_user.id), reply_markup=get_keyboard(message.from_user.id))

@dp.message(lambda message: message.text in [t("settings", message.from_user.id)])
async def handle_settings(message: types.Message):
    await message.answer(t("settings", message.from_user.id), reply_markup=get_set_keyboard(message.from_user.id))

@dp.message(lambda message: message.text in [t("lang", message.from_user.id)])
async def handle_langs(message: types.Message):
    await message.answer("Choose your language", reply_markup=get_lang_keyboard(message.from_user.id))

# Language change handlers
@dp.message(lambda message: message.text == "🇺🇿 O'zbekcha")
async def switch_to_uzbek(message: types.Message):
    user_data[message.from_user.id]["language"] = "uz"
    await message.answer("Til o'zbek tiliga o'zgartirildi.", reply_markup=get_keyboard(message.from_user.id))

@dp.message(lambda message: message.text == "🇷🇺 Русский")
async def switch_to_russian(message: types.Message):
    user_data[message.from_user.id]["language"] = "rus"
    await message.answer("Язык изменен на русский.", reply_markup=get_keyboard(message.from_user.id))

# Feedback handler
@dp.message(lambda message: message.text in [t("feedback", message.from_user.id)])
async def handle_feedback(message: types.Message):
    user_data[message.from_user.id]["waiting_for_comment"] = True
    await message.answer(t("comment_prompt", message.from_user.id), reply_markup=get_orqaga(message.from_user.id))

@dp.message(lambda message: user_data.get(message.from_user.id, {}).get("waiting_for_comment", False))
async def receive_comment(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["waiting_for_comment"] = False
    # You can save the comment to a database or perform any other actions here
    await message.answer(t("comment_received", user_id), reply_markup=get_keyboard(user_id))

# Product information handler
@dp.message(lambda message: message.text in product_info)
async def handle_product_info(message: types.Message):
    product = product_info[message.text]
    description = product["description"]
    image_url = product["image_url"]
    
    await message.answer(description, reply_markup=get_meals_keyboard(message.from_user.id))
    await message.answer_photo(photo=image_url)

# Main function
async def main():
    # Register handlers
    dp.message.register(start_command)
    dp.message.register(handle_buyurtma_berish)
    dp.message.register(handle_meal)
    dp.message.register(handle_drink)
    dp.message.register(handle_salads)
    dp.message.register(handle_desert)
    dp.message.register(handle_tea)
    dp.message.register(handle_biz_haqimizda)
    dp.message.register(handle_orqaga)
    dp.message.register(handle_settings)
    dp.message.register(handle_langs)
    dp.message.register(switch_to_uzbek)
    dp.message.register(switch_to_russian)
    dp.message.register(handle_feedback)
    dp.message.register(receive_comment)
    dp.message.register(handle_product_info)

    # Start polling
    await dp.start_polling(bot)

# Run the bot
run(main())