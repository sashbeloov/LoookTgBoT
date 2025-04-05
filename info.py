# from aiogram import types
# from aiogram.dispatcher import Dispatcher
#
#
# # Masalan, dastlabki holat:
# @dp.message_handler(commands=['start'])
# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(types.KeyboardButton(text="Interaktiv menyu"))
#
#     await message.answer(
#         "Salom! Bu yerda sizga asosiy tugmani ko‘rsatamiz. \n"
#         "“Interaktiv menyu” tugmasini bosing:",
#         reply_markup=keyboard
#     )
#
#
# # “Interaktiv menyu” tugmasi bosilganda:
# @dp.message_handler(lambda msg: msg.text == "Interaktiv menyu")
# async def interactive_menu(message: types.Message):
#     # Yangi tugmalarni yaratamiz
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.row("⬅️ Orqaga", "📥 Savat")
#     keyboard.row("Акция", "BURGERLAR")
#     keyboard.row("TOVUQ", "SHIRINLIKLAR")
#
#     await message.answer(
#         "Kategoriyani tanlang:",
#         reply_markup=keyboard
#     )


# import requests
#
# YANDEX_API_KEY = "29c55c81-c803-4265-b908-805befaa28a2"
#
# def get_address_from_coordinates(lat, lon):
#     url = f"https://geocode-maps.yandex.ru/1.x/?apikey={YANDEX_API_KEY}&geocode={lon},{lat}&format=json"
#     response = requests.get(url)
#     data = response.json()
#
#     if "response" in data:
#         address = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
#         return address
#     else:
#         return "Manzil topilmadi"
#
# latitude = 41.2995
# longitude = 69.2401
#
# address = get_address_from_coordinates(latitude, longitude)
# print(address)



# async def address(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id]['get_location'] = 'location'
#     if message.location is not None:
#         latitude = message.location.latitude
#         longitude = message.location.longitude
#
#         client = Client('29c55c81-c803-4265-b908-805befaa28a2')
#         location = client.address(Decimal(str(longitude)), Decimal(str(latitude)))
#         user_data[user_id]['location'] = location
#         buttons = [
#             [types.KeyboardButton(text='Qayta yuborish'), types.KeyboardButton(text='Tasqidlash')],
#             [types.KeyboardButton(text='Saqlab qoyish'), types.KeyboardButton(text='Orqaga')],
#         ]
#         keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
#         await message.answer(f"Address: {location}", reply_markup=keyboard)
#         print(location)
#     else:
#         pass


# from geopy.geocoders import Nominatim
# async def check_location(message: types.Message):
#     global address
#     user_id = message.from_user.id
#     geolocator=Nominatim(user_agent="geo_bot")
#     if message.location is not None:
#         latitude = message.location.latitude
#         longitude = message.location.longitude
#
#         address_info= geolocator.reverse((latitude,longitude),exactly_one=True)
#         if address_info:
#             address=address_info.address
#         else:
#             address="Manzil topilmadi"
#         location = {
#             "latitude": latitude,
#             "longitude": longitude,
#             "address":address,
#         }
#     else:
#         location = message.text
#         user_data[user_id]["location"] = location
#     buttons = [
#         [types.KeyboardButton(text="⬅️Ortga"), types.KeyboardButton(text="✅Tasdiqlash")]
#     ]
#     keyboards = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
#     await message.answer(f"Sizning manzilingiz\n\n{address}📍joylashuvni tasdiqlang yoki qayta yuboring",reply_markup=keyboards)
#     print(location)
# import random
# print(f"\n<!-- {random.randint(1, 9999)}")

# git config --global user.name "sashbeloov"
# git config --global user.email "beloovsasha23@gmail.com.com"
# git init
# gitadd.
# git commit -m "initial commit"
# git push -u origin main
