# Модуль для установки стандартных команд бота (вроде /start, /help)

from aiogram import types, Dispatcher

async def set_default_commands(dp : Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('desc', 'Описание колеса баланса'),
        types.BotCommand('dev', 'Разработчик'),
    ])