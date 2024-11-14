import telebot
from telebot import types
from telebot.types import ForceReply
from time import sleep
from re import findall
from dotenv import load_dotenv
import os
import json
#====================================== 
load_dotenv()

api_token = os.getenv("API_TOKEN")  
TOKEN = api_token # Telegram token
bot = telebot.TeleBot(TOKEN, parse_mode=None) 

admins_id_list = os.getenv("ADMIN_IDS").split(",")
#======================================
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

f = open("texts/about_bot.txt", "rb")
about_bot_text = f.read()
f.close()
#======================================
# Load the JSON file
with open("directory_links.json", "r") as file:
    data = json.load(file)
# Root directory links
calendar_url = data["root"]["calendar.jpg"]
course_chart_url = data["root"]["course_chart.pdf"]
faculty_map_url = data["root"]["faculty_map.pdf"]
introduction_video_url = data["root"]["introduction_video.mp4"]
university_map_url = data["root"]["university_map.jpg"]
# Portal directory links
# Educational
class_schedule_url = data["portal"]["educational"]["class_schedule.mp4"]
educational_requests_url = data["portal"]["educational"]["educational_requests.mp4"]
exam_schedule_url = data["portal"]["educational"]["exam_schedule.mp4"]
teacher_evaluation_url = data["portal"]["educational"]["teacher_evaluation.mp4"]
# Financial Support
online_payment_url = data["portal"]["financial_support"]["online_payment.mp4"]
portal_password_url = data["portal"]["financial_support"]["portal_password.mp4"]
# Research
book_loan_url = data["portal"]["research"]["book_loan.mp4"]
# Student Affairs
meal_reservation_url = data["portal"]["student_affairs"]["meal_reservation.mp4"]
sports_services_url = data["portal"]["student_affairs"]["sports_services.mp4"]
#======================================
markup_00 = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtna_00 = types.KeyboardButton('IEEE')
itembtnb_00 = types.KeyboardButton('رویدادها 🗓️')
itembtnc_00 = types.KeyboardButton('عضویت در IEEE 📝')
itembtnd_00 = types.KeyboardButton('دانشجو راهنما 📚')
itembtne_00 = types.KeyboardButton('ارتباط با اعضا 📞')
itembtnf_00 = types.KeyboardButton('انتقادات و پیشنهادات 💬')
itembtng_00 = types.KeyboardButton('درباره بات 🤖')
markup_00.row(itembtna_00)
markup_00.row(itembtnb_00, itembtnc_00)
markup_00.row(itembtnd_00, itembtne_00)
markup_00.row(itembtnf_00)
markup_00.row(itembtng_00)

markup_02 = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtna_02 = types.KeyboardButton('رویداد های برگزار شده 📅')
itembtnb_02 = types.KeyboardButton('رویداد های جاری 🔄')
itembtnc_02 = types.KeyboardButton('بازگشت 🔙')
markup_02.row(itembtnb_02, itembtna_02)
markup_02.row(itembtnc_02)

markup_04 = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtna_04 = types.KeyboardButton("آموزش پرتال 📖")
itembtnb_04 = types.KeyboardButton("چارت درسی 🗂️")
itembtnc_04 = types.KeyboardButton("آخرین تقویم آموزشی 📆")
itembtnd_04 = types.KeyboardButton("نقشه دانشگاه 🏫")
itembtne_04 = types.KeyboardButton("نقشه دانشکده 🧭")
itembtnf_04 = types.KeyboardButton("کانال های مهم دانشگاه 🔗")
itembtng_04 = types.KeyboardButton('بازگشت 🔙')
markup_04.row(itembtna_04)
markup_04.row(itembtnb_04, itembtnc_04)
markup_04.row(itembtnd_04, itembtne_04)
markup_04.row(itembtnf_04)
markup_04.row(itembtng_04)

