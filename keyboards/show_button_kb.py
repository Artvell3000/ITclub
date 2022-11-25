from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('Показать')
b2 = KeyboardButton('Отмена')

kb_show = ReplyKeyboardMarkup(resize_keyboard=True)

kb_show.add(b1).add(b2)