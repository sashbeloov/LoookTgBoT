import aiogram
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message
import asyncio
from data_dict import lang_data, uz, en, ru
from random import randint

TOKEN = "7611119839:AAHdiDZ9-olh2EldSCKdE6ktewlhFYvIs3M"

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}



@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start" or message.text == "O'zbekcha" or message.text == "🗂 | Asosiy menu":
        await start(message)
    elif message.text == "🛍 Buyurtma berish" or message.text == "🛍 Order" or message.text == "🛍 Заказать":
        await order(message)
    elif message.text == "⚙️ Sozlamalar" or message.text == "⚙️ Settings" or message.text == "⚙️ Настройки":
        await setting_all(message)
    elif message.text == "ℹ️ Biz haqimizda" or message.text == "ℹ️ About us" or message.text == "ℹ️ О нас":
        await setting_aboutus(message)
    elif message.text == "📋 Mening buyurtmalarim" or message.text == "📋 My orders" or message.text == "📋 Мои заказы":
        await myorders(message)
    elif message.text == "✍️Izoh qoldirish" or message.text == "✍️ Leave feedback" or message.text == "✍️ Оставить отзыв":
        await reviews(message)
    elif message.text == "🇺🇿 Tilni o'zgartirish" or message.text == "🇺🇸 Change language" or message.text == "🇷🇺 Выберите язык":
        await change_languege(message)
        if "holat" in user_data[user_id]:
            del user_data[user_id]["holat"]
        elif "holateng" in user_data[user_id]:
            del user_data[user_id]["holateng"]
        elif "holatru" in user_data[user_id]:
            del user_data[user_id]["holatru"]
    elif message.text == "⬅️ Orqaga" or message.text == "⬅️  back" or message.text == "⬅️  Назад":
        await checkback(message)
    elif message.text in en or message.text in ru or message.text == "🗂 | Main menu" or message.text == "🗂 | Главное меню":
        await check_lang(message)
    elif message.text == "Tug'ilgan kunni qo'shish" or  message.text == "Add birthday" or message.text == "Добавить день рождения":
        await birthday(message)
    elif "birthdays" in user_data[user_id] or "birthdayseng" in user_data[user_id] or "birthdaysru" in user_data[user_id]:
        await check_birthday(message)
    elif message.text == "Telefon raqamni o'zgartirish" or message.text == "Change phone number" or message.text == "Изменить номер телефона":
        await ask_phone(message)
    elif "phone" in user_data[user_id]:
        await check_phone(message)
    elif int(message.text) == user_data[user_id]["ver_code"]:
        pass



@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🛍 Buyurtma berish")],
        [types.KeyboardButton(text="⚙️ Sozlamalar"),types.KeyboardButton(text="ℹ️ Biz haqimizda")],
        [types.KeyboardButton(text="📋 Mening buyurtmalarim"),types.KeyboardButton(text="✍️Izoh qoldirish")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing \n\n"
        "Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin",
        reply_markup=keyboard)
    print(1,user_data)




async def order(message: types.Message,):
    user_id = message.from_user.id
    try:
        if message.text in uz:
            user_data[user_id]['holat'] = "order"
            user_data[user_id]["language"] = "uz"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                            [types.KeyboardButton(text=f"{res[0]}"),types.KeyboardButton(text=f"{res[1]}")],
                            [types.KeyboardButton(text=f"{res[2]}")],
                        ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[3]}",reply_markup=keyboard)
            print(2,user_data)
        elif message.text in en:
            user_data[user_id]['holateng'] = "order"
            user_data[user_id]["language"] = "en"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                            [types.KeyboardButton(text=f"{res[0]}"),types.KeyboardButton(text=f"{res[1]}")],
                            [types.KeyboardButton(text=f"{res[2]}")],
                        ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[3]}",reply_markup=keyboard)
            print(2,user_data)
        elif message.text in ru:
            user_data[user_id]['holatru'] = "order"
            user_data[user_id]["language"] = "ru"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                            [types.KeyboardButton(text=f"{res[0]}"),types.KeyboardButton(text=f"{res[1]}")],
                            [types.KeyboardButton(text=f"{res[2]}")],
                        ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[3]}",reply_markup=keyboard)
            print(2,user_data)
    except Exception as e:
        print(f"order:Xatolik yuz berdi: {e}")



