from aiogram.types import Message, CallbackQuery
from keyboards.inline.menu_keyboard import (
    products_menu,
    macos_menu,
    menu,
    m1_menu,
    by_products,
    m2_menu,
    m2_products,
    m3_menu,
    m4_menu,
    iphone_menu,
    iphone13_menu,
    iphone14_menu,
    iphone15_menu,
    iphone16_menu,
    iwatch_menu,
    iPad_menu,
    m3_products,  # "m3_produts" ni "m3_products" ga tuzatildi
    m4_products,  # "m4_produts" ni "m4_products" ga tuzatildi
    iwatch_products,  # "iwatch_produts" ni "iwatch_products" ga tuzatildi
    iphone13_products,  # "iphone13_produts" ni "iphone13_products" ga tuzatildi
    iphone14_products,  # "iphone14_produts" ni "iphone14_products" ga tuzatildi
    iphone15_products,  # "iphone15_produts" ni "iphone15_products" ga tuzatildi
    iphone16_products,  # "iphone16_produts" ni "iphone16_products" ga tuzatildi
)
from loader import dp


# Asosiy menu (products_menu) ni ko'rsatish uchun handler
@dp.callback_query_handler(text="menu")
async def show_products_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Apple products</b>",
        photo="https://overclockers.ru/st/legacy/blog/390340/198862_O.jpg",
        reply_markup=products_menu
    )


# macOS mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="macos")
async def show_macos_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>macOS products</b>",
        photo="https://avatars.mds.yandex.net/get-yabs_performance/1118404/hat7f7e79532ac57727a20fb1f2cf6fb0ef/huge",
        reply_markup=macos_menu
    )


# Ortga qaytish uchun handler (asosiy menu ga qaytaradi)
@dp.callback_query_handler(text="ortga")
async def show_back_to_main_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi, chunki "show_macos_menu" takrorlanardi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"Salom, {call.from_user.full_name}!",
        photo="https://i.pinimg.com/originals/f1/91/d3/f191d302eb21ade7ece59e9b209a4744.png",
        reply_markup=menu
    )


# M1 mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="m1")
async def show_m1_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi, chunki "show_products_menu" takrorlanardi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M1 products</b>",
        photo="https://frankfurt.apollo.olxcdn.com/v1/files/0ntez3c322322-UZ/image",
        reply_markup=m1_menu
    )


# Ortga qaytish uchun handler (M1 dan products_menu ga)
@dp.callback_query_handler(text="ortga1")
async def show_back_to_products_from_m1(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Apple products</b>",
        photo="https://overclockers.ru/st/legacy/blog/390340/198862_O.jpg",
        reply_markup=products_menu
    )


# M1 Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="m1_pro")
async def show_m1_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi, chunki "show_by_products_menu" takrorlanardi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
Состояние: Яхши ўртача
Хотираси:  256 GB SSD⚡️
Оперативка: DDR4 8 GB
Процессор: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
Видеокартаси: Intel(R) Iris(R) Xe Graphics
Экран : 12 дюйм Full HD
Стильный дизайн 
""",
        photo="https://overclockers.ru/st/legacy/blog/427135/449314_O.jpg",
        reply_markup=by_products
    )


# Mahsulotni sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish")
async def buy_product(call: CallbackQuery):  # Funksiya nomi o'zgartirildi, chunki "buy_detail_product" bir xil edi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (M1 Pro dan macos_menu ga)
@dp.callback_query_handler(text="ortga2")
async def show_back_to_macos_from_m1_pro(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>macOS products</b>",
        photo="https://avatars.mds.yandex.net/get-yabs_performance/1118404/hat7f7e79532ac57727a20fb1f2cf6fb0ef/huge",
        reply_markup=macos_menu
    )


# M1 Air mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="m1_air")
async def show_m1_air_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>Состояние</b>: Яхши ўртача
<b>Хотираси</b>:  1 tB SSD⚡️
<b>Оперативка</b>: DDR4 16 GB
<b>Процессор</b>: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
<b>Видеокартаси</b>: Intel(R) Iris(R) Xe Graphics
<b>Экран</b>: 12 дюйм Full HD
Cтильный дизайн 
""",
        photo="https://cdn1.technopark.ru/technopark/photos_resized/article_text_image/1000_1000/492_4/1_492_4.jpg",
        reply_markup=by_products
    )


