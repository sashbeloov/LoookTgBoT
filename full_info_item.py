list_city = ["Yangli yo'l", "Yunusobod","Maxim Gorkiy","Boulevard","Chilonzor","Beruniy"]

holatlar = {"update_item", "aksiya", "tovuq", "candies", "kids", "pizza", "spinner", "salat", "kombo", "souse", "appitizer", "ice_cream", "drinks", "general", "togora", "vafli", "ava_pizza"}





item_info = {
    "Duet master 2=3":["Duet master 2=3", 35000, 1,"images/bigger_2=3.jpg","Duet master 2=3"],
    "Bigger 2=3":["Bigger 2=3", 32000, 1,"images/bigger_2=3.jpg","Bigger 2=3"],
    "Twins burger mol go'shti":["Twins burger mol go'shti",30000,1,"images/twins-goshtli.jpg",
    "Mol go‘shtli Twins-Burger – ikkita shirali mol go‘shtli burger bir setda! Tanlangan mol go‘shtidan tayyorlangan kotlet, yangi sabzavotlar va maxsus sous yumshoq bulochkada. Haqiqiy go‘shtsevarlar uchun! "],
    "Twins burger tovuqli":["Twins burger tovuqli",39000,1,"images/twins-tovuqli.jpg",
    "Tovuqli Twins-Burger – bitta emas, ikkita qarsildoq tovuqli burger! Tillarang panirlangan yumshoq tovuq go‘shti, yangi sabzavotlar va maxsus sous yumshoq bulochkada. Tovuqni sevuvchilar uchun ideal tanlov! "],
    "Paket": ["Paket", 2000, 1,"images/paket.jpg",
    "Paket пакет "],
    "Beef longer": ["Beef longer", 30000, 1,"images/beef_longer.jpg",
    "Beef longer Non (Longer), Mayonez, Salsa Sous, Piyoz, Sho'rbodring (Manirovanniy), Pomidor, Aysberg, Kotlet (Mol Go'sht)"],
    "Chili Longer": ["Chili Longer", 30000, 1, "images/chili_longer.jpg", " Non (Longer), Mayonez, Salsa Sous(Achchiq), Piyoz, Sho'rbodring (Manirovanniy), Pomidor, Aysberg, Kotlet (Mol Go'sht)"],
    "Bigger": ["Bigger", 31000, 1, "images/bigger.jpg", "Non (Longer), Mayonez, Ketchup, Piyoz, Sho'rbodring (Manirovinniy), Aysberg, Pomidor, Tovuq File, Pishloq"],
    "Burger Cheese": ["Burger Cheese", 32000, 1, "images/burger_cheese.jpg", "Non, Mayonez, Ketchup, Piyoz, Sho'rbodring (Manirovanniy), Pomidor, Aysberg, Kotlet (Mol Go'sht), Pishloq"],
    "Chicky Burger": ["Chicky Burger", 23000, 1, "images/Chicky_Burger.jpg", "Non, Mayonez, Aysberg, Pishloq, Kotlet (Tovuq)"],
    "Hamburger": ["Hamburger", 30000, 1, "images/Hamburger.jpg", "Non, Mayonez, Ketchup, Piyoz, Sho'rbodring (Manirovanniy), Pomidor, Aysberg, Kotlet (Mol Go'sht)"],
    "Junior Burger": ["Junior Burger", 21000, 1, "images/Junior_Burger.jpg", "Non, Mayonez, Ketchup, Piyoz, Sho'rbodring (Manirovinniy), Tovuq File"],
    "Longer": ["Longer", 27000, 1, "images/Longer.jpg", "Non (Longer), Mayonez, Ketchup, Piyoz, Sho'rbodring (Manirovinniy), Aysberg, Pomidor, Tovuq File"],

    "Dinner Meal (2normal, 1spicy)": ["Dinner Meal (2normal, 1spicy)", 49000, 1, "images/dinnert_meal.jpg",
                                      "tovuq, achchiq tovuq,  non, salad (coleslaw), maxsus kartoshka, cola ichimligi, maxsus sous"],
    "Chicken Normal": ["Chicken Normal", 12000, 1, "images/chicken_normal.jpg", "Tovuq, Maxsus Un"],
    "Chicken Spicy": ["Chicken Spicy", 12000, 1, "images/Chicken_Spicy.jpg", "Achchiq Tovuq, Maxsus Un"],
    "Dinner Meal Normal": ["Dinner Meal Normal", 49000, 1, "images/Dinner_Meal_Normal.jpg", "Tovuq,  Non, Salad (Coleslaw), Maxsus Kartoshka, Cola Ichimligi, Maxsus Sous"],
    "Dinner Meal Spicy": ["Dinner Meal Spicy", 49000, 1, "images/Dinner_Meal_Spicy.jpg", "Achchiq Tovuq,  Non, Salad (Coleslaw), Maxsus Kartoshka, Cola Ichimligi, Maxsus Sous"],
    "Mix meal": ["Mix meal", 34000, 1, "images/mix_meal.jpg", "Tovuq, Achchiq Qanot, Tovuq File,  Pishloqli Nuggetlar,, Salad (Coleslaw), Cola Ichimligi, Maxsus Sous"],
    "Snack Meal Normal": ["Snack Meal Normal", 39000, 1, "images/Snack_Meal_Normal.jpg", "Tovuq, Non,  Salad (Coleslaw), Maxsus Kartoshka, Cola Ichimligi, Maxsus Sous"],
    "Snack Meal Spicy": ["Snack Meal Spicy", 39000, 1, "images/Snack_Meal_Spicy.jpg", "Achchiq Tovuq,  Non, Salad (Coleslaw), Maxsus Kartoshka, Cola Ichimligi, Maxsus Sous"],
    "12 chicken set spicy": ["12 chicken set spicy", 175000, 1, "images/12_chicken_set_spicy.jpg", "12 Ta Tovuq Bo'lakchakari, 4 Ta Salat, 4 Ta Non Va 1,5 L Coca Cola"],
    "12 chicken set mix": ["12 chicken set mix", 175000, 1, "images/12chickensetmix.jpg", "2 Ta Tovuq Bo'lakchalari (6 Normal, 6 Spicy), 4 Ta Salat Salatasi, 4 Ta Non Va 1,5 Coca Cola"],
    "12 chicken set normal": ["12 chicken set normal", 175000, 1, "images/12chickensetnormal.jpg", "12 Ta Tovuq Bo'lakchalari (Normal), 4 Ta Salat Bargi, 4 Ta Non Va 1,5 Coca Cola"],
    "Dinner Meal (2spicy, normal)": ["Dinner Meal (2spicy, normal)", 49000, 1, "images/DinnerMeal(2spicy, 1 normal).jpg",
                                     "2spicy, 1 norma"],
    "Snack Meal(1normal, 1spicy)": ["Snack Meal(1normal, 1spicy)", 39000, 1, "images/Snack Meal(1normal, 1spicy).jpg",
                                    "2ta tovuq (1normal, 1spicy), non, salat, cola"],
    "Mix meal (21spicy)": ["Mix meal (21spicy)", 69000, 1, "images/Mixmeal(spicy).jpg", "Achchiq Tovuq, Achchiq Qanot, Tovuq File,  Pishloqli Nuggetlar,  Salad (Coleslaw), Cola Ichimligi, Maxsus Sous"],

    #shirinliklar
    "Medovik": ["Medovik", 14000, 1, "images/medovik.jpg", "Medovik"],
    "Chocotastic": ["Chocotastic", 15000, 1, "images/Chocotastic.jpg", "Tuxum, Un, Shakar, Kakao, Qaymoq, Shakar Kukuni, Kremchiz"],
    "Chocolate Souffle": ["Chocolate Souffle", 11000, 1, "images/Souffle.jpg", "Un, Sut, Tuxum, Kakao, Shokoladnaya Pasta, Shakar, Shokolad,  Yong'oq (Grecheskiy)"],
    "Donuts Choco": ["Donuts Choco", 12000, 1, "images/DonutsChoco.jpg", "Shokolad kulcha"],
    "Donuts Strawberry": ["Donuts Strawberry", 12000, 1, "images/DonutsStrawberry.jpg", "Qulupnayli Ponchik"],
    "Red Wave": ["Red Wave", 15000, 1, "images/RedWave.jpg", "Tuxum, Un, Shakar, Kakao, Qaymoq, Shakar Kukuni, Kremchiz, Malina Jem"],
    "Sugar Chips": ["Sugar Chips", 3000, 1, "images/sugar_chips.jpg", "Sugar Chips"],
    "Tello": ["Tello", 7000, 1, "images/Tello.jpg", "Yogurt, Tvorojniy Pasta, Qaymoq, Sgushoniy Moloko, Kakos Strujka, Sut, Tuxum, Shakar, Un, Rafaello, Bodom"],

    "Kids Menu Burger Boy": ["Kids Menu Burger Boy", 35000, 1, "images/KidsMenuBurgerBoy.jpg", "Kichkina Burger, Kartoshka Fri (Kichkina), O`yinchoq,  Kichkina Sok"],
    "Kids Menu Burger Girl": ["Kids Menu Burger Girl", 35000, 1, "images/KidsMenuBurgerGirl.jpg", "Kichkina Burger, Kartoshka Fri (Kichkina), O`yinchoq,  Kichkina Sok"],
    "Kids Menu Spinner Boy": ["Kids Menu Spinner Boy", 35000, 1, "images/KidsMenuSpinnerBoy.jpg", "Kichkina Spinner, Kartoshka Fri (Kichkina), O`yinchoq,  Kichkina Sok"],
    "Kids Menu Spinner Girl": ["Kids Menu Spinner Girl", 35000, 1, "images/KidsMenuSpinnerGirl.jpg", "Kichkina Spinner, Kartoshka Fri (Kichkina), O`yinchoq,  Kichkina Sok"],
    "Kids Burger": ["Kids Burger", 15000, 1, "images/KidsBurger.jpg", "Non, Mayonez, Ketchup, Sho'rbodring (Manirovanniy), Pomidor, Aysberg, Kotlet (Mol Go'sht)"],
    "Kids Juice": ["Kids Juice", 6000, 1, "images/KidsJuice.jpg", "Kids Sharbat"],
    "Mini spinner": ["Mini spinner", 14000, 1, "images/Minispinner.jpg", "Lavash Xamiri, Aysberg, Pomidor, Tovuq File, Supercharged Sous"],

    "Pizza Supreme": ["Pizza Supreme", 73000, 1, "images/Supreme.jpg", "Xamir, Sous, Pishloq, Qiyma (Mol), Kolbasa, Qo'ziqorin, Bulg'or Qalampiri, Zaytun"],
    "Pizza Hawaiian": ["Pizza Hawaiian", 50000, 1, "images/Hawaiian.jpg", "Xamir, Sous, Pishloq, Tovuq Filesi, Ananas, Kukuruz, Zaytun"],
    "Pizza Margarita (30sm)": ["Pizza Margarita (30sm)", 53000, 1, "images/Margarita (30 sm)(8 dona).jpg", "Xamir, Pizza Sousi, Pishloq, Pomidor"],
    "Pizza Pepperoni": ["Pizza Pepperoni", 57000, 1, "images/Pepperoni.jpg", "Xamir, Sous, Pishloq, Kolbasa, Qo'ziqorin, Zaytun"],
    "Pizza Spicy": ["Pizza Spicy", 60000, 1, "images/PizzaSpicy.jpg", "Xamir, Sous, Pishloq, Achchiq Sous, Qiyma (Mol Go'shti)"],
    "Pizza Steak": ["Pizza Steak", 76000, 1, "images/Steak.jpg", "Xamir, Sous, Pishloq, Go'sht (Mol),  Bulg'or Qalampiri, Zaytun, Pomidor"],
    "Pizza Mix": ["Pizza Mix", 72000, 1, "images/PizzaMix.jpg", " xamir, sous, pishloq, qiyma (mol), kolbasa, qo'ziqorin, zaytun, go'sht (mol) bulg'or qalampiri, pomidor, tovuq filesi "],
    "Pizza BBQ Chicken": ["Pizza BBQ Chicken", 48000, 1, "images/BBQ.jpg", "Xamir, Sous, Pishloq, Tovuq File, Bulg'or Qalampiri, Zaytun"],

    # Spinnerlar
    "Twix Crispy Roll": ["Twix Crispy Roll", 34000, 1, "images/Roll.jpg", "Lavash Xamiri, Pomidor, Go'sht (Mol), Maxsus Sous"],
    "Twix Chicken Crispy Roll": ["Twix Chicken Crispy Roll", 29000, 1, "images/.jpg", "Lavash Xamiri, Pomidor, Tovuq File, Maxsus Sous "],
    "Spinner no sauce": ["Spinner no sauce", 29000, 1, "images/CrispyRoll.jpg", "Lavash Xamiri, Pomidor, Tovuq File, Maxsus Sous "],
    "Duet Master": ["Duet Master", 34000, 1, "images/DuetMaster.jpg", "Lavash Xamiri, Aysberg, Pomidor, Kurka, Tovuq File, Maxsus Sous"],
    "Smile Box": ["Smile Box", 34000, 1, "images/DuetMaster.jpg", "Lavash Xamiri, Aysberg, Pomidor, Kurka, Tovuq File, Maxsus Sous"],
    "Spinner Salsa": ["Spinner Salsa", 32000, 1, "images/SpinnerSalsa.jpg", "Lavash Xamiri, Aysberg, Pomidor, Tovuq File, Salsa Sous (Achchiq)"],
    "Spinner Snack": ["Spinner Snack", 25000, 1, "images/SpinnerSnack.jpg", "Lavash Xamiri, Aysberg, Pomidor, Tovuq File, Snack Sous (Murch)"],
    "Spinner Super Charged": ["Spinner Super Charged", 38000, 1, "images/SpinnerSuperCharged.jpg", "Lavash Xamiri, Aysberg, Pomidor, Tovuq File, Supercharged Sous (Shirin)"],
    "Spinner Tako": ["Spinner Tako", 36000, 1, "images/SpinnerTako.jpg", "Lavash Xamiri, Aysberg, Pomidor, Tovuq File, Tako Sous (Chesnok)"],

    # Salatlar
    "O'yinchoq": ["O'yinchoq", 10000, 1, "images/O'yinchoq.jpg", "O'yinchoq"],
    "Bread Pikelet": ["Bread Pikelet", 3000, 1, "images/BreadPikelet.jpg", "Non Pikelet"],
    "Coleslaw": ["Coleslaw", 7000, 1, "images/ColeslawSalad.jpg", "Karam Salat"],
    "Loook Salad": ["Loook Salad", 16000, 1, "images/LoookSalad.jpg", "Pomidor, Jo'xori, Mаyonez, Aysberg"],
    "Cheese 1 slice": ["Cheese 1 slice", 3000, 1, "images/Cheese1slice.jpg", "Cheese 1 slice"],

    # Kombo
    "Habits": ["Habits", 51000, 1, "images/Habits.jpg", "Bigger, Coca Cola, kartoshka fri, hot shots, souslar"],
    "Fully combo": ["Fully combo", 55000, 1, "images/Fullycombo.jpg", "Cheesburger, Coca Cola, kartoshka fri, chicken (oyoq, yoki qanot, yoki biqin), maxus souslar"],
    "Smile set": ["Smile set", 53000, 1, "images/Fullycombo.jpg", "Cheesburger, Coca Cola, kartoshka fri, chicken (oyoq, yoki qanot, yoki biqin), maxus souslar"],

    # Souslar
    "Halapeno": ["Halapeno", 2000, 1, "images/Halapeno.jpg", "Halapeno"],
    "Cheese Sauce": ["Cheese Sauce", 2000, 1, "images/CheeseSauce.jpg", "Cheese Sauce"],
    "Toco Sous": ["Toco Sous", 2000, 1, "images/Taco.jpg", "Taco Sauce"],
    "Ketchup": ["Ketchup", 2000, 1, "images/Ketchup.jpg", "Ketchup"],
    "Mayo 1 pot": ["Mayo 1 pot", 2000, 1, "images/Mayo.jpg", "mayonez"],
    "Mix max": ["Mix max", 2000, 1, "images/mixmax.jpg", "Mix Max Sous"],
    "Salsa": ["Salsa", 2000, 1, "images/Salsa_souse.jpg", "Salsa sous  "],

    # Appetizers
    "Piyozli halqalari": ["Mahsulot vaqtincha sotuvda emas", 30000, 1, "images/Bighotshots.jpg", "Achchiq Tovuq File bo'lakchalari, Maxsus Un"],
    "Big hot shots": ["Big hot shots", "Big hot shots", 30000, 1, "images/Bighotshots.jpg", "Achchiq Tovuq File bo'lakchalari, Maxsus Un"],
    "Rustic fries": ["Rustic fries", 22000, 1, "images/Rusticfries.jpg", "Maxsus Kartoshka, Ketchup"],
    "Chechevit soup": ["Chechevit soup", 16000, 1, "images/Chechevitsoup.jpg", "Yasmiq sho‘rva"],
    "Cheese Fries": ["Cheese Fries", 22000, 1, "images/CheeseFries.jpg", "Kartoshka Fri, Pishloq Sous, Xalapeno"],
    "Cheese Nuggets": ["Cheese Nuggets", 12000, 1, "images/CheeseNuggets.jpg", "tovuq filesi, pishloq, talqon, ketchup"],
    "Fries (90g)": ["Cheese Nuggets", 17000, 1, "images/Fries(90g).jpg", "kartoshka fri, ketchup"],
    "Hot Shots": ["Cheese Nuggets", 12000, 1, "images/HotShots.jpg", "Achchiq Tovuq File, Maxsus Un, Ketchup"],
    "Fries small": ["Cheese Nuggets", 12000, 1, "images/Friessmall.jpg", "mini kartoshka fri"],
    "Hot Wings 3pcs": ["Cheese Nuggets", 12000, 1, "images/HotWings3pcs.jpg", "ssiq tovuq qanotlari"],
    "Strips 3pcs": ["Cheese Nuggets", 12000, 1, "images/Strips3pcs.jpg", "Stripslar"],

    # Ice Cream & Milkshake
    "Milkshake (Strawberry)": ["Milkshake (Strawberry)", 16000, 1, "images/Milkshake.jpg", "Muzqaymoq, Sut, Qulupnay Sous"],
    "Chilly Ice (500g)": ["Chilly Ice (500g)", 20000, 1, "images/Chilly.jpg", "muzqaymoq (500gr)"],
    "Chocolate Ice Cream": ["Chocolate Ice Cream", 9000, 1, "images/ChocolateIceCream.jpg", "Shokoladli Muzqaymoq"],
    "LoookFlurry Bingo": ["LoookFlurry Bingo", 14000, 1, "images/LoookFlurryBingo.jpg", "Muzqaymoq, Pechene, Shokolad Sous"],
    "LoookFlurry Wafer": ["LoookFlurry Wafer", 27000, 1, "images/LoookFlurry.jpg", "Loookflurry Wafer"],
    "Strawberry Ice Cream": ["Strawberry Ice Cream", 9000, 1, "images/StrawberryIceCream.jpg", "Qulupnayli muzqaymoq"],
    "Milkshake Banana": ["Milkshake Banana", 23000, 1, "images/MilkshakeBanana.jpg", "MilkshakeBanana"],
    "Milkshake Choco": ["Milkshake Choco", 23000, 1, "images/MilkshakeChoco.jpg", "Muzqaymoq, Sut, Shokolad Sous"],

    # Ichimliklar
    "Dinay": ["Dinay", 10000, 1, "images/Dinay.jpg", "Dinay"],
    "Sprite разлив": ["Sprite разлив", 9000, 1, "images/Spriteразлив.jpg", "Sprite"],
    "Fanta разлив": ["Fanta разлив", 10000, 1, "images/Fantaразлив.jpg", "Fanta"],
    "Coca-Cola разлив": ["Coca-Cola разлив", 10000, 1, "images/Coca-Colaразлив.jpg", "Coca-Cola"],
    "Mineralka bezgaz": ["Mineralka bezgaz", 5000, 1, "images/Mineralkabezgaz.jpg", "не газированная вода "],
    # "Sok 1L (Ananas)": ["Sok 1L (Ananas)", 10000, 1, "images/.jpg", ""],
    # "Sok 1L (Apelsin)": ["Sok 1L (Apelsin)", 10000, 1, "images/.jpg", ""],
    "Coca-Cola": ["Coca-Cola", 10000, 1, "images/CocaCola1.5л.jpg", "Coca Cola 1.5 l "],
    "Fanta": ["Fanta", 10000, 1, "images/Fanta0.5л.jpg", "Tetiklantiruvchi Fanta"],
    "Ice-Tea": ["Ice-Tea", 15000, 1, "images/Ice Tea.jpg", "Ice Tea"],
    "Mineralka gaz": ["Mineralka bezgaz", 5000, 1, "images/Mineralkagaz0.5l.jpg", ""],
    "Sprite": ["Sprite", 15000, 1, "images/Sprite0.5л.jpg", "Tetiklantiruvchi Sprite"],
    # "Sok 1L": ["Sok 1L", 10000, 1, "images/.jpg", ""],
    # "Issiq-Ichimliklar": ["Issiq-Ichimliklar", 18000, 1, "images/.jpg", ""],

    # General (Asosiy Mahsulotlar)
    "WINGS 5 PCS - STRIPS 8 PCS (MIX) (0.5kg +-)": ["WINGS 5 PCS - STRIPS 8 PCS (MIX) (0.5kg +-)", 120000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "WINGS 10 PCS - STRIPS 16 PCS (MIX) (1kg +-)": ["WINGS 10 PCS - STRIPS 16 PCS (MIX) (1kg +-)", 150000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "16 PCS STRIPS (0.5kg +-)": ["16 PCS STRIPS (0.5kg +-)", 180000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "32 PCS STRIPS (1kg +-)": ["32 PCS STRIPS (1kg +-)", 220000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "11 PCS WINGS (0.5kg +-)": ["11 PCS WINGS (0.5kg +-)", 110000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "21 PCS WINGS (1kg +-)": ["21 PCS WINGS (1kg +-)", 200000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "16 NORMAL/16 SPICY + 32 WING": ["16 NORMAL/16 SPICY + 32 WING", 180000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "24 SPICY + 24 STRIPS": ["24 SPICY + 24 STRIPS", 240000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "24 NORMAL + 12 STRIPS/12 WINGS": ["24 NORMAL + 12 STRIPS/12 WINGS", 240000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],
    "12 NORMAL/12 SPICY + 24 WING": ["12 NORMAL/12 SPICY + 24 WING", 120000, 1, "images/WINGS10PCS-STRIPS16PCS(MIX)(1kg +-).jpg", "achchiq qanotlar, tovuq file, maxsus un, ketchup"],

    # Tog'ora
    "24 NORMAL + 24 STRIPS": ["24 NORMAL + 24 STRIPS", 340000, 1, "images/24NORMAL+24STRIPS.jpg", ""],
    "32 PIECE NORMAL + 32 WING": ["32 PIECE NORMAL + 32 WING", 400000, 1, "images/24NORMAL+24STRIPS.jpg", ""],
    "32 PIECE NORMAL + 32 STRIPS": ["32 PIECE NORMAL + 32 STRIPS", 400000, 1, "images/24NORMAL+24STRIPS.jpg", ""],
    "24 SPICY + 24 WING": ["24 SPICY + 24 WING", 340000, 1, "images/24NORMAL+24STRIPS.jpg", ""],
    "24 NORMAL + 24 WINGS": ["24 NORMAL + 24 WINGS", 340000, 1, "images/24NORMAL+24STRIPS.jpg", ""],

    # Vafli
    "Gonkong konsuli": ["Gonkong konsuli", 40000, 1, "images/Gonkongkonusli.jpg", "Muzqaymoq, banan, qulupnay, shokolad, vafli  "],
    "Gonkong muzqaymoq vaflisi": ["Gonkong muzqaymoq vaflisi", 37000, 1, "images/Gonkong muzqaymoqli vaflisi.jpg", "Vafli, muzqaymoq, shokolad, banan"],
    "Belgiya bananli vaflisi": ["Belgiya bananli vaflisi", 17000, 1, "images/Belgiya bananli vaflisi  .jpg", "Vafli, banan, shokold"],
    "Belgiya mini vaflisi": ["Belgiya mini vaflisi", 17000, 1, "images/Belgiya mini vaflisi  .jpg", "Vafli, shokolad, muzqaymoq  "],
    "Lorenti Fondyu": ["Lorenti Fondyu", 75000, 1, "images/Lorenti.jpg", "Nutella, shokolad, banan, qulupnay"],
    "Belgiya shokoladli vaflisi": ["Belgiya shokoladli vaflisi", 28000, 1, "images/Belgiya shokoladli vaflisi.jpg", "Vafli, shokolad"],
    "Vena vaflisi": ["Vena vaflisi", 39000, 1, "images/Vena.jpg", "Muzqaymoq, banan, qulupnay, shokolad, vafli  "],
    "Vena shokoladli vaflisi": ["Vena shokoladli vaflisi", 39000, 1, "images/Vena shokoladli vaflisi.jpg", "Muzqaymoq, banan, qulupnay, shokolad, vafli  "],
    "Belgiya qulupnayli vaflisi": ["Belgiya qulupnayli vaflisi", 40000, 1, "images/Belgiya qulupnayli vaflisi  .jpg", "Qulupnay, shokolad, vaffli"],

    # Ava Pizza
    # "Ava Pizza": ["Ava Pizza", 40000, 1, "images/.jpg", ""]

}

