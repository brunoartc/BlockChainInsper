
# A very simple Flask Hello World app for you to get started with...
# import os
from flask import Flask, request
from Crypto.PublicKey import RSA

app = Flask(__name__)

publicKey = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuaezfjIlHqo3VkKGLDI3SNJ1QmhnfpN0ngYYqn3bS1Llsva768wmu2vXM5qQUhBW49U91tLOj/r//QOPOtneu+9819dH02yO5ThTUc/d7xihVKpLDF8FpGVh6VKPg/78mFtIQ7J/d1pVfqCRTcXuMOEet4MjKgbGjOZlvcnSDO/t68UdSBpe3U4zBR2YsMfTmcUWmVQl4g1MAWGpINfpmB6vlIt6EXxNfpeVh+NBS9KXJJiYumkm+5q7sjd+YvRfGmRpewPNP8vcuVSil6eMyfsIkIG4MvPoszbKxTIhhO8OLvn2gk15Q4okAHVVg3n9fSXaTy/24OM8fV6aJ/mvEwIDAQAB'
privateKey = 'MIIEpQIBAAKCAQEAuaezfjIlHqo3VkKGLDI3SNJ1QmhnfpN0ngYYqn3bS1Llsva768wmu2vXM5qQUhBW49U91tLOj/r//QOPOtneu+9819dH02yO5ThTUc/d7xihVKpLDF8FpGVh6VKPg/78mFtIQ7J/d1pVfqCRTcXuMOEet4MjKgbGjOZlvcnSDO/t68UdSBpe3U4zBR2YsMfTmcUWmVQl4g1MAWGpINfpmB6vlIt6EXxNfpeVh+NBS9KXJJiYumkm+5q7sjd+YvRfGmRpewPNP8vcuVSil6eMyfsIkIG4MvPoszbKxTIhhO8OLvn2gk15Q4okAHVVg3n9fSXaTy/24OM8fV6aJ/mvEwIDAQABAoIBACUbctHXXfn6FaNlGoI86zXf8tX6Hi17dYScPVPeYfV1NToG/NqNbHRrgpDq5MuyPlu9ZGXKrsSya3X7vyYJI+62WGKfwdhtS0Zfcq/Yd0hxyNUuUF/BolQQe3hyKwM79OrS2+fEBpwpbwsnNsOvuwMEC+qsCFw/DHJfHpjHfPdeqiumFug/ASfgk7AZLf1zDddal3mrmLsAm/ey6gpaZMGf7z0si2sjEjqdDnnS/ZqJHY7joeABK3OXsavkRuh2v+epuqkHM4KRE+G7fNyB+19xQRaEHRT5CrNfNZB/2daX/NJJBvFob5mLAbC+KoFWPPQ7KD2+FUtaUaV49w5RMmkCgYEA1sIwm8c4Xayk0DBgItOfXA3/6ssKT+dcXy6JasbSZEElLel+vPzvywKrt+1ZAiEiWvg6dHoyf8aFgWEHAnFCpDo5yeGawlgkrHxBGf2xb1BNQsfHziuMUuxMh3aEG/EtCl0y0j+/8hdhZYDILIn0mvhrJBWiuzVA+D4kZoaUUPUCgYEA3U6/KI31ik82nZ/HpA1o+WyIAN0Z2Uo59uvr2cuUibKUuTVm+pH9JrHMERBgyWMxsG/3A+nZmQX/9ZdA9pWhsnbBkih4pbabZRt+Tru3TgNUrt00L58eQ6qyMaVO0aQ3hZAxZSLEivHeYGvctFlUAygcUn8UvzCEe3sdvG3k2ucCgYEAsJbTI3TIK3anuyzcECcVNbupQOad3yAuO3Hnuu4r2BYdPUhvV3Vgs/zJOJ8o/nBCcK0GW/qTBbA23TDsc5ywIJxkIlWpTL7vwQkW+wk5Wn+cWBoweJ4kb5cwQn84mEVTNN93x5x199oz0yP29XCmurskVnKX8foTJ0zp34gv8vUCgYEA2g/9y7gVeXMUHbySutN73ElUuYUjMzgwZV2Rx8kRU5zjbptwHPY8uyP2L9ozhDx5eaDZhMGn52BCFXw0RsSpz2+0zI+UUbTc6YNtsabFt9kQWD0ebs4axBIuAz0frPJiwviRs1XO1Bn/RIMDtbFPVszvG1qc1sa3w/RMGJ8wIYECgYEAtAN8JbnK1jK8ap4OkSnQljiyytEjP5YpWVqWDsb4wc0mCsjoAixhp9TyFMN2xgtFFFWJT0BbE3d7J0B14E2BPfZSaxCUV/AF/ojHFFOON+DVbJ6ymC8hptGHQK+We6N+ak5aY15cx/xjgP7JwjmuXOcX1LDY0+vdvxZqqpqWHCg='

@app.route('/hello<name>')
def hello(name):
    return 'Hello %s' % name

@app.route('/getpub')
def mostrar_public():
    return publicKey
    
    
    
    
def getpub(user):
    url = user + 'pythonanywhere.com/recive'
    keyUser = request.get(url)
    return url, keyUser    
    

@app.route('/send<user><msg><eu>', methods = ['POST', 'GET'])
def send():
    
    url, keyUser = getpub('user')
    msg = 'Hardcodei essa msg, so vai te ela'
    encrypted = keyUser.encrypt(msg)
    request.method == 'POST'
    request.post({'user', encrypted, 'Cais'})
    return "OK"






@app.route('/recive')
def recive():
    file = open('logsMsg.txt','w')
    file.write(privateKey.decrypt(msg))
    return




@app.route('/log')
def log():
    file = open('logsMsg.txt','r')
    logs = file.readlines()
    return logs





