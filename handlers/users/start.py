from aiogram import Dispatcher, types
from keyboards.default.replyKb_main import kb_main

START_COMMAND = '''
<b>Здравствуй!👋
Я бот по созданию колеса баланса!</b>🎡
'''

async def start_command(message : types.Message):
    await message.answer(START_COMMAND, reply_markup=kb_main)

async def register_start_command(dp : Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])