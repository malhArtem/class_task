from aiogram import Router, types
from aiogram.filters import Command

import db

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    db.add_user(message.from_user.id,
                message.from_user.username,
                message.from_user.first_name,
                message.from_user.last_name)