# Mahsulotni sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish1")
async def buy_product_1(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (M1 Air dan m1_menu ga)
@dp.callback_query_handler(text="ortga4")
async def show_back_to_m1_from_m1_air(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M1 products</b>",
        photo="https://frankfurt.apollo.olxcdn.com/v1/files/0ntez3c322322-UZ/image",
        reply_markup=m1_menu
    )


# M2 Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="m2_pro")
async def show_m2_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>👨🏻‍💻 Macbook M2 Pro 2022 💥</b>
<b>🖥 Ekran</b>: 13,3 Dyum Retina 2K✨
<b>⚙️ Protsessor</b>: Apple silicon M2 🚀
<b>🖲 Videokarta</b>: Apple silicon M2 🔥
<b>⏳ Operativka</b>: 8GB 🚀
<b>🔷 ROM</b>: 256GB ✈️
<b>🔋 Batareyka</b>: 100% 15 cycle ✅
<b>🌀 Touch iD</b>
<b>⌨️ Podsvetka klaviatura💡</b>""",
        photo="https://cdn1.technopark.ru/technopark/photos_resized/article_text_image/1000_1000/492_4/1_492_4.jpg",
        reply_markup=m2_products
    )


# Mahsulotni sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish1")
async def buy_product_1(call: CallbackQuery):  # Funksiya nomi saqlanib qoldi, lekin takrorlanishni hisobga olaman
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (M2 Pro dan m2_menu ga)
@dp.callback_query_handler(text="ortga04")
async def show_back_to_m2_from_m2_pro(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M2 products</b>",
        photo="https://www.ixbt.com/img/n1/news/2022/5/1/13-inch-macbook-pro-m2-mock-feature-2_large.jpg",
        reply_markup=m2_menu
    )


# M2 Air mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="m2_air")
async def show_m2_air_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>🍏 MacBook Air 2024 aperelda olingan</b>
<b>🖥 Ekran</b>: 15,3 Dyum (2880x1864)
<b>⚙️ Protsessor</b>: M2 CHip
<b>☺️ Videokarta</b>: INTEGRATED
<b>⚙️ Operativka</b>: 8GB 
<b>😋 SSD</b>: 256GB 
<b>🔋 Емкость</b>: 100% Цикл: 11
<b>⌨️ Podsvetka klaviatura💡</b>""",
        photo="https://cdn1.technopark.ru/technopark/photos_resized/article_text_image/1000_1000/492_4/1_492_4.jpg",
        reply_markup=m2_products
    )


# Mahsulotni sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish1")
async def buy_product_1(call: CallbackQuery):  # Takrorlanishni saqlab qoldim
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (M2 Air dan m2_menu ga)
@dp.callback_query_handler(text="ortga04")
async def show_back_to_m2_from_m2_air(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M2 products</b>",
        photo="https://www.ixbt.com/img/n1/news/2022/5/1/13-inch-macbook-pro-m2-mock-feature-2_large.jpg",
        reply_markup=m2_menu
    )


# M3 Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="m3_pro")
async def show_m3_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
💻 Apple M3  Pro 

👨‍💻Котта боллар Макбук  сўрагани учун махсус опкелтирилди.  