async def setting_all(message: types.Message,):
    user_id = message.from_user.id
    try:
        if message.text in uz:
            user_data[user_id]['holat'] = "setting_all"
            user_data[user_id]["language"] = "uz"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}")],
                [types.KeyboardButton(text=f"{res[2]}"), types.KeyboardButton(text=f"{res[3]}")],
                        ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[4]}", reply_markup=keyboard)
            print(3, user_data)
        elif message.text in en:
            user_data[user_id]["language"] = "en"
            user_data[user_id]['holateng'] = "setting_all"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}")],
                [types.KeyboardButton(text=f"{res[2]}"), types.KeyboardButton(text=f"{res[3]}")],
                        ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[4]}", reply_markup=keyboard)
            print(3, user_data)
        elif message.text in ru:
            user_data[user_id]['holatru'] = "setting_all"
            user_data[user_id]["language"] = "ru"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}")],
                [types.KeyboardButton(text=f"{res[2]}"), types.KeyboardButton(text=f"{res[3]}")],
                        ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[4]}", reply_markup=keyboard)
            print(3, user_data)
    except Exception as e:
        print(f"setting_all:Xatolik yuz berdi: {e}")


async def setting_aboutus(message: types.Message,):
    user_id = message.from_user.id
    try:
        if message.text in uz:
            user_data[user_id]['holat'] = "setting_aboutus"
            user_data[user_id]["language"] = "uz"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
        elif message.text in en:
            user_data[user_id]["language"] = "en"
            user_data[user_id]['holateng'] = "setting_aboutus"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
        elif message.text in ru:
            user_data[user_id]['holatru'] = "setting_aboutus"
            user_data[user_id]["language"] = "ru"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
    except Exception as e:
        print(f"setting_aboutus:xatolik yuz berdi: {e}")


async def myorders(message: types.Message,):
    user_id = message.from_user.id
    try:
        if message.text in uz:
            user_data[user_id]['holat'] = "myorders"
            user_data[user_id]["language"] = "uz"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
        elif message.text in en:
            user_data[user_id]["language"] = "en"
            user_data[user_id]['holateng'] = "myorders"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
        elif message.text in ru:
            user_data[user_id]['holatru'] = "myorders"
            user_data[user_id]["language"] = "ru"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
    except Exception as e:
        print(f"myorders:xatolik yuz berdi: {e}")



async def reviews(message: types.Message,):
    user_id = message.from_user.id
    try:
        if message.text in uz:
            user_data[user_id]['holat'] = "reviews"
            user_data[user_id]["language"] = "uz"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
        elif message.text in en:
            user_data[user_id]["language"] = "en"
            user_data[user_id]['holateng'] = "reviews"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
        elif message.text in ru:
            user_data[user_id]['holatru'] = "reviews"
            user_data[user_id]["language"] = "ru"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[1]}", reply_markup=keyboard)
            print(user_data)
    except Exception as e:
        print(f"reviews:xatolik yuz berdi: {e}")



async def change_languege(message: types.Message):
    user_id = message.from_user.id
    try:
        if user_data[user_id]["language"] == "uz":
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}"), types.KeyboardButton(text=f"{res[2]}")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[3]}", reply_markup=keyboard)
            print(4, user_data)
        elif user_data[user_id]["language"] == "en":
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}"), types.KeyboardButton(text=f"{res[2]}")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[3]}", reply_markup=keyboard)
            print(4, user_data)
        elif user_data[user_id]["language"] == "ru":
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}"), types.KeyboardButton(text=f"{res[2]}")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[3]}", reply_markup=keyboard)
            print(4, user_data)
    except Exception as e:
        print(f"change_languege:Xatolik yuz berdi: {e}")


