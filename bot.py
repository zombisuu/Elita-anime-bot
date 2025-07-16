from aiogram import Bot, Dispatcher, types, executor
import os

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Bot ishlayapti ✅")

if __name__ == '__main__':
    executor.start_polling(dp)