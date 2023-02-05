import os
from dotenv import load_dotenv 
from dataclasses import dataclass

@dataclass
class TgBotConfig:
    token : str # Токен API бота
    admins_id : str # ID администраторов бота

@dataclass
class Config:
    tg_bot : TgBotConfig # Конфиг телеграмм бота

load_dotenv() # Загружает переменную из .env в переменные окружения

config = Config(tg_bot = TgBotConfig(token = str(os.getenv("BOT_TOKEN")), admins_id = str(os.getenv("ADMIN_ID"))))
