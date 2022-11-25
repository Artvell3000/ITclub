from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('Next')
b2 = KeyboardButton('Отмена')

kb_res = ReplyKeyboardMarkup(resize_keyboard=True)

kb_res.add(b1).add(b2)