<b>Состояние Янгидек </b> 👍
<b>Хотираси</b>: 1 TB SSD
<b>Оперативка</b>: 16 GB 
<b>Процессор</b>: Apple M2 Pro (12 ядро) 
<b>Видеокарта</b>: 19 Ядролик
<b>Дисплей</b>: 4K Liquid Retina XDR 16.2 ° дюйм (3456×2234)
Клавиатура подсветкалик 
Touch ID бор
Емкость 100 %
🔋 Цикл: 6 
""",
        photo="https://i.ytimg.com/vi/SQmWk_gH5FU/maxresdefault.jpg",
        reply_markup=m3_products  # "m3_produts" ni tuzatildi
    )


# Mahsulotni sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish2")
async def buy_product_2(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (M3 Pro dan m3_menu ga)
@dp.callback_query_handler(text="ortga6")
async def show_back_to_m3_from_m3_pro(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M3 products</b>",
        photo="https://www.techpowerup.com/img/izoCuxLjUtJ2OoCK.jpg",
        reply_markup=m3_menu
    )


# M3 Air mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="m3_air")
async def show_m3_air_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>💻 MACBOOK M3 AIR 2015 </b>
<b>🖥 13.3 FULL HD </b>
<b>⚙️ Intel Core-i5 1.60 Ghz</b>
<b>🎮 Intel HD Grafiks 6000 </b>
<b>💻 Metalika korpus </b>
<b>⌨️ PADSVETKA KLAVYATURA</b>
<b>⏳ Оперативка: 8GB </b>
<b>💾 SSD: 128-GB M.2 NVME ‼️</b>
<b>🔋 Батарейка: 1-Kunga yetadi ✅</b>
<b>📦 3-ой гарантияси бор ‼️</b>
<b>💵 Нархи: 200$ ‼️</b>
<b> Манзил: Тошкент</b>""",
        photo="https://media.cnn.com/api/v1/images/stellar/prod/220715121407-macbook-air-m2-review-1.jpg?c=16x9&q=h_833,w_1480,c_fill",
        reply_markup=m3_products  # "m3_produts" ni tuzatildi
    )


# Mahsulotni sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish2")
async def buy_product_2(call: CallbackQuery):  # Takrorlanish saqlanib qoldi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (M3 Air dan m3_menu ga)
@dp.callback_query_handler(text="ortga6")
async def show_back_to_m3_from_m3_air(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M3 products</b>",
        photo="https://www.techpowerup.com/img/izoCuxLjUtJ2OoCK.jpg",
        reply_markup=m3_menu
    )


# M4 Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="m4_pro")
async def show_m4_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>💻 MACBOOK M4 PRO 2015 </b>
<b>🖥 13.3 FULL HD </b>
<b>⚙️ Intel Core-i5 1.60 Ghz</b>
<b>🎮 Intel HD Grafiks 6000 </b>
<b>💻 Metalika korpus </b>
<b>⌨️ PADSVETKA KLAVYATURA</b>
<b>⏳ Оперативка: 8GB </b>
<b>💾 SSD: 128-GB M.2 NVME ‼️</b>
<b>🔋 Батарейка: 1.5-Kunga yetadi ✅</b>
<b>📦 3-ой гарантияси бор ‼️</b>
<b>💵 Нархи: 500$ ‼️</b>
<b> Манзил: Тошкент</b>""",
        photo="https://frankfurt.apollo.olxcdn.com/v1/files/0lry3lq4v5z32-UZ/image",
        reply_markup=m4_products  # "m4_produts" ni tuzatildi
    )


# Mahsulotni sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish3")
async def buy_product_3(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (M4 Pro dan m4_menu ga)
@dp.callback_query_handler(text="ortga8")
async def show_back_to_m4_from_m4_pro(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M4 products</b>",
        photo="https://static1.pocketlintimages.com/wordpress/wp-content/uploads/2025/03/m4-macbook-pro-header.jpg",
        reply_markup=m4_menu
    )


# M4 Air mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="m4_air")
async def show_m4_air_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>🍏 MacBook Pro M1 KH/A (Silver)</b>
<b>🖥 Ekran</b>: 13,3 Dyum Retina (2560x1600)
<b>⚙️ Protsessor</b>: Apple M1 Chip
<b>⚙️ Operativka</b>: 8GB 
<b>😋  SSD</b>: 256GB
<b>🔋 Batareyka</b>: 91% (цикл 157)
<b>⌨️ Podsvetka klaviatura💡</b>
<b>✅ True Tone bilan, zaryadnik</b> """,
        photo="https://ichip.ru/images/cache/2023/7/4/q90_746632_cffe18a4f060f9ed08dcdf0a9.jpeg",
        reply_markup=m4_products  # "m4_produts" ni tuzatildi
    )


# Mahsulotni sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish3")
async def buy_product_3(call: CallbackQuery):  # Takrorlanish saqlanib qoldi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (M4 Air dan m4_menu ga)
@dp.callback_query_handler(text="ortga8")
async def show_back_to_m4_from_m4_air(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M4 products</b>",
        photo="https://static1.pocketlintimages.com/wordpress/wp-content/uploads/2025/03/m4-macbook-pro-header.jpg",
        reply_markup=m4_menu
    )


