import telebot
API_KEY = "6664322140:AAEThpN0oFOK6GLYnUSwQdWHgxSAWvZCPuk"
bot = telebot.TeleBot(API_KEY, parse_mode=False)
@bot.message_handler(commands=["start"])
def start_message(msg):
    name = msg.from_user.first_name
    id = msg.from_user.id
    username = msg.from_user.username
    bot.reply_to(msg, "   Your Information \n  Id : "+str(id)+" \n Name : "+ name +"\n username = " + username)
    print("1")
print("running...")
bot.polling()
