from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_balance_wheel = KeyboardButton('✍ Составить колесо баланса')
kb_main.add(kb_balance_wheel)