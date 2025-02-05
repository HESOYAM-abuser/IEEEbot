import telebot
from telebot import types
from dotenv import load_dotenv
import os
from helpers import statics 
from time import sleep

load_dotenv()

api_token = os.getenv("API_TOKEN")
admins_id_list = os.getenv("ADMIN_IDS").split(",")

bot = telebot.TeleBot(api_token, parse_mode=None)

def create_keyboard(button_list):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for row in button_list:
        markup.row(*[types.KeyboardButton(button) for button in row])
    return markup

main_menu = create_keyboard(statics.buttons["main_menu"])
events_menu = create_keyboard(statics.buttons["events_menu"])
guide_menu = create_keyboard(statics.buttons["guide_menu"])
portal_menu = create_keyboard(statics.buttons["portal_menu"])
cancel_menu = create_keyboard(statics.buttons["cancel_menu"])

#================================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, statics.messages["start"], reply_markup=main_menu)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == statics.buttons["cancel_menu"][0][0]:  # "بازگشت 🔙" dynamically from statics
        bot.reply_to(message, statics.messages["start"], reply_markup=main_menu)

    elif message.text == statics.buttons["main_menu"][0][0]:  # "IEEE"
        bot.send_video(chat_id=message.chat.id, video=statics.urls["root"]["introduction_video"])
        bot.send_message(message.chat.id, statics.messages["ieee"])

    elif message.text == statics.buttons["main_menu"][1][0]:  # "رویدادها 🗓️"
        bot.reply_to(message, statics.messages["events"], reply_markup=events_menu)
    
    elif message.text == statics.buttons["main_menu"][1][1]:  # "عضویت در IEEE 📝"
        bot.reply_to(message, statics.messages["join_ieee"])

    elif message.text == statics.buttons["main_menu"][2][0]:  # "دانشجو راهنما 📚"
        bot.reply_to(message, statics.messages["guide_student"], reply_markup=guide_menu)

    elif message.text == statics.buttons["main_menu"][2][1]:  # "ارتباط با اعضا 📞"
        bot.reply_to(message, statics.messages["contact_members"])
    
    elif message.text == statics.buttons["main_menu"][3][0]:  # "انتقادات و پیشنهادات 💬"
        bot.reply_to(message, statics.messages["suggestion"], reply_markup=cancel_menu)
        bot.register_next_step_handler(message, suggestion)

    elif message.text == statics.buttons["main_menu"][4][0]:  # "درباره بات 🤖"
        bot.reply_to(message, statics.messages["about_bot"])

    elif message.text == statics.buttons["events_menu"][0][0]:  # "رویداد های جاری 🔄"
        bot.reply_to(message, statics.messages["current_events"])

    elif message.text == statics.buttons["events_menu"][0][1]:  # "رویداد های برگزار شده 📅"
        bot.reply_to(message, statics.messages["completed_events"])

    elif message.text == statics.buttons["events_menu"][1][0]:  # "بازگشت 🔙"
        bot.reply_to(message, statics.messages["start"], reply_markup=main_menu)

    elif message.text == statics.buttons["guide_menu"][0][0]:  # "آموزش پرتال 📖"
        bot.reply_to(message, statics.messages["choose_portal_option"], reply_markup=portal_menu)

    elif message.text == statics.buttons["guide_menu"][1][0]:  # "چارت درسی 🗂️"
        bot.send_document(chat_id=message.chat.id, document=statics.urls["root"]["course_chart"])

    elif message.text == statics.buttons["guide_menu"][1][1]:  # "آخرین تقویم آموزشی 📆"
        bot.send_photo(chat_id=message.chat.id, photo=statics.urls["root"]["calendar"])

    elif message.text == statics.buttons["guide_menu"][2][0]:  # "نقشه دانشگاه 🏫"
        bot.send_photo(chat_id=message.chat.id, photo=statics.urls["root"]["university_map"])

    elif message.text == statics.buttons["guide_menu"][2][1]:  # "نقشه دانشکده 🧭"
        bot.send_document(chat_id=message.chat.id, document=statics.urls["root"]["faculty_map"])

    elif message.text == statics.buttons["guide_menu"][3][0]:  # "کانال های مهم دانشگاه 🔗"
        bot.reply_to(message, statics.messages["important_channels"])

    elif message.text == statics.buttons["guide_menu"][4][0]:  # "بازگشت 🔙"
        bot.reply_to(message, statics.messages["start"], reply_markup=main_menu)

    elif message.text == statics.buttons["portal_menu"][0][0]:  # "آموزشی 📚"
        bot.send_video(chat_id=message.chat.id, video=statics.urls["portal"]["educational"]["class_schedule"],
                       caption=statics.captions["class_schedule"])
        bot.send_video(chat_id=message.chat.id, video=statics.urls["portal"]["educational"]["exam_schedule"],
                       caption=statics.captions["exam_schedule"])
        bot.send_video(chat_id=message.chat.id, video=statics.urls["portal"]["educational"]["teacher_evaluation"],
                       caption=statics.captions["teacher_evaluation"])

    elif message.text == statics.buttons["portal_menu"][0][1]:  # "پژوهشی 🔬"
        bot.send_video(chat_id=message.chat.id, video=statics.urls["portal"]["research"]["book_loan"],
                       caption=statics.captions["book_loan"])

    elif message.text == statics.buttons["portal_menu"][1][0]:  # "دانشجویی 🧑‍🎓"
        bot.send_video(chat_id=message.chat.id, video=statics.urls["portal"]["student_affairs"]["meal_reservation"],
                       caption=statics.captions["meal_reservation"])
        bot.send_video(chat_id=message.chat.id, video=statics.urls["portal"]["student_affairs"]["sports_services"],
                       caption=statics.captions["sports_services"])

    elif message.text == statics.buttons["portal_menu"][1][1]:  # "مالی و پشتیبانی 💵"
        bot.send_video(chat_id=message.chat.id, video=statics.urls["portal"]["financial_support"]["online_payment"],
                       caption=statics.captions["online_payment"])
        bot.send_video(chat_id=message.chat.id, video=statics.urls["portal"]["financial_support"]["portal_password"],
                       caption=statics.captions["portal_password"])

    elif message.text == statics.buttons["portal_menu"][2][0]:  # "سایر موارد 🌐"
        bot.reply_to(message, statics.messages["other_cases"])

    elif message.text == statics.buttons["portal_menu"][3][0]:  # "↩️"
        bot.reply_to(message, statics.messages["start"], reply_markup=main_menu)
        
def suggestion(message):
	suggestion_text = message.text
	if suggestion_text == statics.buttons["cancel_menu"][0][0]:
		bot.reply_to(message, statics.messages["suggestion_cancelled"], reply_markup=main_menu)
		return
	try: 
		for id in admins_id_list:
			bot.send_message(id, statics.messages["new_suggestion"]+suggestion_text)
	except:
		pass
	bot.reply_to(message, statics.messages["suggestion_received"], reply_markup=main_menu)
#================================================
if __name__ == "__main__":
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(f"Error: {e}")
            sleep(5)
