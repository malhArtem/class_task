import asyncio
from aiogram import Bot, Dispatcher, types, F
import db_users as db

bot = Bot("7511369929:AAFMoEisfUCs9ftNz5dvu8NelAbH6K4vrFo")
dp = Dispatcher()

@dp.message(F.text=="/start")
async def start(message: types.Message):
    db.add_user(message.from_user.id,
                message.from_user.username,
                message.from_user.first_name,
                message.from_user.last_name)

    await message.answer("Вы сохранены в бд")


@dp.message(F.text=="/users")
async def users_handler(message: types.Message):
    users = db.get_all_users()
    text = ''
    for i, user in enumerate(users):
        text += f"{i + 1}. {user.username}({user.id}): {user.first_name} {user.last_name} \n"
    await message.answer(text)

async def main():
    db.create_table()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())