from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛍 Menu", callback_data="menu"),
        ]
    ]
)

products_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 macOS", callback_data="macos"),
            InlineKeyboardButton(text="📱 iphones", callback_data="iphones"),
        ],
        [
            InlineKeyboardButton(text="⌚️ I Watch", callback_data="iwatch"),
            InlineKeyboardButton(text="📲 iPad", callback_data="ipad"),
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga"),
        ]
    ]
)

macos_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 MacBook M1", callback_data="m1"),
            InlineKeyboardButton(text="💻 MacBook M2", callback_data="m2")
        ],
        [
            InlineKeyboardButton(text="💻 MacBook M3", callback_data="m3"),
            InlineKeyboardButton(text="💻 MacBook M4", callback_data="m4")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga1")
        ]
    ]
)

m1_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 M1 Pro", callback_data="m1_pro"),
            InlineKeyboardButton(text="💻 M1 Air", callback_data="m1_air")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga2")
        ]
    ]
)

by_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga3")
        ]
    ]
)

m2_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 M2 Pro", callback_data="m2_pro"),
            InlineKeyboardButton(text="💻 M2 Air", callback_data="m2_air")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga3")  # "ortga2" dan "ortga3" ga o'zgartirildi, m1_menu bilan farqlanish uchun
        ]
    ]
)

m2_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish1"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga4")  # "ortga04" ni "ortga4" ga tuzatildi
        ]
    ]
)

m3_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 M3 Pro", callback_data="m3_pro"),
            InlineKeyboardButton(text="💻 M3 Air", callback_data="m3_air")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga5")
        ]
    ]
)

m3_products = InlineKeyboardMarkup(  # "m3_produts" ni "m3_products" ga tuzatildi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish2"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga6")
        ]
    ]
)

m4_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 M4 Pro", callback_data="m4_pro"),
            InlineKeyboardButton(text="💻 M4 Air", callback_data="m4_air")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga7")
        ]
    ]
)

m4_products = InlineKeyboardMarkup(  # "m4_produts" ni "m4_products" ga tuzatildi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish3"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga8")
        ]
    ]
)

iphone_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📱 Iphone 13", callback_data="iphone_13"),
            InlineKeyboardButton(text="📱 Iphone 14", callback_data="iphone_14")
        ],
        [
            InlineKeyboardButton(text="📱 Iphone 15", callback_data="iphone_15"),
            InlineKeyboardButton(text="📱 Iphone 16", callback_data="iphone_16")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga0")
        ]
    ]
)

iphone13_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📱 Iphone 13 Pro", callback_data="13_Pro"),
            InlineKeyboardButton(text="📱 Iphone 13 Pro Max", callback_data="13_Max")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga9")
        ]
    ]
)

iphone13_products = InlineKeyboardMarkup(  # "iphone13_produts" ni "iphone13_products" ga tuzatildi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish4"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga13")
        ]
    ]
)

iphone14_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📱 Iphone 14 Pro", callback_data="14_Pro"),
            InlineKeyboardButton(text="📱 Iphone 14 Pro Max", callback_data="14_Max")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga10")
        ]
    ]
)

iphone14_products = InlineKeyboardMarkup(  # "iphone14_produts" ni "iphone14_products" ga tuzatildi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish5"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga14")
        ]
    ]
)

iphone15_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📱 Iphone 15 Pro", callback_data="15_Pro"),
            InlineKeyboardButton(text="📱 Iphone 15 Pro Max", callback_data="15_Max")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga11")
        ]
    ]
)

iphone15_products = InlineKeyboardMarkup(  # "iphone15_produts" ni "iphone15_products" ga tuzatildi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish6"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga15")
        ]
    ]
)

iphone16_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📱 Iphone 16 Pro", callback_data="16_Pro"),
            InlineKeyboardButton(text="📱 Iphone 16 Pro Max", callback_data="16_Max")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga12")
        ]
    ]
)

iphone16_products = InlineKeyboardMarkup(  # "iphone16_produts" ni "iphone16_products" ga tuzatildi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish7"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga16")
        ]
    ]
)

iwatch_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⌚️ Apple Watch Ultra", callback_data="watch"),
            InlineKeyboardButton(text="⌚️ Apple Watch SE", callback_data="watch_se")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga17")
        ]
    ]
)

iwatch_products = InlineKeyboardMarkup(  # "iwatch_produts" ni "iwatch_products" ga tuzatildi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish8"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga18")
        ]
    ]
)

iPad_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📲 iPad Pro", callback_data="pro"),
            InlineKeyboardButton(text="📲 iPad Air", callback_data="air")
        ],
        [
            InlineKeyboardButton(text="🔚 Ortga", callback_data="ortga19")
        ]
    ]
)

ipad_products = InlineKeyboardMarkup(  # "ipad_produts" ni "ipad_products" ga tuzatildi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="sotib_olish9"),
            InlineKeyboardButton(text="🔚 Bekor qilish", callback_data="ortga20")
        ]
    ]
)






























