import os
import json
import time
import telebot
from telebot import types

TOKEN = "BU_YERGA_TOKENINGIZNI_QOYING"
WEB_APP_URL = "BU_YERGA_GITHUB_HAVOLANGIZNI_QOYING"

bot = telebot.TeleBot(TOKEN)

def darajani_aniqla(ball):
    if ball >= 70: return "A+"
    elif ball >= 65: return "A"
    elif ball >= 60: return "B+"
    elif ball >= 55: return "B"
    elif ball >= 50: return "C+"
    elif ball >= 46: return "C"
    else: return "Sertifikat berilmadi"

def ball_hisobla(theta, min_theta=-3.0, max_theta=3.0):
    if theta < min_theta: theta = min_theta
    if theta > max_theta: theta = max_theta
    ball = ((theta - min_theta) / (max_theta - min_theta)) * 100
    return round(ball, 1)

@bot.message_handler(commands=['start', 'test'])
def start_test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_btn = types.WebAppInfo(WEB_APP_URL)
    markup.add(types.KeyboardButton(text="📝 Milliy sertifikat testini boshlash", web_app=web_btn))
    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! Testni boshlash uchun pastdagi tugmani bosing:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def web_app_natija(message):
    data = json.loads(message.web_app_data.data)
    theta = data["theta"]
    savol_soni = data["savol_soni"]

    yakuniy_ball = ball_hisobla(theta)
    daraja = darajani_aniqla(yakuniy_ball)

    natija_matni = (
        f"✅ <b>Test yakunlandi!</b>\n\n"
        f"📊 Siz jami <b>{savol_soni}</b> ta savol yechdingiz\n"
        f"🎯 To'plagan ball: <b>{yakuniy_ball}</b> ball (100 lik tizimda)\n"
        f"🏆 Sertifikat darajasi: <b>{daraja}</b>"
    )
    bot.send_message(message.chat.id, natija_matni, parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())

    if name == "main":
    print("Bot muvaffaqiyatli ishga tushdi...")
    while True:
        try:
            bot.infinity_polling(timeout=20, long_polling_timeout=20)
        except Exception as e:
            print(f"Tarmoqda xatolik: {e}. 5 soniyadan so'ng qayta ulaniladi...")
            time.sleep(5)