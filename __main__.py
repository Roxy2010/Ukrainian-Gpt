import openai
import telebot

bot=telebot.TeleBot('6167495629:AAGzGE1--4acZwUwIOIzvU1hjJEGX9xkyC8')

API_KEY = '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'
model_id = 'gpt-3.5-turbo'

def init_openAI_API_Key():
    openai.api_key = API_KEY


@bot.message_handler(commands=['start'])
def start(message):
    send_message_to_user(message.chat.id, "Вас вітає Ukrainian GPT!Ви можете запитати в мене будь що чи просто поспілкуватися зі мною")
    print("До бота підключився користувач:", message.from_user.full_name )                

@bot.message_handler(content_types=['text'])
def handler_text(message):
    print( message.from_user.full_name, "написав(ла) повідомлення:", message.text )
    response=Send(message.text)
    send_message_to_user(message.chat.id, response['choices'][0].message.content)
    
@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def handler_unsupported_types(message):
    send_message_to_user(message.chat.id, "Прибачте, ми не підтримуємо такий тип повідомлень")

def send_message_to_user(id, text):
    bot.send_message(id, text)


def Send(message):
    myMessage = [] 
    myMessage.append({'role': 'system', 'content': message})
    response = openai.ChatCompletion.create(
        model =model_id,
        messages=myMessage
    )
    return response

init_openAI_API_Key()
print("chat bot is start")
print(API_KEY)

bot.polling(non_stop=True)

