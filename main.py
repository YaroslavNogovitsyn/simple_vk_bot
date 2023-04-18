import os
import random
from dotenv import load_dotenv

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(path):
    load_dotenv(path)
    TOKEN = os.environ.get("TOKEN")
else:
    raise FileNotFoundError

vk = vk_api.VkApi(token=TOKEN)

long_poll = VkLongPoll(vk)


def send_message(chat_id, text):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send', {"chat_id": chat_id, 'message': text, 'random_id': random_id})


for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text
                chat_id = event.chat_id
                send_message(chat_id, msg)
