# -*- coding: UTF-8 -*-

import os
import asyncio
import random
from ppgan.apps import Photo2CartoonPredictor#人像动漫化
from PIL import Image
import paddlehub as hub


from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)




os.environ['WECHATY_PUPPET'] = "wechaty-puppet-service"
os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = "c2fc312912f6449cada8ddd8562c70ef"
os.environ['WECHATY_PUPPET_SERVICE_ENDPOINT'] = "47.100.50.78:8080"
os.environ['CUDA_VISIBLE_DEVICES']='0'

model = hub.Module(name='plato-mini')


# module = hub.Module(name="deeplabv3p_xception65_humanseg")

async def on_message(msg: Message):
    talker = msg.talker()
    if not msg.is_self():
        if msg.text() == 'ding':
            await talker.say('这是自动回复: dong dong dong')

        if msg.text() == '聊天':
            await talker.say('好呀我最喜欢聊天了')

        with model.interactive_mode(max_turn=5):

            human_utterance =msg.text().strip()
            robot_utterance = model.predict(human_utterance)[0]
            await talker.say(robot_utterance)


async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    print('Status: ' + str(status))
    print('View QR Code Online: https://wechaty.js.org/qrcode/' + qrcode)


async def on_login(user: Contact):
    print(user)


async def main():
    # 确保我们在环境变量中设置了WECHATY_PUPPET_SERVICE_TOKEN
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        print('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    bot.on('scan', on_scan)
    bot.on('login', on_login)
    bot.on('message', on_message)

    await bot.start()

    print('[Python Wechaty] Ding Dong Bot started.')


asyncio.run(main())
