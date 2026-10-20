import telebot
from flask import Flask
from threading import Thread
import math
from telebot import types

TOKEN = '8803170589:AAEKy5Exs1XW9hVdnyh6ksgDhH2RGRy2nL4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("👨‍💻 المطور: ابو القدايس", url="https://t.me/RHKKK313HR"))
    bot.send_message(msg.chat.id, "أهلا بيك حبيبي في بوت ابو القدايس 🧮🔥\n\nدزلي اي مسألة رياضية وانا احلها الك فورا!\nمثال: 2+2*5 او sqrt(16)", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def solve(msg):
    try:
        text = msg.text.replace('^','**').replace('√','math.sqrt')
        # السماح بدوال math
        result = eval(text, {"__builtins__": None, "math": math, "sqrt": math.sqrt})
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("👨‍💻 المطور: ابو القدايس", url="https://t.me/RHKKK313HR"))
        bot.send_message(msg.chat.id, f"📝 مسألتك: {msg.text}\n✅ الناتج: {result}", reply_markup=markup)
    except Exception as e:
        bot.send_message(msg.chat.id, "❌ صيغة غلط حبيبي، دزها مثل: 2+2*3")

app = Flask('')
@app.route('/')
def home(): return "Bot of Abu Al-Qudais is Alive!"

def run(): app.run(host='0.0.0.0', port=8080)
Thread(target=run).start()

print("Bot Started...")
bot.infinity_polling()
