import aiogram
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message
import asyncio
from decimal import Decimal
from yandex_geocoder import Client

TOKEN = "8130717585:AAHS0sptIpqNLd66QzFOWIKV1uXZ9mkWbFc"
bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}

@dp.message()
async def handnle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start" or message.text == "🗂 | Asosiy menu":
        await start(message)
    elif message.text == "🛍 Buyurtma berish":
        await order(message)
    elif message.text == "⚙️ Sozlamalar":
        await settings(message)
    elif message.text == "ℹ️ Biz haqimizda":
        await aboutus(message)
    elif message.text == "📋 Mening buyurtmalarim":
        await myorders(message)
    elif message.text == "✍️Izoh qoldirish":
        await revies(message)
    elif message.text == "Olib ketish":
        await take_away(message)
    elif message.text == "Yetkazib berish":
        await delivery(message)
    elif message.text in list_city:
        await check_branch(message)
    elif message.text == "🍔BURGERLAR":
        await burgers(message)
    elif message.text in item_info:
        await check_burger(message)


    elif message.text == "⬅️ Orqaga":
        if user_data[user_id]["holat"] == "order" or user_data[user_id]["holat"] == "settings" or user_data[user_id]["holat"] == "aboutus" or user_data[user_id]["holat"] == "revies":
            await start(message)
        elif user_data[user_id]["holat"] == "take_away":
            await order(message)
        elif user_data[user_id]["holat"] == "burgers":
            await check_branch(message)
        elif user_data[user_id]["holat"] == "check_burger":
            await burgers(message)