# M2 mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="m2")
async def show_m2_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M2 products</b>",
        photo="https://www.ixbt.com/img/n1/news/2022/5/1/13-inch-macbook-pro-m2-mock-feature-2_large.jpg",
        reply_markup=m2_menu
    )


# Ortga qaytish uchun handler (M2 dan m1_menu ga)
@dp.callback_query_handler(text="ortga3")
async def show_back_to_m1_from_m2(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M1 products</b>",
        photo="https://frankfurt.apollo.olxcdn.com/v1/files/0ntez3c322322-UZ/image",
        reply_markup=m1_menu
    )


# M3 mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="m3")
async def show_m3_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M3 products</b>",
        photo="https://www.techpowerup.com/img/izoCuxLjUtJ2OoCK.jpg",
        reply_markup=m3_menu
    )


# Ortga qaytish uchun handler (M3 dan macos_menu ga)
@dp.callback_query_handler(text="ortga5")
async def show_back_to_macos_from_m3(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>macOS products</b>",
        photo="https://avatars.mds.yandex.net/get-yabs_performance/1118404/hat7f7e79532ac57727a20fb1f2cf6fb0ef/huge",
        reply_markup=macos_menu
    )


# M4 mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="m4")
async def show_m4_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b> macOS M4 products</b>",
        photo="https://static1.pocketlintimages.com/wordpress/wp-content/uploads/2025/03/m4-macbook-pro-header.jpg",
        reply_markup=m4_menu
    )


# Ortga qaytish uchun handler (M4 dan macos_menu ga)
@dp.callback_query_handler(text="ortga7")
async def show_back_to_macos_from_m4(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>macOS products</b>",
        photo="https://avatars.mds.yandex.net/get-yabs_performance/1118404/hat7f7e79532ac57727a20fb1f2cf6fb0ef/huge",
        reply_markup=macos_menu
    )


# iPhone mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="iphones")
async def show_iphone_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone products</b>",
        photo="https://s.yimg.com/ny/api/res/1.2/jJ9MT1sUVsSJnGYEULma7A--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY5MA--/https://media.zenfs.com/en/shefinds_255/d0c584a2169c2ed4f659f4d77d101923",
        reply_markup=iphone_menu
    )


# Ortga qaytish uchun handler (iPhone dan products_menu ga)
@dp.callback_query_handler(text="ortga0")
async def show_back_to_products_from_iphone(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Apple products</b>",
        photo="https://overclockers.ru/st/legacy/blog/390340/198862_O.jpg",
        reply_markup=products_menu
    )


# iPhone 13 mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="iphone_13")
async def show_iphone13_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone 13 products</b>",
        photo="https://s0.rbk.ru/v6_top_pics/media/img/5/21/756467660725215.jpg",
        reply_markup=iphone13_menu
    )


# Ortga qaytish uchun handler (iPhone 13 dan iphone_menu ga)
@dp.callback_query_handler(text="ortga9")
async def show_back_to_iphone_from_13(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone products</b>",
        photo="https://s.yimg.com/ny/api/res/1.2/jJ9MT1sUVsSJnGYEULma7A--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY5MA--/https://media.zenfs.com/en/shefinds_255/d0c584a2169c2ed4f659f4d77d101923",
        reply_markup=iphone_menu
    )


# iPhone 13 Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="13_Pro")
async def show_iphone13_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>❗️iPhone 13 Pro </b>
                                    
