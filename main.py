from aiogram.utils import executor
from create_bot import dp
#import os, json

async def on_startup(self):
    print('on startup')

from handlers import user, other, team

user.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)