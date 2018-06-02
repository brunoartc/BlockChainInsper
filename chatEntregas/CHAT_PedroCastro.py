#  import os
from flask import Flask, request, jsonify
import requests
from Crypto.PublicKey import RSA
import urllib.request

app = Flask(__name__)

key = RSA.generate(2048)
pubKey = key.publickey()

domain = 'pythonanywhere.com/'


#nicolasbs
def getpub(user):
    responseKey = RSA.importKey(req.urlopen('http://' + user + domain +'getpub').read())
    return responseKey

@app.route('/send', methods=['POST', 'GET'])
def enviarMsg():
    if request.method == 'POST':
        dest = request.form['dest']
        msg = request.form['msg']
        responseKey = getpub(dest)
        encrypted = responseKey.encrypt(msg.encode('uft-8'),32)
        # params = {'msg': encrypted, 'sender': 'Cais'}
        # query = urllib.urlencode(params)
        # r = urllib.urlopen(dest + domain + 'recive', query)
        # contents = r.read()
        # r.close()
        return '''<h1>msgEnc: {}</h1>
                  <h1>url: {}</h1>'''.format(encrypted, responseKey)

    return '''<form method="POST">
                  Para: <input type="text" name="dest"><br>
                  Sua mensagem: <input type="text" name="msg"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


@app.route('/query-example')
# def query_example():
#     language = request.args.get('language') #if key doesn't exist, returns None
#     framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
#     website = request.args.get('website')

@app.route('/getpub')
def mostrar_public():
    return pubKey.exportKey()
    # return '<p name="pub">{}</p>'.format(publicKey)

# @app.route('/teste',  methods = ['POST', 'GET'])
# def test():
#     response = request.get(http://165.227.125.49:3001/contas)
#     return response



# @app.route('/send', methods = ['POST', 'GET'])
# def send():
#     if request.method == "POST":
#         url, keyUser = getpub(input('Destinatario: '))
#         msg = input('msg: ')
#         encrypted = keyUser.encrypt(msg)
#         request.post({'user', encrypted, 'Cais'})

#     return "OK"



@app.route('/recive')
def recive():
    res = request.json
    file = open('logsMsg.txt','w')
    file.write(privateKey.decrypt(msg))
    return



@app.route('/log')
def log():
    file = open('logsMsg.txt','r')
    logs = file.readlines()
    return logs
