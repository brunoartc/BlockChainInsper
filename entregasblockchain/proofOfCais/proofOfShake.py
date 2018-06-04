#!/usr/bin/env python
import random 
import hashlib
import markovify
import datetime
import nltk
import re
import pickle
import pprint
from comedyOfErrors import shake

maxNonce = 869609989
blocks = []
# genis = {'body': {'scene': 'Trump Cancels Summit Meeting With Kim'}, 'head': {'date': '2018-05-24 19:54:05.832450', 'nonce': 4208796, 'ultimoHash': '', 'digest': '000dc63f421ada932615e8f36d336117'}}
# blocks.append(genis)
# with open('blocos.pickle', "wb") as f:
#     pickle.dump( blocks, open( "blocos.pickle", "wb" ) )
with open('blocos.pickle', "rb") as f:
        blocks = pickle.load(f)

def milkshake():
    scene = []
    
    with open('comOfErr.txt') as f:
        text = f.read()
        # text_modelComedy = markovify.Text(text, state_size=2)
    # with open('trumpsTweets.txt') as f:
    #     text = f.read()
    #     text_modelTrump = markovify.Text(text, state_size=2)

    text_model = markovify.Text(text)
    # model_combo = markovify.combine([ text_modelComedy, text_modelTrump ], [ 4, 1 ])

    class POSifiedText(markovify.Text):
        def word_split(self, sentence):
            words = re.split(self.word_split_pattern, sentence)
            words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
            return words

        def word_join(self, words):
            sentence = " ".join(word.split("::")[0] for word in words)
            return sentence

    for i in range(5):
        scene.append(text_model.make_short_sentence(100)) 
        # scene.append(text_model.make_sentence()) 
        # print scene[i]

    return scene

# def milkshake():
#     scene = []
#     for j in range (4): 
#         line = ''
#         milkCount = random.randint(0, 86240)
#         for i in range (milkCount, milkCount + random.randint(5, 28)):
#             line = line + line.join(shake[i])  
#         scene.append(line)
#     return scene, milkCount

def lerBlocks():
    ultimo = blocks[len(blocks) - 1]
    return ultimo 

def resHash():
    res = 0
    scene = milkshake()
    date = str(datetime.datetime.now())
    while res == 0:
        nonce = random.randint(0, maxNonce)
        random.shuffle(scene)
        audition = str(''.join(scene)) + str(nonce) + date
        hashBlock = hashlib.md5(audition)
        if  hashBlock.hexdigest().startswith('00000') == True:
            res = 1
            nonce = nonce
            digest = hashBlock.hexdigest() 
            return digest, date, scene, nonce

def novoBlock():
    ultimo = lerBlocks()
    digest, date, scene, nonce = resHash()
    novoBlock = {
        'head': {
            'digest': digest,
            'ultimoHash': ultimo['head']['digest'],
            'date': date,
            'nonce': nonce
        },
        'body': {
            'scene': scene
        }
    }
    blocks.append(novoBlock)

def action():
    nBlocks = raw_input('Numero de Blocos: ')
    print datetime.datetime.now()
    for i in range(int(nBlocks)):
        novoBlock()
        print datetime.datetime.now()

    pickle.dump(blocks, open('blocos.pickle', 'wb'))
        
action()

bs = pickle.load(open('blocos.pickle', 'rb'))
print '\n'
for b in bs:
    pprint.pprint (b)  
    print '\n'