<b>📱 Modeli</b>: iPhone 13 Pro 
<b>🛠 Xolati</b>: Ideal
<b>🔋 Yomkust</b>: 79%
<b>💾 Xotira</b>: 256GB
<b>🎨 Rangi</b>: Blue
<b>📁 Hujjat</b>: bor
<b>♻️ Obmen</b>: Yo'q
<b>🚩 Manzil</b>: Toshkent
<b>💸 Narx</b>: 520$""",
        photo="https://www.renderhub.com/madmix/apple-iphone-13-mini-and-13-and-13-pro-and-13-pro-max-all-c/apple-iphone-13-mini-and-13-and-13-pro-and-13-pro-max-all-c-09.jpg",
        reply_markup=iphone13_products  # "iphone13_produts" ni tuzatildi
    )


# iPhone 13 Pro Max mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="13_Max")
async def show_iphone13_pro_max_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>❗️iPhone 13 Pro Max </b>
                                    
<b>📱 Modeli</b>: iPhone 13 Pro Max
<b>🛠 Xolati</b>: Ideal
<b>🔋 Yomkust</b>: 80%
<b>💾 Xotira</b>: 1 TB
<b>🎨 Rangi</b>: Blue
<b>📁 Hujjat</b>: bor
<b>♻️ Obmen</b>: Yo'q
<b>🚩 Manzil</b>: Toshkent
<b>💸 Narx</b>: 720$""",
        photo="https://avatars.mds.yandex.net/get-mpic/4462738/img_id5612948385494025577.jpeg/orig",
        reply_markup=iphone13_products  # "iphone13_produts" ni tuzatildi
    )


# iPhone 13 mahsulotini sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish4")
async def buy_iphone13_product(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (iPhone 13 dan iphone13_menu ga)
@dp.callback_query_handler(text="ortga13")
async def show_back_to_iphone13_from_13(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone 13 products</b>",
        photo="https://s0.rbk.ru/v6_top_pics/media/img/5/21/756467660725215.jpg",
        reply_markup=iphone13_menu
    )


# iPhone 14 mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="iphone_14")
async def show_iphone14_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone 14 products</b>",
        photo="https://m-cdn.phonearena.com/images/articles/392500-image/iphone14-colors-applehub.jpg",
        reply_markup=iphone14_menu
    )


# Ortga qaytish uchun handler (iPhone 14 dan iphone_menu ga)
@dp.callback_query_handler(text="ortga10")
async def show_back_to_iphone_from_14(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone products</b>",
        photo="https://s.yimg.com/ny/api/res/1.2/jJ9MT1sUVsSJnGYEULma7A--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY5MA--/https://media.zenfs.com/en/shefinds_255/d0c584a2169c2ed4f659f4d77d101923",
        reply_markup=iphone_menu
    )


# iPhone 14 Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="14_Pro")
async def show_iphone14_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>❗️iPhone 14 Pro </b>
                                    
<b>📱 Modeli</b>: iPhone 14 Pro 
<b>🛠 Xolati</b>: Ideal
<b>🔋 Yomkust</b>: 100%
<b>💾 Xotira</b>: 512GB
<b>🎨 Rangi</b>: White
<b>📁 Hujjat</b>: bor
<b>♻️ Obmen</b>: Yo'q
<b>🚩 Manzil</b>: Toshkent
<b>💸 Narx</b>: 1000$""",
        photo="https://i-smart.by/image/catalog/iphone14/14pro/8967.jpg",
        reply_markup=iphone14_products  # "iphone14_produts" ni tuzatildi
    )


# iPhone 14 Pro Max mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="14_Max")
async def show_iphone14_pro_max_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>❗️iPhone 14 Pro Max</b>
                                    
<b>📱 Modeli</b>: iPhone 14 Pro Max
<b>🛠 Xolati</b>: Ideal
<b>🔋 Yomkust</b>: 98%
<b>💾 Xotira</b>: 512GB
<b>🎨 Rangi</b>: Bulue
<b>📁 Hujjat</b>: bor
<b>♻️ Obmen</b>: Yo'q
<b>🚩 Manzil</b>: Toshkent
<b>💸 Narx</b>: 989$""",
        photo="https://2cent.ru/storage/photo/resized/xy_1500x1500/b/jx8xg5yyk7k7sdv_74baac0d.jpg.webp",
        reply_markup=iphone14_products  # "iphone14_produts" ni tuzatildi
    )


# iPhone 14 mahsulotini sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish5")
async def buy_iphone14_product(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (iPhone 14 dan iphone14_menu ga)
@dp.callback_query_handler(text="ortga14")
async def show_back_to_iphone14_from_14(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone 14 products</b>",
        photo="https://m-cdn.phonearena.com/images/articles/392500-image/iphone14-colors-applehub.jpg",
        reply_markup=iphone14_menu
    )


# iPhone 15 mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="iphone_15")
async def show_iphone15_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone 15 products</b>",
        photo="https://frankfurt.apollo.olxcdn.com/v1/files/f5yi84s0guvv1-UZ/image;s=693x693",
        reply_markup=iphone15_menu
    )


