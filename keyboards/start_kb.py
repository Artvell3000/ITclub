from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

async def create_start_kb(reg):
    b1 = KeyboardButton('/Создать_аккаунт') if not reg else KeyboardButton('/Продолжить')
    kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_start.add(b1)
    return kb_start

