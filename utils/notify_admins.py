# Модуль с уведомлениями администраторов бота о запуске бота

import logging
from aiogram import Dispatcher
from data.config import config

async def on_startup_notify(dp : Dispatcher):
    try:
        text = 'Bot was started!'
        await dp.bot.send_message(config.tg_bot.admins_id, text)
    except Exception as error:
        logging.exception(error)