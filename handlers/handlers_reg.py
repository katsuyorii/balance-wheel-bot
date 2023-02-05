from aiogram import Dispatcher
from handlers.users.start import register_start_command
from handlers.users.dev import register_dev_command
from handlers.users.desc import register_desc_command
from handlers.users.wheel_generate import register_wheel_gen_echo

async def register_all_handlers(dp : Dispatcher):
    await register_start_command(dp)
    await register_dev_command(dp)
    await register_desc_command(dp)
    await register_wheel_gen_echo(dp)
    