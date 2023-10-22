import asyncio
from aiogram.types import BotCommand
from logging import basicConfig
from bot import dp, bot
from handlers.start import start_router
from handlers.myinfo import info_router
from handlers.image import img_router
from handlers.faculties import faculties_router

async def main():
    await bot.set_my_commands(
        [
           BotCommand(command='start', description='Запустить бота'),
           BotCommand(command='image', description='Отправить картинку'),
           BotCommand(command='myinfo', description='Показать данные'),
           BotCommand(command='faculties', description='Открыть факультеты')
        ]
    )

    dp.include_router(img_router)
    dp.include_router(info_router)
    dp.include_router(start_router)
    dp.include_router(faculties_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    basicConfig(level='INFO')
    asyncio.run(main())
