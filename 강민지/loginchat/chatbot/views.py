from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import os
import json
import nltk
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
from .models import MessagesWithChatBot
from tensorflow.python.framework import ops
import random
import tflearn
# nltk.download()

stemmer = LancasterStemmer()

def getDataSet():
    words = []
    labels = []
    docs_x = []
    docs_y = []
    training = []
    output = []
    with open(os.path.join('static','json/intents.json'), encoding='UTF8') as file:
        data = json.load(file)
    
    for intent in data['intents']:
        for pattern in intent['patterns']:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent['tag'])
        
        if intent['tag'] not in labels:
            labels.append(intent['tag'])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w.lower()) for w in doc]
        
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
                
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        
        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)
    
    return words, labels, training, output, data

def bag_of_words(s, word):
    bag = [0 for _ in range(len(word))]
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(w.lower()) for w in s_words]
    for se in s_words:
        for i, w in enumerate(word):
            if w == se:
                bag[i] = 1

    return np.array(bag)

def printAnswer(chat_txt):
    isTraining = False
    ops.reset_default_graph()
    
    words, labels, training, output, data = getDataSet()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    if isTraining:
        model.fit(training, output, n_epoch=1500, batch_size=8, show_metric=True)
        model.save('static/train.h5')
        isTraining = False
    model.load('static/train.h5')

    results = model.predict([bag_of_words(chat_txt, words)])
    results_index = np.argmax(results)
    tag = labels[results_index]
    
    for tg in data['intents']:
        if tg['tag'] == tag:
            responses = tg['responses']
            
    return random.choice(responses)

def sendUserChat(request, question):
    MessagesWithChatBot(speaker='user', chat_text=question).save()
    return HttpResponseRedirect(reverse('login:chatbot:chathome'))

def sendBotChat(request, question):
    answer = printAnswer(question)
    MessagesWithChatBot(speaker='chatbot', chat_text=answer).save()
    

def sendChatBody(request):
    if request.method == 'POST' and request.POST['userTxt'] != '':
        question = request.POST['userTxt']
        sendUserChat(request, question)
        sendBotChat(request, question)
    return HttpResponseRedirect(reverse('login:chatbot:chathome'))
    
def chatbotView(request):
    messages = MessagesWithChatBot.objects.all()
    messages = {"messages":messages}
    return render(request, 'chatbot/chatbot.html', messages)