import pickle
import json
import tflearn
import tensorflow as tf
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import random
from pymongo import MongoClient

empt = ""

context = {}
#client = MongoClient("mongodb://admin:pass@bossdb-shard-00-00-w54dc.mongodb.net:27017,bossdb-shard-00-01-w54dc.mongodb.net:27017,bossdb-shard-00-02-w54dc.mongodb.net:27017/test?ssl=true&replicaSet=BOSSDB-shard-0&authSource=admin&retryWrites=true")
client = MongoClient("mongodb://localhost:27017")

db = client.database

stemmer = LancasterStemmer()
data = pickle.load(open('data/trainingData', 'rb'))
words = data['words']
classes = data['classes']
trainX = data['trainX']
trainY = data['trainY']
with open(r'context.json', 'r') as jsonData:
    contexts = json.load(jsonData)

net = tflearn.input_data(shape=[None, len(trainX[0])])
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, len(trainY[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.load('data/model/model.tflearn')
MIN_ACC = 0.30


def tokenizeAndStem(sentence):
    sentenceWords = nltk.word_tokenize(sentence)
    sentenceWords = [stemmer.stem(word.lower()) for word in sentenceWords]
    return sentenceWords


def makeInputArray(sentence, words, showDetails=False):
    sentenceWords = tokenizeAndStem(sentence)
    bag = [0]*len(words)
    for s in sentenceWords:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if showDetails:
                    print("found in bag: %s" % w)
    return(np.array(bag))


def classify(sentence):
    results = model.predict([makeInputArray(sentence, words)])
    # print(results)
    results = results[0]
    # print(results)
    results = [[i, r] for i, r in enumerate(results) if r > MIN_ACC]
    results.sort(key=lambda x: x[1], reverse=True)
    returnList = []
    for r in results:
        returnList.append((classes[r[0]], r[1]))
    return returnList


def database(sentence,respon,chatid):
	print("chatid : ",chatid)
	db.database.insert_one(
        	{
        	"sentence": sentence,
        	"response": respon,
        	})

def databas(sentence,respon):
    db.database.insert_one(
        {
        "sentence": sentence,
        "response": respon,
        })
def databa(sentence):
    db.testdatabase.insert_one(
        {
        "sentence": sentence,
        "response": empt,
        })


def response(sentence, chatID=0):
    results = classify(sentence)
    print("results : ",results)
    if results:
        while results:
            for i in contexts['contexts']:
                if i['tag'] == results[0][0]:
                    if 'contextSet' in i:
                        context[chatID] = i['contextSet']

                    if not 'contextFilter' in i or (chatID in context and 'contextFilter' in i and i['contextFilter'] == context[chatID]) or "contextCheck" in i:
                        respon = random.choice(i['responses'])
                        database(sentence,respon,chatID)
                        return respon
                    databa(sentence)
                    return empt
    else:
        databa(sentence)
        return empt
