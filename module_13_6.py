import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Добро пожаловать! Выберите действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора:\n\n" +
                              "Для мужчин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n" +
                              "Для женщин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161")
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.answer('Введите свой возраст:')
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer('Введите свой рост:')

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer('Введите свой вес:')

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data.get('age', 0))
    growth = int(data.get('growth', 0))
    weight = int(data.get('weight', 0))

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий: {calories} калорий в день.')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)