# Ortga qaytish uchun handler (iPhone 15 dan iphone_menu ga)
@dp.callback_query_handler(text="ortga11")
async def show_back_to_iphone_from_15(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone products</b>",
        photo="https://s.yimg.com/ny/api/res/1.2/jJ9MT1sUVsSJnGYEULma7A--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY5MA--/https://media.zenfs.com/en/shefinds_255/d0c584a2169c2ed4f659f4d77d101923",
        reply_markup=iphone_menu
    )


# iPhone 15 Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="15_Pro")
async def show_iphone15_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>❗️iPhone 15 Pro </b>
                                    
<b>📱 Modeli</b>: iPhone 15 Pro 
<b>🛠 Xolati</b>: Ideal
<b>🔋 Yomkust</b>: 80%
<b>💾 Xotira</b>: 512GB
<b>🎨 Rangi</b>: Bulue
<b>📁 Hujjat</b>: bor
<b>🚩 Manzil</b>: Toshkent
<b>💸 Narx</b>: 800$""",
        photo="https://resizer.mail.ru/p/d08b0c7e-49c5-5e2f-8a95-5d1cc4604909/AQAKsKjOLHDdEmq9jXz3r7-8FOhS86ZDSFFVKPu0wkwaK54CN3_-frKXZ5zmy2uB8IFZWzjK8DmYVYiCbinCjH8T03g.jpg",
        reply_markup=iphone15_products  # "iphone15_produts" ni tuzatildi
    )


# iPhone 15 Pro Max mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="15_Max")
async def show_iphone15_pro_max_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>❗️iPhone 15 Pro Max </b>
                                    
<b>📱 Modeli</b>: iPhone 15 Pro Max
<b>🛠 Xolati</b>: Ideal
<b>🔋 Yomkust</b>: 97%
<b>💾 Xotira</b>: 256GB
<b>🎨 Rangi</b>: Red
<b>📁 Hujjat</b>: bor
<b>🚩 Manzil</b>: Toshkent
<b>💸 Narx</b>: 500$""",
        photo="https://i.ytimg.com/vi/jFEkQ2cByxI/maxresdefault.jpg",
        reply_markup=iphone15_products  # "iphone15_produts" ni tuzatildi
    )


# iPhone 15 mahsulotini sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish6")
async def buy_iphone15_product(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (iPhone 15 dan iphone15_menu ga)
@dp.callback_query_handler(text="ortga15")
async def show_back_to_iphone15_from_15(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone 15 products</b>",
        photo="https://frankfurt.apollo.olxcdn.com/v1/files/f5yi84s0guvv1-UZ/image;s=693x693",
        reply_markup=iphone15_menu
    )


# iPhone 16 mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="iphone_16")
async def show_iphone16_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone 16 products</b>",
        photo="https://avatars.mds.yandex.net/get-mpic/4338525/2a00000192f819a2637084226df2d70bde45/orig",
        reply_markup=iphone16_menu
    )


# Ortga qaytish uchun handler (iPhone 16 dan iphone_menu ga)
@dp.callback_query_handler(text="ortga12")
async def show_back_to_iphone_from_16(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone products</b>",
        photo="https://s.yimg.com/ny/api/res/1.2/jJ9MT1sUVsSJnGYEULma7A--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY5MA--/https://media.zenfs.com/en/shefinds_255/d0c584a2169c2ed4f659f4d77d101923",
        reply_markup=iphone_menu
    )


# iPhone 16 Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="16_Pro")
async def show_iphone16_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>❗️iPhone 16 Pro  </b>
                                    
