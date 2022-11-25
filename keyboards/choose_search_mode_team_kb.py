from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/Искать_по_названию')
b2 = KeyboardButton('/Искать_по_умениям')
b3 = KeyboardButton('/Отмена')
kb_choose_search_mode_team = ReplyKeyboardMarkup(resize_keyboard=True)

kb_choose_search_mode_team.add(b1).add(b2).add(b3)