# chatbot

Chatbot是对话式交会的产品形态。 我们身边的Chatbot 闲聊型 任务型 问答型 今天我们就来了解下闲聊型机器人

近年来，人机对话系统受到了学术界和产业界的广泛关注并取得了不错的发展。开放域对话系统旨在建立一个开放域的多轮对话系统，使得机器可以流畅自然地与人进行语言交互，既可以进行日常问候类的闲聊，又可以完成特定功能，以使得开放域对话系统具有实际应用价值。具体的说，开放域对话可以继续拆分为支持不同功能的对话形式，例如对话式推荐，知识对话技术等，如何解决并有效融合以上多个技能面临诸多挑战。

机器人能实现闲聊的根本是自然语言处理

自然语言处理( Natural Language Processing, NLP)是计算机科学领域与人工智能领域中的一个重要方向。它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。自然语言处理是一门融语言学、计算机科学、数学于一体的科学。因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，所以它与语言学的研究有着密切的联系，但又有重要的区别。自然语言处理并不是一般地研究自然语言，而在于研制能有效地实现自然语言通信的计算机系统，特别是其中的软件系统。因而它是计算机科学的一部分

自然语言处理主要应用于机器翻译、舆情监测、自动摘要、观点提取、文本分类、问题回答、文本语义对比、语音识别、中文OCR等方面

Transformer 模型

Transformer 模型在2017 年，由Google 团队中首次提出。Transformer 是一种基于注意力机制来加速深度学习算法的模型，模型由一组编码器和一组解码器组成，编码器负责处理任意长度的输入并生成其表达，解码器负责把新表达转换为目的词。Transformer 模型利用注意力机制获取所有其他单词之间的关系，生成每个单词的新表示。Transformer 的优点是注意力机制能够在不考虑单词位置的情况下，直接捕捉句子中所有单词之间的关系。模型抛弃之前传统的encoder-decoder 模型必须结合RNN 或者CNN(Convolutional Neural Networks, CNN)的固有模式，使用全Attention 的结构代替了LSTM，减少计算量和提高并行效率的同时不损害最终的实验结果。但是此模型也存在缺陷。首先此模型计算量太大，其次还存在位置信息利用不明显的问题，无法捕获长距离的信息。

plato-mini UnifiedTransformer以Transformer 编码器为网络基本组件，采用灵活的注意力机制，十分适合文本生成任务，并在模型输入中加入了标识不同对话技能的special token，使得模型能同时支持闲聊对话、推荐对话和知识对话。

plato-mini包含6层的transformer结构，头数为12，隐藏层参数为768，参数量为89M。该模型在十亿级别的中文对话数据上进行预训练，通过PaddleHub加载后可直接用于对话任务。

# 交互模式
import paddlehub as hub

model = hub.Module(name='plato-mini')
with model.interactive_mode(max_turn=3):
    while True:
        human_utterance = input("[Human]: ").strip()
        robot_utterance = model.predict(human_utterance)[0]
        print("[Bot]: %s"%robot_utterance)
