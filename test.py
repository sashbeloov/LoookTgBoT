# import aiogram
# from aiogram import types, Bot, Dispatcher
# from aiogram.filters import Command
# import asyncio
#
# from pyexpat.errors import messages
#
# TOKEN = "7702041998:AAGYq7SjeufGnJQ4OFAr2zrzqVP7VyD6nCM"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# list_ortga = []
#
# user_data = {}
#
# lang_data = {
#     "🇺🇿 O'zbekcha":
#         ["Toshkent","Samarqand","Jizax","Buxoro","Shaxarni tanlang:","🛍 Buyurtma berish","menuni tanlang","⬅️ Ortga", "📖 Buyurtmalar tarixi","⚙️Sozlash ℹ️ Ma'lumotlar","✅ Raqamni jo'natish","Sizning telefon raqamingiz:"],
#     "🇷🇺 Русский":
#         ["Ташкент","Самарканд","Джиззах","Бухара","Виберите город:","🛍 сделать заказ","виберите меню","⬅️ назад","📖 Мои заказы", "⚙️Настройки ℹ️ Информация","✅ Отправить номер","ваш номер телефона:"],
#     "🇺🇸 English":
#         ["Tashkent","Samarqand","Jizakh","Bukhara","Choose the city:","🛍 give order","choose menu","⬅️ back", "📖 My orders","⚙️Settings ℹ️ Information","✅ Send phone number","Your phone number:"],
#     "⬅️ Ortga":
#         ["Toshkent", "Samarqand", "Jizax", "Buxoro", "Shaxarni tanlang:", "🛍 Buyurtma berish", "menuni tanlang","⬅️ Ortga","📖 Buyurtmalar tarixi","⚙️Sozlash ℹ️ Ma'lumotlar","✅ Raqamni jo'natish","Sizning telefon raqamingiz:"],
#     "⬅️ назад":
#         ["Ташкент","Самарканд","Джиззах","Бухара","Виберите город:","🛍 сделать заказ","виберите меню","⬅️ назад", "📖 Мои заказы", "⚙️Настройки ℹ️ Информация","✅ Отправить номер","ваш номер телефона:"],
#     "⬅️ back":
#         ["Tashkent", "Samarqand", "Jizakh", "Bukhara", "Choose the city:", "🛍 give order", "choose menu", "⬅️ back",
#          "📖 My orders", "⚙️Settings ℹ️ Information", "✅ Send phone number","Your phone number:"],
# }
#
# cities = ["Toshkent","Samarqand","Jizax","Buxoro","Ташкент","Самарканд","Джиззах","Бухара","Tashkent","Samarqand","Jizakh","Bukhara"]
#
# ortgadict = {
#     "⬅️ Ortga":"⬅️ Ortga",
#     "⬅️ назад":"⬅️ назад",
#     "⬅️ back":"⬅️ back",
# }
#
# @dp.message()
# async def handle_text(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_data or message.text == "/start":
#         await start(message)
#     elif message.text in lang_data:
#         await chooce_city(message)
#     elif message.text in ortgadict:   # ortga tekshirilmoqda
#         til = ortgadict[message.text]
#         if user_data[user_id]['holat'] == 'main':
#             await chooce_city(message)
#         elif user_data[user_id]['holat'] == 'next':
#             await main_menu(message)
#     elif message.text in cities:
#         await main_menu(message)
#     elif message.text in lang_data[user_data[user_id]["choose_lang"]][5]:
#         await next_menu(message)
#     elif 'phone_number' in user_data[user_id]:
#         print("bu funksiyaga keldi")
#         await num_check(message)
#
#
#
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id] = {}
#     button = [
#         [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
#          types.KeyboardButton(text="🇺🇸 English")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#     await message.answer(
#         "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n\n"
#         "Здравствуйте! Добро пожаловать в службу доставки Les Ailes.\n\n"
#         "Hello! Welcome to Les Ailes delivery service.",
#         reply_markup=keyboard)
#     print(1, user_data)
#
#
# async def chooce_city(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id]["choose_lang"] = message.text  # uzb yoki rus yoki ,eng saqlanadi
#     text = message.text
#     if message.text in ortgadict:
#         phone.clear()
#     if text in lang_data:
#         button = [
#             [types.KeyboardButton(text=lang_data[text][0]), types.KeyboardButton(text=lang_data[text][1])],
#             [types.KeyboardButton(text=lang_data[text][2]), types.KeyboardButton(text=lang_data[text][3])],
#         ]
#         keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#         await message.answer(
#             f"{lang_data[text][4]}",
#             reply_markup=keyboard)
#         print(1, user_data)
#
#
# phone = []
# async def main_menu(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id]['holat'] = 'main'
#     lang1 = user_data[user_id]["choose_lang"]   # boshida tanlangan til bo'yicha til boyicha list chiqarib olinmoqda
#     ortga = lang_data[lang1][7]
#     if message.text in ortgadict:
#         phone.clear()
#     if message.text in lang_data[lang1]:       # lang_data dan ro'yhat chiqib kelmoqda va uni ichidan qidirilmoqda
#         button = [
#             [types.KeyboardButton(text=lang_data[lang1][5]),types.KeyboardButton(text=lang_data[lang1][8]),],
#             [types.KeyboardButton(text=lang_data[lang1][9]),types.KeyboardButton(text=lang_data[lang1][7]),],
#
#         ]
#         keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#         await message.answer(
#             f"{lang_data[lang1][6]}",
#             reply_markup=keyboard)
#         print(2, user_data)
#
#
#
# async def next_menu(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id]['holat'] = 'next'
#     lang1 = user_data[user_id]["choose_lang"]
#
#     list_ortga.append(message)
#     if message.text in ortgadict:
#         phone.clear()
#     button = [
#         [types.InlineKeyboardButton(text="1️⃣",callback_data='one'), types.InlineKeyboardButton(text="2️⃣",callback_data='two'),types.InlineKeyboardButton(text="3️⃣",callback_data='three')],
#         [types.InlineKeyboardButton(text="4️⃣",callback_data='four'), types.InlineKeyboardButton(text="5️⃣",callback_data='five'),types.InlineKeyboardButton(text="6️⃣",callback_data='six')],
#         [types.InlineKeyboardButton(text="7️⃣",callback_data='seven'), types.InlineKeyboardButton(text="8️⃣",callback_data='eight'),types.InlineKeyboardButton(text="9️⃣",callback_data='nine')],
#         [types.InlineKeyboardButton(text="➕",callback_data='plus'), types.InlineKeyboardButton(text="0️⃣",callback_data='zero'),types.InlineKeyboardButton(text="🔙",callback_data='back')],
#         [types.InlineKeyboardButton(text=lang_data[lang1][10],callback_data='true')],
#
#     ]
#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
#     await message.answer(
#         f"{lang_data[lang1][11]}",
#         reply_markup=keyboard)
#     print(2, user_data)
#     print(3, user_data)
#
#
#
#
# dict_num = {
#     "one":'1',
#     "two":'2',
#     "three":'3',
#     "four":'4',
#     "five":'5',
#     "six":"6",
#     "seven":"7",
#     "eight":'8',
#     "nine":'9',
#     "plus":'+',
#     "zero":'0',
# }
#
#
# list_numbers = ['one', 'two', 'three','four','five','six','seven','eight','nine','plus','zero','back','true',]
# @dp.callback_query(lambda c: c.data.startswith(('one', 'two', 'three','four','five','six','seven','eight','nine','plus','zero','back','true',)))
# async def checkcallback(callback: types.CallbackQuery):
#     user_id = callback.from_user.id
#     lang1 = user_data[user_id]["choose_lang"]
#     user_id = callback.from_user.id
#     text = callback.data
#     if text == 'back':
#         del phone[-1]
#         str1 = ""
#     elif text in dict_num:
#         phone.append(dict_num[text])
#         str1 = ""
#     elif text == 'true':
#         str1 = ""
#         for i in phone:
#             str1 += i
#         user_data[user_id]['phone_number'] = str1
#         # await num_check(callback.message)  # Bu yerda num_check funksiyasini chaqiraman.
#         print(f"Phone number saved: {str1}")
#         await num_check(callback.message)
#     for i in phone:
#         str1 += i
#     button = [
#         [types.InlineKeyboardButton(text="1️⃣", callback_data='one'),
#          types.InlineKeyboardButton(text="2️⃣", callback_data='two'),
#          types.InlineKeyboardButton(text="3️⃣", callback_data='three')],
#         [types.InlineKeyboardButton(text="4️⃣", callback_data='four'),
#          types.InlineKeyboardButton(text="5️⃣", callback_data='five'),
#          types.InlineKeyboardButton(text="6️⃣", callback_data='six')],
#         [types.InlineKeyboardButton(text="7️⃣", callback_data='seven'),
#          types.InlineKeyboardButton(text="8️⃣", callback_data='eight'),
#          types.InlineKeyboardButton(text="9️⃣", callback_data='nine')],
#         [types.InlineKeyboardButton(text="➕", callback_data='plus'),
#          types.InlineKeyboardButton(text="0️⃣", callback_data='zero'),
#          types.InlineKeyboardButton(text="🔙", callback_data='back')],
#         [types.InlineKeyboardButton(text=lang_data[lang1][10], callback_data='true')],
#
#     ]
#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
#     if text in dict_num:
#         try:
#             await callback.message.edit_text(
#                 f"{lang_data[lang1][11]}{str1}",
#                 reply_markup=keyboard
#             )
#         except aiogram.exceptions.TelegramBadRequest as e:
#             print(text)
#             if "message is not modified" in str(e):
#                 print("Xabar o'zgarmaganligi sababli yangilash o'tkazib yuborildi.")
#             else:
#                 print(f"Xato yuz berdi: {e}")
#     elif text == 'back':
#         await callback.message.edit_text(
#
#             f"Sizning telefon raqamingiz:{str1}",
#             reply_markup=keyboard
#         )
#     # elif text == "true":
#     #     user_data[user_id]['phone_number']= str1
#     #     # await num_check(callback.message)
#     #     print(user_data)
#     print(phone)
#
#
# async def num_check(message: types.Message):
#     print("bu funksiyaga keldi")
#     user_id = message.from_user.id
#     user_data[user_id]['holat'] = 'num'
#     number = user_data[user_id]['phone_number']
#     await message.answer(f"Your phone number: {number}")
#
#
#
# async def main():
#     print('The bot is running...')
#     await dp.start_polling(bot)
#
# asyncio.run(main())



