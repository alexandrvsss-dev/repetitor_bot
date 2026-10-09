from os import getenv
import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from dotenv import load_dotenv
from database import cursor, conn
from keyboards import goal, class_kb, signup_kb, smena_kb
from handlers.routes import router

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(router)

#async def send_series( bot, user_id):
#    await asyncio.sleep (300)
#    await bot.send_message(user_id, "Е ")

#    await asyncio.sleep (300)
#    await bot.send_message(user_id, "П")

#    await asyncio.sleep (300)
#    await bot.send_message(user_id,"НХ")

#    await asyncio.sleep (300)
#    await bot.send_message(user_id, "В!")


async def main():
    bot = Bot(token=TOKEN)
    print("Старт...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
