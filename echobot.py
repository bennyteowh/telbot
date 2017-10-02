
# coding: utf-8

# In[ ]:


import json 
import requests
import time
import urllib

TOKEN = "331146838:AAEOa1sc115fS7SugfxkZ0fl5TKt-8bBoYk"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url): # get the url and encode it to utf8
    response = requests.get(url)
    content = response.content.decode("utf8")
    print(content)#for testing
    return content


def get_json_from_url(url): # get json from URL
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None): #get the 
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates): #gets the id of the latest update
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates): #updates the message to be sent and calls send message
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)
            

def get_last_chat_id_and_text(updates): # receives the last chat id & message
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id): # sends the message with the API method
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    print(url) #for testing
    print(url) #for testing
    get_url(url) # works!
    
def main(): 
    last_update_id = None
    while True:
        print("getting updates")# for testing
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()