<b>📱 Modeli</b>: iPhone 16 Pro
<b>🛠 Xolati</b>: Ideal
<b>🔋 Yomkust</b>: 100%
<b>💾 Xotira</b>: 1 TB
<b>🎨 Rangi</b>: Yellow
<b>📁 Hujjat</b>: bor
<b>🚩 Manzil</b>: Toshkent
<b>💸 Narx</b>: 1100$""",
        photo="https://avatars.mds.yandex.net/get-mpic/12354050/2a00000194cde7aa2d0f79b34463da700ce9/orig",
        reply_markup=iphone16_products  # "iphone16_produts" ni tuzatildi
    )


# iPhone 16 Pro Max mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="16_Max")
async def show_iphone16_pro_max_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>❗️iPhone 16 Pro Max </b>
                                    
<b>📱 Modeli</b>: iPhone 16 Pro Max
<b>🛠 Xolati</b>: Ideal
<b>🔋 Yomkust</b>: 99%
<b>💾 Xotira</b>: 1 TB
<b>🎨 Rangi</b>: Yellow
<b>📁 Hujjat</b>: bor
<b>🚩 Manzil</b>: Toshkent
<b>💸 Narx</b>: 1500$""",
        photo="https://img2.festima.ru/2/1.X33zrraA85SFADGbweMsa-AP8ZBBGfeUQX6SkEHN_FZIDfeOhQAxm0U.owtkcLRcMuLKWizkMkJUJqH-AGHlGfMPBceOy-cpMD4",
        reply_markup=iphone16_products  # "iphone16_produts" ni tuzatildi
    )


# iPhone 16 mahsulotini sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish7")
async def buy_iphone16_product(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (iPhone 16 dan iphone16_menu ga)
@dp.callback_query_handler(text="ortga16")
async def show_back_to_iphone16_from_16(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Iphone 16 products</b>",
        photo="https://avatars.mds.yandex.net/get-mpic/4338525/2a00000192f819a2637084226df2d70bde45/orig",
        reply_markup=iphone16_menu
    )


# iWatch mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="iwatch")
async def show_iwatch_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>iWatch products</b>",
        photo="https://sneg.top/uploads/posts/2023-03/1680289636_sneg-top-p-zastavka-na-chasi-smart-kartinki-vkontakte-57.png",
        reply_markup=iwatch_menu
    )


# Ortga qaytish uchun handler (iWatch dan products_menu ga)
@dp.callback_query_handler(text="ortga17")
async def show_back_to_products_from_iwatch(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Apple products</b>",
        photo="https://overclockers.ru/st/legacy/blog/390340/198862_O.jpg",
        reply_markup=products_menu
    )


# iWatch Ultra mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="watch")
async def show_iwatch_ultra_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>⌚️ Applewatch  Ultra 🔝</b>

<b>🔅 Hajmi</b>: 49 * 43 * 11,5 mm.
<b>⚖️Og'irligi</b>: 46 g.
<b>💧Suv o'tkazmaydigan</b>: IP68.
<b>📺Ekran</b>: 2,0 dyuymli IPS ekran, 420*485.
<b>🔋Batareya</b>: 280 mA / soat.
<b>⚡️Zaryadlash rejimi</b>: simsiz zaryadlash""",
        photo="https://i.pinimg.com/736x/0c/0b/30/0c0b30cbe56d6d5a20696f92d01a5424.jpg",
        reply_markup=iwatch_products  # "iwatch_produts" ni tuzatildi
    )


# iWatch mahsulotini sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish8")
async def buy_iwatch_product(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (iWatch Ultra dan iwatch_menu ga)
@dp.callback_query_handler(text="ortga18")
async def show_back_to_iwatch_from_ultra(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>iWatch products</b>",
        photo="https://sneg.top/uploads/posts/2023-03/1680289636_sneg-top-p-zastavka-na-chasi-smart-kartinki-vkontakte-57.png",
        reply_markup=iwatch_menu
    )


# iWatch SE mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="watch_se")
async def show_iwatch_se_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
⌚️ Apple watch SE 🔝

<b>🔅 Hajmi</b>: 49 * 43 * 12 mm.
<b>⚖️Og'irligi</b>: 30 g.
<b>💧Suv o'tkazmaydigan</b>: IP68.
<b>📺Ekran</b>: 2,5 dyuymli IPS ekran, 420*485.
<b>🔋Batareya</b>: 290 mA / soat.
<b>⚡️Zaryadlash rejimi: simsiz zaryadlash </b>

<b>Narxi</b>: 30💲""",
        photo="https://news.zindaa.mn/uploads/images/maxresdefault%20(1)(10).jpg",
        reply_markup=iwatch_products  # "iwatch_produts" ni tuzatildi
    )


