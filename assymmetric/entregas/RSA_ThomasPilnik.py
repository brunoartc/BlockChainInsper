# -*- coding: utf-8 -*-
#author: Thomas Pilnik
#função de geração de números primos: Joe James
#função de geração de coprimos: Jim Fasarakis Hilliard

from random import *
import random
import numpy as np
from math import gcd as bltin_gcd

def toASCII(texto):
    asciiList=[]
    for i in texto:
        asciiList.append(ord(i))
    back2string=''.join(map(str,asciiList))
    return asciiList

def backFromASCII(palavra):
    word=chr(palavra)
    return word

def encrypt(publickey,multiplicacao):
    encryptedList=[]
    m=toASCII(texto)
    for i in m:
        c=int(i)**publickey
        resto=c%multiplicacao
        encryptedList.append(resto)
    return encryptedList

def decrypt(privatekey, lista_mensagem, multiplicacao):
    decryptedList=[]
    textList=[]
    for i in lista_mensagem:
        conv1=int(i)**privatekey
        m=conv1%multiplicacao
        decryptedList.append(m)
    for h in decryptedList:
        text=backFromASCII(h)
        textList.append(text)
    back2string=''.join(map(str,textList))
    return back2string

def primeGenerator(n):
    primeList=[]
    max=n
    for i in range(2,max+1):
        isPrime=True
        for h in range(2,int(i**0.5)+1):
            if i%h==0:
                isPrime=False
        if isPrime:
            primeList.append(i)
    return primeList

def timesGenerator():
    limit=primeGenerator(1000)
    while True:
        p=random.choice(limit)
        q=random.choice(limit)
        if abs(p-q)>20:
            n=p*q
            break
        else:
            continue
    return n,p,q

def coprime(a, b):
    return bltin_gcd(a, b) == 1

def publicKeyGenerator():
    n,p,q=timesGenerator()
    phi=(p-1)*(q-1)
    while True:
        e=round(np.random.uniform(2,phi))
        if coprime(phi,e) == True:
            if coprime(n,e) == True:
                break
        else: continue
    return e, n

def privateKeyGenerator():
    e,n=publicKeyGenerator()
    while True:
        d=randrange(e,5*e)
        if (e*d)%n==1:
            break
        else: continue
    return d

task=str(input("Para enviar mensagem, pressione E; para receber, pressione R "))

if task=='E' or task=='e':
    texto=str(input("Qual mensagem você quer enviar pro Toranja? "))
    publickey=int(input("Digite a chave pública: "))
    multiplicacao=int(input("Digite a multiplicação dos números primos: "))
    mensagem=encrypt(publickey,multiplicacao)
    print("A sua mensagem encriptada é:\n\n{}".format(mensagem))

elif task=='R' or task=='r':
    decision=str(input("A mensagem já está encriptada? S/N "))
    if decision=="S" or decision=="s":
        texto=str(input("Digite a mensagem encriptada: "))
        privatekey=str(input("Digite a Private Key: "))
        multiplicacao=int(input("Digite a multiplicação dos números primos: "))
        mensagem=decrypt(privatekey,texto,multiplicacao)
        mensa
    elif decision=="N" or decision=="n":
        n,x,y=timesGenerator()
        d,e=publicKeyGenerator()
        print("Salve as informações abaixo. A chave privada não deve ser compartilhada!\n\n")
        print("Essa é sua chave pública: {}".format(d))
        print("Essa é sua chave privada: {}".format(privateKeyGenerator()))
        print("Essa é a multiplicação dos números primos: {}\n\n".format(n))
        texto=str(input("Digite a mensagem encriptada: "))
        privatekey=int(input("Digite a Private Key: "))
        multiplicacao=int(input("Digite a multiplicação dos números primos: "))
        mensagem=decrypt(privatekey,texto,multiplicacao)
    print("Sua mensagem descriptada é: {}".format(mensagem))