async def birthday(message: types.Message):
    user_id = message.from_user.id
    try:
        if user_data[user_id]["language"] == "uz":
            user_data[user_id]['holat'] = "birthday"
            if "birthdays" not in user_data[user_id]:
                user_data[user_id]['birthdays'] = "birthdays"
            else:
                user_data[user_id]['birthdays'] = "birthdays"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[2]}", reply_markup=keyboard)
            print(user_data)
        elif user_data[user_id]["language"] == "en":
            user_data[user_id]['holateng'] = "birthday"
            if "birthdayseng" not in user_data[user_id]:
                user_data[user_id]['birthdayseng'] = "birthdayseng"
            else:
                user_data[user_id]['birthdayseng'] = "birthdayseng"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[2]}", reply_markup=keyboard)
            print(user_data)
        elif user_data[user_id]["language"] == "ru":
            user_data[user_id]['holatru'] = "birthday"
            if "birthdaysru" not in user_data[user_id]:
                user_data[user_id]['birthdaysru'] = "birthdaysru"
            else:
                user_data[user_id]['birthdaysru'] = "birthdaysru"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}"), types.KeyboardButton(text=f"{res[1]}")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[2]}", reply_markup=keyboard)
            print(user_data)
    except Exception as e:
        print(f"birthday:Xatolik yuz berdi: {e}")




async def check_birthday(message: types.Message):
    user_id = message.from_user.id
    numbers = "-0123456789"
    text =str(message.text)
    ok = True
    try:
        if user_data[user_id]["language"] == "uz":
            lang = user_data[user_id]["language"]
            if len(text) == 10 and text[2] == "-" and text[5] == "-":
                for i in text:
                    if i not in numbers:
                        await message.answer(f"{lang_data[lang][0]}")
                        await message.answer(f"{lang_data[lang][1]}")
                        ok = False
                        break
                if ok == True:
                    user_data[user_id]["birthday"] = text
                    await message.answer(f"{lang_data[lang][2]}")
            else:
                await message.answer(f"{lang_data[lang][0]}")
                await message.answer(f"{lang_data[lang][1]}")
        elif user_data[user_id]["language"] == "en":
            lang = user_data[user_id]["language"]
            if len(text) == 10 and text[2] == "-" and text[5] == "-":
                for i in text:
                    if i not in numbers:
                        await message.answer(f"{lang_data[lang][0]}")
                        await message.answer(f"{lang_data[lang][1]}")
                        ok = False
                        break
                if ok == True:
                    user_data[user_id]["birthday"] = text
                    await message.answer(f"{lang_data[lang][2]}")
            else:
                await message.answer(f"{lang_data[lang][0]}")
                await message.answer(f"{lang_data[lang][1]}")
        elif user_data[user_id]["language"] == "ru":
            lang = user_data[user_id]["language"]
            if len(text) == 10 and text[2] == "-" and text[5] == "-":
                for i in text:
                    if i not in numbers:
                        await message.answer(f"{lang_data[lang][0]}")
                        await message.answer(f"{lang_data[lang][1]}")
                        ok = False
                        break
                if ok == True:
                    user_data[user_id]["birthday"] = text
                    await message.answer(f"{lang_data[lang][2]}")
            else:
                await message.answer(f"{lang_data[lang][0]}")
                await message.answer(f"{lang_data[lang][1]}")
    except Exception as e:
        print(f"check_birthday:Xatolik yuz berdi: {e}")



