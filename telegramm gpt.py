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

@bot.message_handler(content_types=['text'])
def handler_text(message):
    response=Send(message.text)
    send_message_to_user(message.chat.id, response['choices'][0].message.content)
    


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
# response['choices'][0].message.content

bot.polling(non_stop=True)

