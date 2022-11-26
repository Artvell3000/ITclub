from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('продолжить')
kb_continue = ReplyKeyboardMarkup(resize_keyboard=True)

kb_continue.add(b1)