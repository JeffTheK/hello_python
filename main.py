#######################################################
#  ___  __  ____  _  _  ____  __  ___  _  _  ____     #
# / __)/  \(  _ \( \/ )(  _ \(  )/ __)/ )( \(_  _)    #
#( (__(  O )) __/ )  /  )   / )(( (_ \) __ (  )(      #
# \___)\__/(__)  (__/  (__\_)(__)\___/\_)(_/ (__)     #
#   __  ____  ____  ____    ____  _  _  ____    __ _  #
# _(  )(  __)(  __)(  __)  (_  _)/ )( \(  __)  (  / ) #
#/ \) \ ) _)  ) _)  ) _)     )(  ) __ ( ) _)    )  (  #
#\____/(____)(__)  (__)     (__) \_)(_/(____)  (__\_) #
#######################################################
#This script is copyrighted. Paste this template in the script and don't cut it
from chatterbot  import ChatBot    #this imports chatbot.It is a library that helps making talking bots!
from chatterbot.trainers import ListTrainer  # method to train the chatbot 

bot = ChatBot('Hello Python')# It is the name of bot we set.
bot.set_trainer(ListTrainer)       #set the trainer to respond

conversation = open('chats.txt','r').readlines() #The file through which bot uses basic commands.

bot.train(conversation)             # train the bot to how to talk

while True:
    message = input('You:')
    if message.strip()!= 'Bye':
     reply = bot.get_response(message)
    print('Hello Python:',reply)
    if message.strip()=='Bye':
        print('Hello Python:Bye Jeff,Have nice day from Hello Python')
        break
#Copyrights don't belong to AristodamusAdairs        
