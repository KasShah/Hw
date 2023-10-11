import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
from logging import basicConfig


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(Command('myinfo'))
async def info(message: types.Message):
    await message.answer(f'Ваш ID: {message.from_user.id}\n'
                         f'Ваше имя: {message.from_user.first_name}\n'
                         f'Ваше имя пользователя: {message.from_user.username}\n')

@dp.message(Command('image'))
async def image(message: types.Message):
    file = types.FSInputFile('image/galaxy.jpg')
    await message.answer_photo(file)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    basicConfig(level='INFO')
    asyncio.run(main())
