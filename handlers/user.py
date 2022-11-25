from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot

from keyboards.choose_mode_kb import kb_choose_mode
from keyboards.choose_search_mode_team_kb import kb_choose_search_mode_team
from keyboards.search_res_kb import kb_res
from keyboards.show_button_kb import kb_show

class FSMUser(StatesGroup):
    input_skills = State()
    viewing = State()


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'okey', reply_markup=kb_choose_mode) #, reply_markup = ReplyKeyboardRemove())

async def command_begin_search(message: types.Message):
    await bot.send_message(message.from_user.id, 'okey', reply_markup=kb_choose_search_mode_team)

async def input_skills(message: types.Message):
    await FSMUser.input_skills.set()
    await bot.send_message(message.from_user.id, 'напиши необходимые умения', reply_markup=ReplyKeyboardRemove())

async def parse_skills(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['skills'] = message.text
    await FSMUser.viewing.set()
    await bot.send_message(message.from_user.id, 'найдено x команд', reply_markup=kb_show)

async def show_res(message: types.Message, state: FSMContext):
    if(message.text == 'Next' or message.text == 'Показать'):
        await FSMUser.viewing.set()
        await bot.send_message(message.from_user.id, 'типо анкета', reply_markup=kb_res)
    if(message.text == 'Отмена'):
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await bot.send_message(message.from_user.id, 'я вернул вас на главную', reply_markup=kb_choose_mode)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state=None)
    dp.register_message_handler(command_begin_search, commands=['Искать_команду'], state=None)
    dp.register_message_handler(input_skills, commands=['Искать_по_умениям'], state=None)
    dp.register_message_handler(parse_skills, state=FSMUser.input_skills)
    dp.register_message_handler(show_res, state=FSMUser.viewing)

