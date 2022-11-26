from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot

from keyboards.start_kb import create_start_kb
from keyboards.YesNo_kb import kb_YesNo
from keyboards.button_continue import kb_continue

class FSMUserSearching(StatesGroup):
    input_skills = State()
    viewing = State()

class FSMUserRegis(StatesGroup):
    create_acc = State()
    name = State()
    has_team = State()
    skills = State()
    telegram = State()
    description = State()
    correct = State()


async def command_start(message: types.Message):
    #запрос в бд
    reg = False
    kb = await create_start_kb(reg)
    mes = "Привет! A я тебя помню :)" if reg else "Я тебя впервые вижу..."
    await bot.send_message(message.from_user.id, mes, reply_markup=kb) #, reply_markup = ReplyKeyboardRemove())

async def command_create_acc(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
    await FSMUserRegis.name.set()
    await bot.send_message(message.from_user.id, "Как мне тебя называть?", reply_markup=ReplyKeyboardRemove())

async def input_name_acc(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMUserRegis.has_team.set()
    await bot.send_message(message.from_user.id, "У тебя ужe есть команда?", reply_markup=kb_YesNo)

async def input_has_team(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'да':
            data['has_team'] = True
        elif message.text == 'нет':
            data['has_team'] = False

    await FSMUserRegis.skills.set()
    await bot.send_message(message.from_user.id, "Отправь все свои умения", reply_markup=ReplyKeyboardRemove())

async def input_skills(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['skills'] = message.text
    await FSMUserRegis.description.set()
    await bot.send_message(message.from_user.id, "Опиши себя")

async def input_description(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMUserRegis.telegram.set()
    await bot.send_message(message.from_user.id, "Отлично! Отправь мне свой телеграмм, чтобы с тобой могли связаться другие участники")

async def input_tg(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['telegram'] = message.text
    await FSMUserRegis.correct.set()
    #kb = await create_start_kb(False)
    await bot.send_message(message.from_user.id, "Я всё записал", reply_markup=kb_continue)

async def correct_acc(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        s = ''
        for i in data:
            s += (str(i) + ':' + str(data[i]) + '\n')

    await state.finish()
    await bot.send_message(message.from_user.id, s, reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state=None)
    dp.register_message_handler(command_create_acc, commands=['Создать_аккаунт'], state=None)
    dp.register_message_handler(input_name_acc, state=FSMUserRegis.name)
    dp.register_message_handler(input_has_team, state=FSMUserRegis.has_team)
    dp.register_message_handler(input_skills, state=FSMUserRegis.skills)
    dp.register_message_handler(input_description, state=FSMUserRegis.description)
    dp.register_message_handler(input_tg, state=FSMUserRegis.telegram)
    dp.register_message_handler(correct_acc, state=FSMUserRegis.correct)

