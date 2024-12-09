from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7938815284:AAHp1mJaKpvE7a0sNXPs784F26izYZDcUbM"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(text = ["Urban", 'ff'])
async def urban_message(message):
    print("Urban Message")
    await  message.answer("Urban message!")

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет, я бот помогающий твоему здоровью')
    await message.answer("Привет, я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_message(message):
   print("Введите команду /start, что бы начать общение")
   await message.answer('Введите команду /start что бы начать общение')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)