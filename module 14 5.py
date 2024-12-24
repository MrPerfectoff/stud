from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products, add_user, is_included

API_TOKEN = '7938815284:AAHp1mJaKpvE7a0sNXPs784F26izYZDcUbM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
button_register = KeyboardButton('Регистрация')  # Кнопка регистрации
keyboard.add(button_calculate, button_info, button_buy, button_register)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Добро пожаловать! Выберите действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text.lower() == 'регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if not is_included(username):
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя:")
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    data = await state.get_data()
    username = data.get('username')
    email = data.get('email')

    add_user(username, email, age)  # Добавление пользователя в БД
    await message.answer("Вы успешно зарегистрированы!")
    await state.finish()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Новое Inline меню для покупки
buy_inline_keyboard = InlineKeyboardMarkup()
button_product1 = InlineKeyboardButton('Product1', callback_data='product_buying')
button_product2 = InlineKeyboardButton('Product2', callback_data='product_buying')
button_product3 = InlineKeyboardButton('Product3', callback_data='product_buying')
button_product4 = InlineKeyboardButton('Product4', callback_data='product_buying')
buy_inline_keyboard.add(button_product1, button_product2, button_product3, button_product4)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Добро пожаловать! Выберите действие:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)


@dp.message_handler(lambda message: message.text.lower() == 'купить')
async def get_buying_list(message: types.Message):
    products_info = [
        (1, "Product1", "описание 1", 100, 'https://www.ozon.ru/search/?deny_category_prediction=true&from_global=true&text=%D0%96%D0%B8%D1%80%D0%BE%D1%81%D0%B6%D0%B8%D0%B3%D0%B0%D1%82%D0%B5%D0%BB%D1%8C&product_id=1428436112'),
        (2, "Product2", "описание 2", 200, 'https://aliexpress.ru/item/1005006872524676.html?sku_id=12000038581789141'),
        (3, "Product3", "описание 3", 300, 'https://global.wildberries.ru/product/tabletki-dlya-pokhudeniya-zhiroszhigatel-53636598'),
        (4, "Product4", "описание 4", 400, 'https://www.wildberries.ru/catalog/28664230/detail.aspx')
    ]

    for number, name, description, price, image_url in products_info:
        await message.answer(f'Название: {name} | Описание: {description} | Цена: {price} руб.')
        await bot.send_photo(message.chat.id, photo=image_url)

    await message.answer("Выберите продукт для покупки:", reply_markup=buy_inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)