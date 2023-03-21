import openai
API_KEY = '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'
model_id = 'gpt-3.5-turbo'

def init_openAI_API_Key():
    openai.api_key = API_KEY

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
text= input(" ")
response=Send(text)
print(response['choices'][0].message.content)