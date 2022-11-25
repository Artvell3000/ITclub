from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/Искать_команду')
b2 = KeyboardButton('/Искать_участников')
b3 = KeyboardButton('/Администрировать_команду')

kb_choose_mode = ReplyKeyboardMarkup(resize_keyboard=True)

kb_choose_mode.row(b1, b2).add(b3)

