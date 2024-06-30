import telebot
from telebot import types
from telebot.types import ForceReply
from time import sleep
from re import findall
#====================================== 
TOKEN = "000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" # Telegram token
bot = telebot.TeleBot(TOKEN, parse_mode=None) 
#======================================
f = open("texts/admins_id.txt", "r")
admins_id_text = f.read()
admins_id_list = findall(r'\d+', admins_id_text)
f.close()

f = open("texts/suggestion_01.txt", "rb")
suggestion_01 = f.read()
f.close()

f = open("texts/suggestion_02.txt", "rb")
suggestion_02 = f.read()
f.close()

f = open("texts/start.txt", "rb")
start_text = f.read()
f.close()

f = open("texts/daneshjoo_rahnama.txt", "rb")
daneshjoo_rahnama_text = f.read()
f.close()

f = open("texts/ieee.txt", "rb")
ieee_text = f.read()
f.close()

f = open("texts/event.txt", "rb")
event_text = f.read()
f.close()

f = open("texts/ertebat_ba_aza.txt", "rb")
ertebat_ba_aza_text = f.read()
f.close()

f = open("texts/forsat_haye_hamkari.txt", "rb")
forsat_haye_hamkari_text = f.read()
f.close()

f = open("texts/kanal_haye_mohem.txt", "rb")
kanal_haye_mohem_text = f.read()
f.close()
#======================================
tizer_url = "https://link-to-file/ieee-bot/tizer.mp4"
chart_url = "https://link-to-file/ieee-bot/chart.pdf"
taghvim_url = "https://link-to-file/ieee-bot/taghvim.pdf"
uni_map_url = "https://link-to-file/ieee-bot/uni-map.jpg"
engineering_map_url = "https://link-to-file/ieee-bot/engineering-map.jpg"
#======================================
markup_00 = types.ReplyKeyboardMarkup()
itembtna_00 = types.KeyboardButton('IEEE')
itembtnb_00 = types.KeyboardButton('رویدادها')
itembtnc_00 = types.KeyboardButton('فرصت‌های همکاری')
itembtnd_00 = types.KeyboardButton('دانشجو راهنما')
itembtne_00 = types.KeyboardButton('ارتباط با اعضا')
itembtnf_00 = types.KeyboardButton('انتقادات و پیشنهادات')
markup_00.row(itembtna_00)
markup_00.row(itembtnb_00,itembtnc_00)
markup_00.row(itembtnd_00,itembtne_00)
markup_00.row(itembtnf_00)

markup_02 = types.ReplyKeyboardMarkup()
itembtna_02 = types.KeyboardButton('رویداد های برگزار شده')
itembtnb_02 = types.KeyboardButton('رویداد های جاری')
itembtnc_02 = types.KeyboardButton('بازگشت')
markup_02.row(itembtnb_02, itembtna_02)
markup_02.row(itembtnc_02)

markup_04 = types.ReplyKeyboardMarkup()
itembtna_04 = types.KeyboardButton("آموزش پرتال")
itembtnb_04 = types.KeyboardButton("چارت درسی")
itembtnc_04 = types.KeyboardButton("آخرین تقویم آموزشی")
itembtnd_04 = types.KeyboardButton("نقشه دانشگاه")
itembtne_04 = types.KeyboardButton("نقشه دانشکده")
itembtnf_04 = types.KeyboardButton("کانال های مهم دانشگاه")
itembtng_04 = types.KeyboardButton('بازگشت')
markup_04.row(itembtna_04)
markup_04.row(itembtnb_04,itembtnc_04)
markup_04.row(itembtnd_04,itembtne_04)
markup_04.row(itembtnf_04)
markup_04.row(itembtng_04)

markup_05 = types.ReplyKeyboardMarkup()
itembtna_05 = types.KeyboardButton("آموزشی")
itembtnb_05 = types.KeyboardButton("پژوهشی")
itembtnc_05 = types.KeyboardButton("دانشجویی")
itembtnd_05 = types.KeyboardButton("مالی و پشتیبانی")
itembtne_05 = types.KeyboardButton("سایر موارد")
itembtnf_05 = types.KeyboardButton("↩️")
markup_05.row(itembtna_05, itembtnb_05)
markup_05.row(itembtnc_05, itembtnd_05)
markup_05.row(itembtne_05)
markup_05.row(itembtnf_05)
#======================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, start_text, reply_markup=markup_00)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "بازگشت":
		bot.reply_to(message, "🏠", reply_markup=markup_00)

	if message.text == "IEEE":
		bot.send_video(chat_id=message.chat.id, video=tizer_url, caption=ieee_text)
		
	if message.text == "رویدادها":
		bot.reply_to(message, event_text, reply_markup=markup_02)
	
	if message.text == "فرصت‌های همکاری":
		bot.reply_to(message, forsat_haye_hamkari_text)

	if message.text == "دانشجو راهنما" or message.text == "↩️":
		bot.reply_to(message, daneshjoo_rahnama_text, reply_markup=markup_04)

	if message.text == "ارتباط با اعضا":
		bot.reply_to(message, ertebat_ba_aza_text)
	
	if message.text == "رویداد های برگزار شده":
		bot.reply_to(message, "under construction")

	if message.text == "رویداد های جاری":
		bot.reply_to(message, "under construction")

	if message.text == "آموزش پرتال":
		bot.reply_to(message, "choose one the options", reply_markup=markup_05)

	if message.text == "چارت درسی":
		bot.send_document(chat_id=message.chat.id, document=chart_url)

	if message.text == "آخرین تقویم آموزشی":
		bot.send_document(chat_id=message.chat.id, document=taghvim_url)

	if message.text == "نقشه دانشگاه":
		bot.send_photo(chat_id=message.chat.id, photo=uni_map_url)

	if message.text == "نقشه دانشکده":
		bot.send_photo(chat_id=message.chat.id, photo=engineering_map_url)

	if message.text == "کانال های مهم دانشگاه":
		bot.reply_to(message, kanal_haye_mohem_text)

	if message.text == "آموزشی":
		bot.reply_to(message, "under construction")

	if message.text == "پژوهشی":
		bot.reply_to(message, "under construction")

	if message.text == "دانشجویی":
		bot.reply_to(message, "under construction")

	if message.text == "مالی و پشتیبانی":
		bot.reply_to(message, "under construction")

	if message.text == "سایر موارد":
		bot.reply_to(message, "under construction")
		
	if message.text == "انتقادات و پیشنهادات":
		bot.reply_to(message, suggestion_01, reply_markup=ForceReply())
		bot.register_next_step_handler(message, suggestion)

def suggestion(message):
	suggestion_text = message.text
	try: 
		for id in admins_id_list:
			bot.send_message(id, "NEW SUGGESTION:\n\n"+suggestion_text)
	except:
		pass
	bot.reply_to(message, suggestion_02, reply_markup=markup_00)
#======================================
if __name__ == "__main__":
	while True:
		try:
			bot.infinity_polling()
		except:
			sleep(5)