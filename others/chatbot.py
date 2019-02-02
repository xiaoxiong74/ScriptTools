# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: chatbot.py
@Software: PyCharm
@time: 2018/12/26 19:24
@desc:
'''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("myBot")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# 使用英文语料库训练它
chatbot.train("chatterbot.corpus.chinese")

# 开始对话
while True:
    print(chatbot.get_response(input(">")))


