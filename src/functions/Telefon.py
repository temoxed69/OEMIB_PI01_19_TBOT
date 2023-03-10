import telebot
from telebot import types


bot = telebot.TeleBot('6160529824:AAExGEMcY7Uhfqw14K_9eQ60IzZipQF2vTQ')
@bot.message_handler(commands=['start'])
def start(message):

       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
       item1 = types.KeyboardButton("Доп.функции")
       item2 = types.KeyboardButton("Давай приступим")
       item3 = types.KeyboardButton("Приобрести телефон")
       markup.add(item1, item2, item3)

       bot.send_message(message.chat.id, 'Привет, я - бот, созданный для помощи в выборе  телефона(Айфон не телефон)!',
       parse_mode='html', reply_markup=markup)
       bot.send_message(message.chat.id, 'Процесс выбора будет происходить в виде небольшого опроса.',
       parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
   if (message.text == "Доп.функции"):
           markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           item15 = types.KeyboardButton("Перейти к конкретному шагу")
           item25 = types.KeyboardButton("Привет")
           item250 = types.KeyboardButton("Вернуться в главное меню")
           markup.add(item15, item25, item250)
           bot.send_message(message.chat.id, text="Привет".format(message.from_user),
           reply_markup=markup)
   elif (message.text == "Перейти к конкретному шагу"):
           markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           item1 = types.KeyboardButton("1 шаг")
           item2 = types.KeyboardButton("2 шаг")
           markup.add(item1, item2)

   if (message.text == "Давай приступим"):
           markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           item1 = types.KeyboardButton("Да")
           item2 = types.KeyboardButton("Нет")
           markup.add(item1, item2)
           bot.send_message(message.chat.id,text="Нужен ли вам в телефон с сенсором распознавания лица?".format(message.from_user),
           reply_markup=markup)
   elif (message.text == "Нет"):
           markup = types.InlineKeyboardMarkup()
           item3 = types.InlineKeyboardButton(text='Купить', url='https://market.yandex.ru/product--smartfon-xiaomi-redmi-9c-nfc-4-128-gb-ru-zelenyi/1444624496?glfilter=14871214%3A14898020_101523585832&glfilter=23476910%3A23477050_101523585832&glfilter=24938090%3A1_101523585832&glfilter=25879492%3A26802070_101523585832&clid=1601&utm_source=yandex&utm_medium=search&utm_campaign=ymp_offer_dp_cehac_ultracorfix_bko_dyb_search_rus&utm_term=91491%7C101523585832&utm_content=cid%3A78843385%7Cgid%3A5041631525%7Caid%3A12836044957%7Cph%3A2906307%7Cpt%3Apremium%7Cpn%3A2%7Csrc%3Anone%7Cst%3Asearch%7Crid%3A2906307%7Ccgcid%3A0&sku=101523585832&resale_goods=resale_new&cpa=1')
           markup.add(item3)
           bot.send_message(message.chat.id, "Тогда ваш выбор - это недорогой телефончик Xiaomi Redmi 9c",
           reply_markup = markup)
   elif (message.text == "Да"):
           markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           item4 = types.KeyboardButton("Honor")
           item5 = types.KeyboardButton("Xiaomi")
           markup.add(item4, item5)
           bot.send_message(message.chat.id, "От какого производителя вы бы хотели себе телефон?".format(message.from_user),
           reply_markup=markup)
   elif (message.text == "Xiaomi"):
           markup = types.InlineKeyboardMarkup()
           item6 = types.InlineKeyboardButton(text='Купить', url='https://www.eldorado.ru/cat/detail/smartfon-xiaomi-redmi-10c-4gb-64gb-gray/?yclid=813305687201862805&utm_medium=cpc&utm_source=yandex&utm_campaign=cn:mg_dsa_gallery_p_spb|cid:81827926&utm_term=&utm_content=ph:3286700|re:3286700|cid:81827926|gid:5106730933|aid:13272870911|adp:no|pos:premium2|src:search_none|dvc:desktop|coef_goal:0|region:2|%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3')
           markup.add(item6)
           bot.send_message(message.chat.id, "Тогда ваш выбор - это Xiaomi Redmi 10 c",
           reply_markup = markup)
   elif (message.text == "Honor"):
           markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           item7 = types.KeyboardButton("Для игр")
           item8 = types.KeyboardButton("Для сотовой связи")
           markup.add(item7, item8)
           bot.send_message(message.chat.id, "В каких целях планируете использовать телефон?".format(message.from_user),
           reply_markup=markup)
   elif (message.text == "Для сотовой связи"):
           markup = types.InlineKeyboardMarkup()
           item9 = types.InlineKeyboardButton(text='Купить',
           url='https://market.yandex.ru/product--smartfon-honor-8a/413274473?clid=703&resale_goods=resale_resale&cpa=1&resale_goods_condition=resale_well')
           markup.add(item9)
           bot.send_message(message.chat.id, "Тогда ваш выбор - это  телефон Honor Huawei 8a ",
           reply_markup = markup)
   elif (message.text == "Для игр"):
           markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           item10 = types.KeyboardButton("8")
           item11 = types.KeyboardButton("12")
           markup.add(item10, item11)
           bot.send_message(message.chat.id, "Сколько оперативной памяти в телефоне вам требуется?".format(message.from_user),
           reply_markup=markup)
   elif (message.text == "8"):
           markup = types.InlineKeyboardMarkup()
           item12 = types.InlineKeyboardButton(text='Купить', url='https://market.yandex.ru/product--smartfon-honor-50-8-128gb-midnight-black-nth-nx9/1463060413?glfilter=14871214%3A16333632_101481529765&glfilter=25879492%3A26835570_101481618749&cpa=1&utm_source=yandex&utm_medium=search&utm_campaign=ymp_offer_dp_cehac_ultracorfix_bko_dyb_search_rus&utm_term=91491%7C101481529765&utm_content=cid%3A78843385%7Cgid%3A5041631525%7Caid%3A12836044957%7Cph%3A2906307%7Cpt%3Apremium%7Cpn%3A1%7Csrc%3Anone%7Cst%3Asearch%7Crid%3A2906307%7Ccgcid%3A0&sku=101481618749&resale_goods=resale_new')
           markup.add(item12)
           bot.send_message(message.chat.id, "Тогда ваш выбор - это телефон с хорошей производительностью под названием Honor 50",
           reply_markup = markup)
   elif (message.text == "12"):
           markup = types.InlineKeyboardMarkup()
           item13 = types.InlineKeyboardButton(text='Купить', url='https://www.ozon.ru/product/smartfon-honor-honor-80-pro-12gb-512gb-black-12-512-gb-chernyy-808537818/?advert=5qWU6Y8dfQKjrRnm_VxAG2V9U_yF7UIU2EWkNR2RU8aOzLWCqkXuE_V3203opy-B3OReKGSzmt3qkAwm9IarCOMzFKa_JlvJrpjyVU6WWMjBOwM4nafqmHwYuAQYIYX4hBZrVIM7MTL0hk5Ig39g5YTP3R2hxRSTNr3Z6HXcRGOLyAaV4x008AjE7XsEzYljqJ1FN0LN7rIMmrG7TdzRp00nUp9ZUWNajB4mYPlzkFVZQAZUkmE87ZlNMhv6PgNRDpTu7DKbT8Qa21uOehS9nT4_ZSx-bhbHt0E4gq545PBroXALobmm8_oT2cWb9TXqj0a2rXMkKGdcWK_YREm4EupX9L00oj_d0dvZwdoINBs2q-w8h93jABrJLFvhO1cKP-NL1zZv-iGDuU5KnYu0-gQ_Xyn7_6QDpYdIH8ur72X4zQf5IOvq6JkKTkPss4MxMuOXXXjyGTx0oQVNQf0gHdN24dFV0zx2EFvUhPKklM1nDCxLXcOhZtz_BmTxq1Ct9SjI-uv3GuJC1GgKziZabj3XeIyzJUt5CNrk-yrMX6mgvh-lN5bTkwt5QTM029s0OaTdm8AvZnIcZ8073_u2pu8u0WIZu3oI1kzG1yHMIZan9FAiHe_hZcUZYgtBLc64r2TPWM4pXCGKpSZ-3HynMlL7IoLXil9MhwyDauEfCKLw8-UfHtM1fYSbMHZijQgqLfblk3dcctWLPL1BstpgiF6Ud5YRsm9SSvMjsd3nKn-qDBqzpI8yi-SjruY0jD30OonN1vFTxk1W_00bdD-rLg&avtc=1&avte=2&avts=1677275845&keywords=honor+80+pro+plus&sh=wDM1SQ2jnw')
           markup.add(item13)
           bot.send_message(message.chat.id, "Тогда ваш выбор - это производительный 12-гиговый телефончик Honor 80 pro",
           reply_markup = markup)

bot.polling(none_stop=True)