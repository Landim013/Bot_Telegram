import telebot
import requests

chaveApi = "5979637243:AAF0f3wwtyA_rMAEoyLac7RexLTkAZuCzkk"

bot = telebot.TeleBot(chaveApi)

@bot.message_handler(commands=["opcao1"])
def opc1(mensagem):
    img = open('./batman.png','rb')
    bot.send_photo(mensagem.chat.id, photo=img)
    bot.send_message(mensagem.chat.id,'Eu sou o batma!')

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    img = open('imgs/capamerica.png','rb')
    bot.send_photo(mensagem.chat.id, photo=img)
    bot.send_message(mensagem.chat.id,'Vingadores, avante!')


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    img = open('imgs/chapolim.png','rb')
    bot.send_photo(mensagem.chat.id, photo=img)
    bot.send_message(mensagem.chat.id,'Não contavam com minha astucia!')




def verificar (mensagem):
    return True
     
@bot.message_handler(func=verificar) #defina quado a funçao sera iniciado (quando mensagem for True)
def resposta(mensagem):
    texto = """
Qual é o heroi mais forte? (Clique na opção):

/opcao1 Batman

/opcao2 Capitão america

/opcao3 Chapolim Colorado 
"""
    nome = (mensagem.chat.first_name)
    t = f"Bem vindo {nome}"
    
    bot.send_message(mensagem.chat.id, t)
    bot.send_message(mensagem.chat.id, texto)
    
    print(mensagem)
bot.polling()