async def ask_phone(message: types.Message):
    user_id = message.from_user.id
    try:
        if message.text:
            if "phone" not in user_data[user_id]:
                user_data[user_id]['phone'] = "phone"
            else:
                user_data[user_id]['phone'] = "phone"
            user_data[user_id]["holat"] = "ask_phone"
            lang = user_data[user_id]["language"]
            res = lang_data[message.text][lang]
            button = [
                [types.KeyboardButton(text=f"{res[0]}", request_contact=True),],
                [types.KeyboardButton(text=f"{res[1]}"),],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{res[2]}", reply_markup=keyboard)
            print(user_data)
    except Exception as e:
        print(f"check_phone:Xatolik yuz berdi: {e}")


async def check_phone(message: types.Message):
    user_id = message.from_user.id
    nums = "+0123456789"
    state = True
    try:
        if message.text:
            text = message.text
            lang = user_data[user_id]["language"]
            if len(text) == 13 and text[0:4] == "+998":
                for i in text:
                    if i not in nums:
                        await message.answer(f"{lang_data[lang][6]}")
                        state = False
                        break
                if state == True:
                    button = [
                        [types.KeyboardButton(text=f"{lang_data[lang][4]}")],
                        [types.KeyboardButton(text=f"{lang_data[lang][5]}")],
                    ]
                    user_data[user_id]["user_phone_number:"] = text
                    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
                    ver_code = randint(100000, 999999)
                    user_data[user_id]["ver_code:"] = ver_code
                    await message.answer(f"{lang_data[lang][3]}: {ver_code}", reply_markup=keyboard)
                    print(user_data)
            else:
                await message.answer(f"{lang_data[lang][6]}")
    except Exception as e:
        print(f"check_phone:Xatolik yuz berdi: {e}")



async def check_lang(message: types.Message):
    user_id = message.from_user.id
    try:
        if message.text in en:
            button = [
                [types.KeyboardButton(text=f"{en[1]}")],
                [types.KeyboardButton(text=f"{en[2]}"), types.KeyboardButton(text=f"{en[3]}")],
                [types.KeyboardButton(text=f"{en[4]}"), types.KeyboardButton(text=f"{en[5]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{en[6]}", reply_markup=keyboard)
            print(5, user_data)
        elif message.text in ru:
            button = [
                [types.KeyboardButton(text=f"{ru[1]}")],
                [types.KeyboardButton(text=f"{ru[2]}"), types.KeyboardButton(text=f"{ru[3]}")],
                [types.KeyboardButton(text=f"{ru[4]}"), types.KeyboardButton(text=f"{ru[5]}")]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
            await message.answer(f"{ru[6]}", reply_markup=keyboard)
            print(user_data)
    except Exception as e:
        print(f"check_lang:Xatolik yuz berdi: {e}")



async def checkback(message: types.Message):
    user_id = message.from_user.id
    if message.text == "⬅️ Orqaga" and "holat" in user_data[user_id]:
        if user_data[user_id]["holat"] == "order" or user_data[user_id]["holat"] == "setting_all":
            await start(message)
        elif user_data[user_id]['holat'] == "setting_aboutus" or user_data[user_id]['holat'] == "myorders" or user_data[user_id]['holat'] == "reviews":
            await start(message)
        elif user_data[user_id]['holat'] == "birthday" or user_data[user_id]["holat"] == "ask_phone":
            await setting_all(message)
            del user_data[user_id]["phone"]
    elif message.text == "⬅️  back" and 'holateng'in user_data[user_id]:
        if user_data[user_id]['holateng'] == "order" or user_data[user_id]['holateng'] == "setting_all":
            await check_lang(message)
        elif user_data[user_id]['holateng'] == "setting_aboutus" or user_data[user_id]['holateng'] == "myorders" or user_data[user_id]['holateng'] == "reviews":
            await check_lang(message)
        elif user_data[user_id]['holateng'] == "birthday":
            await setting_all(message)
    elif message.text == "⬅️  Назад" and 'holatru'in user_data[user_id]:
        if user_data[user_id]['holatru'] == "order" or user_data[user_id]['holatru'] == "setting_all":
            await check_lang(message)
        elif user_data[user_id]['holatru'] == "setting_aboutus" or user_data[user_id]['holatru'] == "myorders" or user_data[user_id]['holatru'] == "reviews":
            await check_lang(message)
        elif user_data[user_id]['holatru'] == "birthday":
            await setting_all(message)






async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())