@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    photos = await bot.get_user_profile_photos(user_id)

    # * RASMNI JONATISH  *
    # if photos.photos:
    #     photo = photos.photos[0][-1].file_id  # Eng oxirgi profil rasm ID'si
    #     await message.answer_photo(photo, caption="Bu sizning profil rasmingiz!")
    # else:
    #     await message.answer("Sizda profil rasmi yo‘q.")

    user_data[user_id] = {}
    user_data["first_name"] = f"first_name{first_name}\n"
    user_data["last_name"] = f"last_name{last_name}\n"
    user_data["username"] = f"username{username}\n"
    user_data["photos"] = f"photos{photos}\n"
    button = [
        [types.KeyboardButton(text="🛍 Buyurtma berish")],
        [types.KeyboardButton(text="⚙️ Sozlamalar"), types.KeyboardButton(text="ℹ️ Biz haqimizda")],
        [types.KeyboardButton(text="📋 Mening buyurtmalarim"), types.KeyboardButton(text="✍️Izoh qoldirish")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)
    await message.answer("Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing \n\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin", reply_markup=keyboard)
    print(user_data)
    print(photos)



async def order(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "order"
    button = [
        [types.KeyboardButton(text="Olib ketish"), types.KeyboardButton(text="Yetkazib berish")],
        [types.KeyboardButton(text="⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)
    await message.answer("Yetkazib berish turini tanlang", reply_markup=keyboard)
    print(user_data)



async def settings(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "settings"
    button = [
        [types.KeyboardButton(text="🇺🇿 Tilni o'zgartirish"), types.KeyboardButton(text="Tug'ilgan kunni qo'shish")],
        [types.KeyboardButton(text="Telefon raqamni o'zgartirish"), types.KeyboardButton(text="⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Sozlamani tanlang", reply_markup=keyboard)
    print(user_data)



async def aboutus(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "aboutus"
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("loook", reply_markup=keyboard)
    print(user_data)


async def myorders(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="🗂 | Asosiy menu")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Sizda buyurtmalar yo'q", reply_markup=keyboard)
    print(user_data)


async def revies(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "revies"
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Izoh qoldiring. Sizning fikringiz biz uchun muhim", reply_markup=keyboard)
    print(user_data)



async def take_away(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "take_away"
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"),types.KeyboardButton(text="📍 Eng yaqin filialni aniqlash")],
        [types.KeyboardButton(text="Yangli yo'l"),types.KeyboardButton(text="Yunusobod")],
        [types.KeyboardButton(text="Maxim Gorkiy"),types.KeyboardButton(text="Boulevard")],
        [types.KeyboardButton(text="Chilonzor"),types.KeyboardButton(text="Beruniy")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Filialni tanlang", reply_markup=keyboard)
    print(user_data)


async def delivery(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "delivery"
    button = [
        [types.KeyboardButton(text="Lokatsiya yuborish")],
        [types.KeyboardButton(text="⬅️ Orqaga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring", reply_markup=keyboard)
    print(user_data)


async def check_branch(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "check_branch"
    button = [
        [types.KeyboardButton(text="Interaktiv menu",web_app=types.WebAppInfo(url="https://loook.uz"))],
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Iftor set"), types.KeyboardButton(text="🍔BURGERLAR")],
        [types.KeyboardButton(text="🍗TOVUQ"), types.KeyboardButton(text="🍰SHIRINLIKLAR")],
        [types.KeyboardButton(text="🧸BOLALAR MENYUSI"), types.KeyboardButton(text="🍕PIZZA")],
        [types.KeyboardButton(text="🌯SPINNERLAR"), types.KeyboardButton(text="🥗SALATLAR")],
        [types.KeyboardButton(text="🥤🍟KOMBO"), types.KeyboardButton(text="🍅SAUSE")],
        [types.KeyboardButton(text="🍟APPETIZERS"), types.KeyboardButton(text="🍦🥛ICE CREAM & MILKSHAKE")],
        [types.KeyboardButton(text="🥤ICHIMLIKLAR"), types.KeyboardButton(text="GENERAL")],
        [types.KeyboardButton(text="TOG'ORA"), types.KeyboardButton(text="VAFLI")],
        [types.KeyboardButton(text="AVA Pizza")],
    ]
    but = [
        [types.InlineKeyboardButton(text="Interaktiv menu", url="https://loook.uz")] # url qoshish kerey
    ]
    key = types.InlineKeyboardMarkup(inline_keyboard=but, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Kategoriyani tanlang", reply_markup=keyboard)
    await message.answer("Interaktiv menyudan buyurtma bering", reply_markup=key)
    print(user_data)

list_city = ["Yangli yo'l", "Yunusobod","Maxim Gorkiy","Boulevard","Chilonzor","Beruniy"]




async def burgers(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "burgers"
    button = [
        [types.KeyboardButton(text="Interaktiv menu",web_app=types.WebAppInfo(url="https://loook.uz"))],
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Twins burger mol go'shti"), types.KeyboardButton(text="Twins burger tovuqli")],
        [types.KeyboardButton(text="Paket"), types.KeyboardButton(text="Beef longer")],
        [types.KeyboardButton(text="Chili Longer"), types.KeyboardButton(text="Bigger")],
        [types.KeyboardButton(text="Burger Cheese"), types.KeyboardButton(text="Chicky Burger")],
        [types.KeyboardButton(text="Hamburger"), types.KeyboardButton(text="Junior Burger")],
        [types.KeyboardButton(text="Longer")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🍔BURGERLAR\n🍔Burgerlar \nMahsulotni tanlang:", reply_markup=keyboard)



async def check_burger(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "check_burger"
    text = message.text
    if text in item_info:
        but = [
            [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        ]
        button = [
            [types.InlineKeyboardButton(text=f"➖", callback_data="minus"),
            types.InlineKeyboardButton(text=f"{item_info[text][2]}", callback_data=f"count_{item_info[text][2]}"),
            types.InlineKeyboardButton(text=f"➕", callback_data="plus"),],
            [types.InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data=f"basket")],

        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=but, resize_keyboard=True)
        key = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
        file_path = f"{item_info[text][3]}"
        caption_text = (
            f"{item_info[text][0]}\n"
            f"{item_info[text][-1]}\n\n"
            f"\n"
            f"{item_info[text][0]}: {item_info[text][1]} x {item_info[text][2]} = {item_info[text][1]}\n"
            f"Umumiy: {item_info[text][1]} UZS"
        )
        await message.answer("Mahsulot miqdorini tanlang:", reply_markup=keyboard)
        await message.answer_photo(
            caption=caption_text,
            photo=types.FSInputFile(path=file_path),
            parse_mode="Markdown",
            reply_markup=key)
    else:
        print("Mahsulot topilmadi")


item_info = {
    "Twins burger mol go'shti":["Twins burger mol go'shti",30000,1,"images/twins-goshtli.jpg",
    "Mol go‘shtli Twins-Burger – ikkita shirali mol go‘shtli burger bir setda! Tanlangan mol go‘shtidan tayyorlangan kotlet, yangi sabzavotlar va maxsus sous yumshoq bulochkada. Haqiqiy go‘shtsevarlar uchun! "],
    "Twins burger tovuqli":["Twins burger tovuqli",39000,1,"images/twins-tovuqli.jpg",
    "Tovuqli Twins-Burger – bitta emas, ikkita qarsildoq tovuqli burger! Tillarang panirlangan yumshoq tovuq go‘shti, yangi sabzavotlar va maxsus sous yumshoq bulochkada. Tovuqni sevuvchilar uchun ideal tanlov! "],
    "Paket": ["Paket", 2000, 1,"images/paket.jpg",
    "Paket пакет "],
    "Beef longer": ["Beef longer", 30000, 1,"images/beef_longer.jpg",
    "Beef longer Non (Longer), Mayonez, Salsa Sous, Piyoz, Sho'rbodring (Manirovanniy), Pomidor, Aysberg, Kotlet (Mol Go'sht)"],
}




async def main():
    print('The bot is running...')
    await dp.start_polling(bot)

asyncio.run(main())


























