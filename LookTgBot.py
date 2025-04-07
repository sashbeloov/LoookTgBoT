from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message
import asyncio

TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}


@dp.message()
async def handnle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start" or message.text == "🗂 | Asosiy menu":
        await start(message)
    elif message.text in functions:
        await functions[message.text](message)
    elif message.text in list_city:
        await check_branch(message)
    elif message.text in item_info:
        await check_item(message)
    elif message.text == "📥 Savat":
        await basket(message)
    elif "next_menu" in user_data[user_id]:
        if user_data[user_id]["choosed_menu"] == "🍔BURGERLAR":
            await burgers(message)

    # "⬅️ Orqaga" ni tekshirish
    elif message.text == "⬅️ Orqaga":
        if user_data[user_id]["holat"] == "order" or user_data[user_id]["holat"] == "settings" or user_data[user_id]["holat"] == "aboutus" or user_data[user_id]["holat"] == "revies":
            await start(message)
        elif user_data[user_id]["holat"] == "take_away":
            await order(message)
        elif user_data[user_id]["holat"] == "burgers":
            await check_branch(message)
        elif user_data[user_id]["holat"] == "check_item":
            await burgers(message)
        if user_data[user_id]["holat"] in holatlar:
            await check_branch(message)


@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    # first_name = message.from_user.first_name
    # last_name = message.from_user.last_name
    # username = message.from_user.username
    # photos = await bot.get_user_profile_photos(user_id)

    # * RASMNI JONATISH  *
    # if photos.photos:
    #     photo = photos.photos[0][-1].file_id  # Eng oxirgi profil rasm ID'si
    #     await message.answer_photo(photo, caption="Bu sizning profil rasmingiz!")
    # else:
    #     await message.answer("Sizda profil rasmi yo‘q.")

    user_data[user_id] = {}
    # user_data["first_name"] = f"first_name{first_name}\n"
    # user_data["last_name"] = f"last_name{last_name}\n"
    # user_data["username"] = f"username{username}\n"
    # user_data["photos"] = f"photos{photos}\n"
    button = [
        [types.KeyboardButton(text="🛍 Buyurtma berish")],
        [types.KeyboardButton(text="⚙️ Sozlamalar"), types.KeyboardButton(text="ℹ️ Biz haqimizda")],
        [types.KeyboardButton(text="📋 Mening buyurtmalarim"), types.KeyboardButton(text="✍️Izoh qoldirish")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)
    await message.answer("Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing \n\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin", reply_markup=keyboard)
    print(user_data)
    # print(photos)



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
    if "basket" not in user_data[user_id]:
        user_data[user_id]["basket"] = {}
    button = [
        [types.KeyboardButton(text="Interaktiv menu",web_app=types.WebAppInfo(url="https://loook.uz"))],
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Aksiya"), types.KeyboardButton(text="🍔BURGERLAR")],
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


async def aksiya(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "aksiya"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Duet master 2=3"), types.KeyboardButton(text="Bigger 2=3")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("aksiya \nMahsulotni tanlang:", reply_markup=keyboard)



async def burgers(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "burgers"
    user_data[user_id]["choosed_menu"] = message.text
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


async def tovuq(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "tovuq"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Dinner Meal (2normal, 1spicy)"), types.KeyboardButton(text="Chicken Normal")],
        [types.KeyboardButton(text="Chicken Spicy"), types.KeyboardButton(text="Dinner Meal Normal")],
        [types.KeyboardButton(text="Dinner Meal Spicy"), types.KeyboardButton(text="Mix meal")],
        [types.KeyboardButton(text="Snack Meal Normal"), types.KeyboardButton(text="Snack Meal Spicy")],
        [types.KeyboardButton(text="12 chicken set spicy"), types.KeyboardButton(text="12 chicken set mix")],
        [types.KeyboardButton(text="12 chicken set normal"), types.KeyboardButton(text="Dinner Meal (2spicy, normal)")],
        [types.KeyboardButton(text="Snack Meal(1normal, 1spicy)"), types.KeyboardButton(text="Mix meal (21spicy)")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🧸BOLALAR MENYUSI\b🧸Bolalar menyusi \nMahsulotni tanlang:", reply_markup=keyboard)


async def candies(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "candies"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Medovik"), types.KeyboardButton(text="Chocotastic")],
        [types.KeyboardButton(text="Chocolate Souffle"), types.KeyboardButton(text="Donuts Choco")],
        [types.KeyboardButton(text="Donuts Strawberry"), types.KeyboardButton(text="Red Wave")],
        [types.KeyboardButton(text="Sugar Chips"), types.KeyboardButton(text="Tello")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🍰SHIRINLIKLAR\n🍰Shiriliklar \nMahsulotni tanlang::", reply_markup=keyboard)




async def kids(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "kids"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Kids Menu Burger Boy"), types.KeyboardButton(text="Kids Menu Burger Girl")],
        [types.KeyboardButton(text="Kids Menu Spinner Boy"), types.KeyboardButton(text="Kids Menu Spinner Girl")],
        [types.KeyboardButton(text="Kids Burger"), types.KeyboardButton(text="Kids Juice")],
        [types.KeyboardButton(text="Mini spinner")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🧸BOLALAR MENYUSI\b🧸Bolalar menyusi \nMahsulotni tanlang:", reply_markup=keyboard)




async def pizza(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "pizza"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Pizza Supreme"), types.KeyboardButton(text="Pizza Hawaiian")],
        [types.KeyboardButton(text="Pizza Margarita (30sm)"), types.KeyboardButton(text="Pizza Pepperoni")],
        [types.KeyboardButton(text="Pizza Spicy"), types.KeyboardButton(text="Pizza Steak")],
        [types.KeyboardButton(text="Pizza Mix"), types.KeyboardButton(text="Pizza BBQ Chicken")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🍕PIZZA\n🍕PIZZA \nMahsulotni tanlang::", reply_markup=keyboard)



async def spinner(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "spinner"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Twix Crispy Roll"), types.KeyboardButton(text="Twix Chicken Crispy Roll")],
        [types.KeyboardButton(text="Spinner no sauce"), types.KeyboardButton(text="Duet Master")],
        [types.KeyboardButton(text="Smile Box"), types.KeyboardButton(text="Spinner Salsa")],
        [types.KeyboardButton(text="Spinner Snack"), types.KeyboardButton(text="Spinner Super Charged")],
        [types.KeyboardButton(text="Spinner Tako")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🌯SPINNERLAR\n🌯SPINNERLAR \nMahsulotni tanlang::", reply_markup=keyboard)



async def salat(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "salat"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="O'yinchoq"), types.KeyboardButton(text="Bread Pikelet")],
        [types.KeyboardButton(text="Coleslaw"), types.KeyboardButton(text="Loook Salad")],
        [types.KeyboardButton(text="Cheese 1 slice")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🥗SALATLAR\n🥗SALATLAR \nMahsulotni tanlang::", reply_markup=keyboard)



async def kombo(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "kombo"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Habits"), types.KeyboardButton(text="Fully combo")],
        [types.KeyboardButton(text="Smile set")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🥤🍟KOMBO\n🥤🍟KOMBO \nMahsulotni tanlang::", reply_markup=keyboard)



async def souse(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "souse"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Halapeno"), types.KeyboardButton(text="Cheese Sauce")],
        [types.KeyboardButton(text="Toco Sous"),types.KeyboardButton(text="Ketchup")],
        [types.KeyboardButton(text="Mayo 1 pot"),types.KeyboardButton(text="Mix max")],
        [types.KeyboardButton(text="Salsa")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🍅SAUSE\n🍅SAUSE \nMahsulotni tanlang::", reply_markup=keyboard)



async def appitizer(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "appitizer"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Piyozli halqalari"), types.KeyboardButton(text="Big hot shots")],
        [types.KeyboardButton(text="Rustic fries"),types.KeyboardButton(text="Chechevit soup")],
        [types.KeyboardButton(text="Cheese Fries"),types.KeyboardButton(text="Cheese Nuggets")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🍟APPETIZERS\n🍟APPETIZERS \nMahsulotni tanlang::", reply_markup=keyboard)


async def ice_cream(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "ice_cream"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Milkshake (Strawberry)"), types.KeyboardButton(text="Chilly Ice (500g)")],
        [types.KeyboardButton(text="Chocolate Ice Cream"),types.KeyboardButton(text="LoookFlurry Bingo")],
        [types.KeyboardButton(text="LoookFlurry Wafer"),types.KeyboardButton(text="Strawberry Ice Cream")],
        [types.KeyboardButton(text="Milkshake Banana"),types.KeyboardButton(text="Milkshake Choco")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🍦🥛ICE CREAM & MILKSHAKE\n🍦🥛ICE CREAM & MILKSHAKE \nMahsulotni tanlang::", reply_markup=keyboard)


async def drinks(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "drinks"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Dinay"), types.KeyboardButton(text="Sprite разлив")],
        [types.KeyboardButton(text="Fante разлив"),types.KeyboardButton(text="Coca-Cola разлив")],
        [types.KeyboardButton(text="Mineralka bezgaz"),types.KeyboardButton(text="Sok 1L (Ananas)")],
        [types.KeyboardButton(text="Sok 1L (apelsin)"),types.KeyboardButton(text="Coca-Cola")],
        [types.KeyboardButton(text="Fanta"),types.KeyboardButton(text="Ice-Tea")],
        [types.KeyboardButton(text="Mineralka bezgaz"),types.KeyboardButton(text="Sprite")],
        [types.KeyboardButton(text="Sok 1L "),types.KeyboardButton(text="Issiq-Ichimliklar")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("🥤ICHIMLIKLAR\n🥤ICHIMLIKLAR \nMahsulotni tanlang::", reply_markup=keyboard)


async def general(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "general"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="WINGS 5 PCS - STRIPS 8 PCS (MIX) (0.5kg +-)"), types.KeyboardButton(text="WINGS 10 PCS - STRIPS 16 PCS (MIX) (1kg +-)")],
        [types.KeyboardButton(text="16 PCS STRIPS (0.5kg +-)"),types.KeyboardButton(text="32 PCS STRIPS (1kg +-)")],
        [types.KeyboardButton(text="11 PCS WINGS (0.5kg +-)"),types.KeyboardButton(text="21 PCS WINGS (1kg +-)")],
        [types.KeyboardButton(text="16 NORMAL/16 SPICY + 32 WING"),types.KeyboardButton(text="24 SPICY + 24 STRIPS")],
        [types.KeyboardButton(text="24 SPICY + 24 STRIPS"),types.KeyboardButton(text="12 NORMAL/12 SPICY + 24 WING")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("GENERAL\nGENERAL \nMahsulotni tanlang::", reply_markup=keyboard)


async def togora(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "togora"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="24 NORMAL + 24 STRIPS"), types.KeyboardButton(text="32 PIECE NORMAL + 32 WING")],
        [types.KeyboardButton(text="32 PIECE NORMAL + 32 STRIPS"),types.KeyboardButton(text="24 SPICY + 24 WING")],
        [types.KeyboardButton(text="24 NORMAL + 24 WINGS")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("TOG'ORA\nTOG'ORA \nMahsulotni tanlang::", reply_markup=keyboard)

async def vafli(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "vafli"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Gonkong konsuli"), types.KeyboardButton(text="Gonkong muzqaymoq vaflisi")],
        [types.KeyboardButton(text="Belgiya bananli vaflisi"), types.KeyboardButton(text="Belgiya mini vaflisi")],
        [types.KeyboardButton(text="Lorenti Fondyu"), types.KeyboardButton(text="Belgiya shokoladli vaflisi")],
        [types.KeyboardButton(text="Vena vaflisi"), types.KeyboardButton(text="Vena shokoladli vaflisi")],
        [types.KeyboardButton(text="Belgiya qulupnayli vaflisi")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("VAFLI\nVAFLI \nMahsulotni tanlang::", reply_markup=keyboard)



async def ava_pizza(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "ava_pizza"
    user_data[user_id]["choosed_menu"] = message.text
    button = [
        [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("AVA Pizza\nMahsulotni tanlang::", reply_markup=keyboard)


async def check_item(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "check_item"
    text = message.text
    if text in item_info:
        but = [
            [types.KeyboardButton(text="⬅️ Orqaga"), types.KeyboardButton(text="📥 Savat")],
        ]
        button = [
            [types.InlineKeyboardButton(text=f"➖", callback_data=f"minus_{text}"),
            types.InlineKeyboardButton(text=f"{item_info[text][2]}", callback_data=f"count_{text}"),
            types.InlineKeyboardButton(text=f"➕", callback_data=f"plus_{text}"),],
            [types.InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data=f"basket_{text}")],
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
        user_data[user_id]["counter"] = [item_info[text][2], item_info[text][1]]
    else:
        print("Mahsulot topilmadi")



@dp.callback_query()
async def update_item(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_data[user_id]["holat"] = "update_item"
    info_button, name = callback.data.split("_")
    count = user_data[user_id]["counter"][0]
    price = user_data[user_id]["counter"][1]

    if info_button == "plus":
        count += 1
    elif info_button == "minus":
        if count > 1:
            count -= 1
    elif info_button == "basket":
        if name in user_data[user_id]["basket"]:
            user_data[user_id]["basket"][name] += count
            user_data[user_id]["next_menu"] = "next_menu"
        else:
            user_data[user_id]["basket"][name] = count
            user_data[user_id]["next_menu"] = "next_menu"

    # ✅ Yangilangan qiymatni saqlash
    user_data[user_id]["counter"] = [count, price]

    button = [
        [types.InlineKeyboardButton(text="➖", callback_data=f"minus_{name}"),
         types.InlineKeyboardButton(text=f"{count}", callback_data=f"count_{name}"),
         types.InlineKeyboardButton(text="➕", callback_data=f"plus_{name}")],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data=f"basket_{name}")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)

    caption_text = (
        f"{item_info[name][0]}\n"
        f"{item_info[name][-1]}\n\n"
        f"{item_info[name][0]}: {price} x {count} = {price * count}\n"
        f"Umumiy: {price * count} UZS")
    caption_text += f"\n\u200b"
    print(user_data[user_id]["basket"])
    try:
        await callback.message.edit_caption(
            caption=caption_text,
            reply_markup=keyboard,)
    except Exception as e:
        print(f"Xato: {e}")


async def basket(message: types.Message):
    user_id = message.from_user.id
    result = user_data[user_id]["basket"] # {'Twins burger tovuqli': 1, 'Paket': 1}
    print(result)
    choosed_items = ""
    all_total = 0
    if result:
        but = [
            [types.InlineKeyboardButton(text="Buyurtmani tasdiqlash", callback_data="confirm")],
            [types.InlineKeyboardButton(text="Buyurtmani davom ettirish", callback_data="continue")],
            [types.InlineKeyboardButton(text="🔄 Tozalash", callback_data="clear")]
        ]

        for item_name, count in result.items():
            summa = item_info[item_name][1]
            summa *= count
            all_total += summa
            choosed_items += f"{item_name} x {count} = {summa} \n"

            row = [
                types.InlineKeyboardButton(text="➖", callback_data=f"minus_{item_name}"),
                types.InlineKeyboardButton(text=f"{item_name}", callback_data="none"),
                types.InlineKeyboardButton(text="➕", callback_data=f"plus_{item_name}")
            ]
            but.append(row)

        inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=but)

        reply_buttons = [
            [types.KeyboardButton(text="⬅️ Orqaga")]
        ]
        reply_keyboard = types.ReplyKeyboardMarkup(keyboard=reply_buttons, resize_keyboard=True)

        await message.answer("Savat:", reply_markup=reply_keyboard)
        await message.answer(f"{choosed_items}\n\nUmumiy: {all_total}", reply_markup=inline_keyboard)


    else:
        button = [
            [types.KeyboardButton(text="⬅️ Orqaga")]
        ]
        but = [
            [types.InlineKeyboardButton(text="🔄 Tozalash", callback_data=f"clear"),]
        ]
        key = types.InlineKeyboardMarkup(inline_keyboard=but,)
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer("Savat:", reply_markup=keyboard)
        await message.answer("Hozircha savatingiz bo'sh", reply_markup=keyboard)
        await message.answer("Buyurtmani davom ettirish", reply_markup=key)
        print(user_data)



list_city = ["Yangli yo'l", "Yunusobod","Maxim Gorkiy","Boulevard","Chilonzor","Beruniy"]

holatlar = {"update_item", "aksiya", "tovuq", "candies", "kids", "pizza", "spinner", "salat", "kombo", "souse", "appitizer", "ice_cream", "drinks", "general", "togora", "vafli", "ava_pizza"}

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

functions = {
    "🛍 Buyurtma berish": order,
    "⚙️ Sozlamalar": settings,
    "ℹ️ Biz haqimizda": aboutus,
    "📋 Mening buyurtmalarim": myorders,
    "✍️Izoh qoldirish": revies,
    "Olib ketish": take_away,
    "Yetkazib berish": delivery,
    "🍔BURGERLAR": burgers,
    "🍗TOVUQ": tovuq,
    "🍰SHIRINLIKLAR": candies,
    "🧸BOLALAR MENYUSI": kids,
    "🍕PIZZA": pizza,
    "🌯SPINNERLAR": spinner,
    "🥗SALATLAR": salat,
    "🥤🍟KOMBO": kombo,
    "🍅SAUSE": souse,
    "🍟APPETIZERS": appitizer,
    "🍦🥛ICE CREAM & MILKSHAKE": ice_cream,
    "🥤ICHIMLIKLAR": drinks,
    "GENERAL": general,
    "TOG'ORA": togora,
    "VAFLI": vafli,
    "AVA Pizza": ava_pizza
}



async def main():
    print('The bot is running...')
    await dp.start_polling(bot)

asyncio.run(main())