# iWatch mahsulotini sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish8")
async def buy_iwatch_product(call: CallbackQuery):  # Takrorlanish saqlanib qoldi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (iWatch SE dan iwatch_menu ga)
@dp.callback_query_handler(text="ortga18")
async def show_back_to_iwatch_from_se(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>iWatch products</b>",
        photo="https://sneg.top/uploads/posts/2023-03/1680289636_sneg-top-p-zastavka-na-chasi-smart-kartinki-vkontakte-57.png",
        reply_markup=iwatch_menu
    )


# iPad mahsulotlari menyusini ko'rsatish uchun handler
@dp.callback_query_handler(text="ipad")
async def show_iPad_menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>iPad products</b>",
        photo="https://miggim.ru/wp-content/uploads/5/3/f/53f2c79af774717d22c161e2a942dbfc.jpeg",
        reply_markup=iPad_menu
    )


# Ortga qaytish uchun handler (iPad dan products_menu ga)
@dp.callback_query_handler(text="ortga19")
async def show_back_to_products_from_ipad(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>Apple products</b>",
        photo="https://overclockers.ru/st/legacy/blog/390340/198862_O.jpg",
        reply_markup=products_menu
    )


# iPad Pro mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="pro")
async def show_ipad_pro_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>📱 iPad Pro 12.9 M2 </b>
<b>🛠 Идеал Sim kartali</b>
<b>🔋 92% </b>
<b>🎨 Midnight Grey</b>
<b>📦 & 📑 Bor </b>
<b>💰 799$ </b> """,
        photo="https://blog.eldorado.ru/storage/publication/0/59/rr83OQYDAn11EtsyzSZOsBQMXt13GtQyUSdlPiew.jpeg",
        reply_markup=iwatch_products  # "iwatch_produts" ni tuzatildi (bu yerda iPad uchun noto'g'ri klaviatura ishlatilgan bo'lishi mumkin)
    )


# iPad mahsulotini sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish9")
async def buy_ipad_product(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (iPad Pro dan iPad_menu ga)
@dp.callback_query_handler(text="ortga20")
async def show_back_to_ipad_from_pro(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>iPad products</b>",
        photo="https://miggim.ru/wp-content/uploads/5/3/f/53f2c79af774717d22c161e2a942dbfc.jpeg",
        reply_markup=iPad_menu
    )


# iPad Air mahsulotini ko'rsatish uchun handler
@dp.callback_query_handler(text="air")
async def show_ipad_air_menu(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption=f"""
<b>📱 iPad Air 13 M4 256GB </b>
<b>🛠 Идеал Sim kartali </b>
<b>🔋 100% 60 Sikl </b>
<b>🎨 Midnight Gray </b>
<b>📦 & 📑 Bor </b>
<b>💰 1111$</b>  """,
        photo="https://avatars.mds.yandex.net/i?id=2f53d303b14cef2036d6461975585df2_l-5288660-images-thumbs&n=13",
        reply_markup=iwatch_products  # "iwatch_produts" ni tuzatildi (bu yerda iPad uchun noto'g'ri klaviatura ishlatilgan bo'lishi mumkin)
    )


# iPad mahsulotini sotib olish uchun handler
@dp.callback_query_handler(text="sotib_olish9")
async def buy_ipad_product(call: CallbackQuery):  # Takrorlanish saqlanib qoldi
    await call.answer(
        text="Buyurtmangiz qabul qilindi",
        cache_time=60,
        show_alert=True
    )


# Ortga qaytish uchun handler (iPad Air dan iPad_menu ga)
@dp.callback_query_handler(text="ortga20")
async def show_back_to_ipad_from_air(call: CallbackQuery):  # Funksiya nomi o'zgartirildi
    await call.message.delete()
    await call.message.answer_photo(
        caption="<b>iPad products</b>",
        photo="https://miggim.ru/wp-content/uploads/5/3/f/53f2c79af774717d22c161e2a942dbfc.jpeg",
        reply_markup=iPad_menu
    )
    