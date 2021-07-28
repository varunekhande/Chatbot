from chatterbot import ChatBot
bot = ChatBot("My Bot")

#setting the storage adapter
storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
database_uri = 'sqlite:///database.sqlite3'

#specifying logic adapters  a logic adapter is a class that takes an input statement and returns a response to that statement.
logic_adapters = [
    'chatterbot.logic.MathematicalEvaluation',  
             #The MathematicalEvaluation adapter solves math problems that use basic operations.
]

#training the bot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train = ([
    "Hello",
    "Hi there",
    "how are you",
    "I am doing good",
    "who are you?",
    "i am chatbot created by varun",
    "where do you live?",
    "I live in artificial world",
    
])

#getting response from bot
respone = bot.get_response("how are you")
print(respone)