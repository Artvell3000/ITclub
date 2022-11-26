from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('да')
b2 = KeyboardButton('нет')
b3 = KeyboardButton('/отмена')
kb_YesNo = ReplyKeyboardMarkup(resize_keyboard=True)

kb_YesNo.add(b1).add(b2).add(b3)