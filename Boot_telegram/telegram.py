import requests

def send_message(token, chat_id, message):
    data = {"chat_id": chat_id, "text": message}
    url = "https://api.telegram.org/bot{}/sendMessage".format(token)
    requests.post(url,data)
    print('foi')


token ='5874652496:AAGvNK6WlmsQ2ClnvX_DunfP7abPqfQx4eo'
chat_id ='-871803933'


msg = "ola mundo"
send_message(token,chat_id,msg)