markup_05 = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtna_05 = types.KeyboardButton("آموزشی 📚")
itembtnb_05 = types.KeyboardButton("پژوهشی 🔬")
itembtnc_05 = types.KeyboardButton("دانشجویی 🧑‍🎓")
itembtnd_05 = types.KeyboardButton("مالی و پشتیبانی 💵")
itembtne_05 = types.KeyboardButton("سایر موارد 🌐")
itembtnf_05 = types.KeyboardButton("↩️")
markup_05.row(itembtna_05, itembtnb_05)
markup_05.row(itembtnc_05, itembtnd_05)
markup_05.row(itembtne_05)
markup_05.row(itembtnf_05)

markup_06 = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtna_06 = types.KeyboardButton("Cancel")
markup_06.row(itembtna_06)
#======================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, start_text, reply_markup=markup_00)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "بازگشت 🔙":
		bot.reply_to(message, "🏠", reply_markup=markup_00)

	if message.text == "IEEE":
		bot.send_video(chat_id=message.chat.id, video=introduction_video_url, caption=ieee_text)
		
	if message.text == "رویدادها 🗓️":
		bot.reply_to(message, event_text, reply_markup=markup_02)
	
	if message.text == "عضویت در IEEE 📝":
		bot.reply_to(message, forsat_haye_hamkari_text)

	if message.text == "دانشجو راهنما 📚" or message.text == "↩️":
		bot.reply_to(message, daneshjoo_rahnama_text, reply_markup=markup_04)

	if message.text == "ارتباط با اعضا 📞":
		bot.reply_to(message, ertebat_ba_aza_text)
	
	if message.text == "رویداد های برگزار شده 📅":
		bot.reply_to(message, "under construction")

	if message.text == "رویداد های جاری 🔄":
		bot.reply_to(message, "under construction")

	if message.text == "آموزش پرتال 📖":
		bot.reply_to(message, "choose one the options", reply_markup=markup_05)

	if message.text == "چارت درسی 🗂️":
		bot.send_document(chat_id=message.chat.id, document=course_chart_url)

	if message.text == "آخرین تقویم آموزشی 📆":
		bot.send_photo(chat_id=message.chat.id, photo=calendar_url)

	if message.text == "نقشه دانشگاه 🏫":
		bot.send_photo(chat_id=message.chat.id, photo=university_map_url)

	if message.text == "نقشه دانشکده 🧭":
		bot.send_document(chat_id=message.chat.id, document=faculty_map_url)

	if message.text == "کانال های مهم دانشگاه 🔗":
		bot.reply_to(message, kanal_haye_mohem_text)

	if message.text == "آموزشی 📚":
		bot.send_video(chat_id=message.chat.id, video=class_schedule_url, caption="Educational 1")
		bot.send_video(chat_id=message.chat.id, video=exam_schedule_url, caption="Educational 2")
		bot.send_video(chat_id=message.chat.id, video=teacher_evaluation_url, caption="Educational 3")
		#bot.send_document(chat_id=message.chat.id, document=educational_requests_url, caption="Educational 4")
		#print(educational_requests_url)

	if message.text == "پژوهشی 🔬":
		bot.send_video(chat_id=message.chat.id, video=book_loan_url, caption="Research")

	if message.text == "دانشجویی 🧑‍🎓":
		bot.send_video(chat_id=message.chat.id, video=meal_reservation_url, caption="Student Affairs 1")
		bot.send_video(chat_id=message.chat.id, video=sports_services_url, caption="Student Affairs 2")

	if message.text == "مالی و پشتیبانی 💵":
		bot.send_video(chat_id=message.chat.id, video=online_payment_url, caption="Financial & Support 1")
		bot.send_video(chat_id=message.chat.id, video=portal_password_url, caption="Financial & Support 2")

	if message.text == "سایر موارد 🌐":
		bot.reply_to(message, "under construction")
		
	if message.text == "انتقادات و پیشنهادات 💬":
		bot.reply_to(message, suggestion_01, reply_markup=markup_06)
		bot.register_next_step_handler(message, suggestion)

	if message.text == 'درباره بات 🤖':
		bot.reply_to(message, about_bot_text)

def suggestion(message):
	suggestion_text = message.text
	if suggestion_text == "Cancel":
		bot.reply_to(message, "Canceled", reply_markup=markup_00)
		return
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