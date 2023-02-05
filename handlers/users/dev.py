from aiogram import Dispatcher, types

DEV_COMMAND = '''
<b>Разработчик🔧</b>
@katsuyorii
'''

async def dev_command(message : types.Message):
    await message.answer(DEV_COMMAND)

async def register_dev_command(dp : Dispatcher):
    dp.register_message_handler(dev_command, commands=['dev'])