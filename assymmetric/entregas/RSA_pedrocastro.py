#!/usr/bin/python

# chave (141837, 153721) (193429, 153721)

def caracts():
    frase = input("Frase: ")
    fraseAsc = []
    for c in frase:
        fraseAsc.append(ord(c))
    return fraseAsc

def encrypt(keyE, n):
    mSent = caracts()
    mCryp = []
    for t in mSent:
        mCryp.append(t**keyE%n)
    print mCryp
    return mCryp

def decrypt(keyD, n):
    mRecebida = []
    mensagem = ""
    for g in mRecebida:
        mensagem = mensagem + chr((g**keyD)%n)
    print mensagem
    return mensagem

encrypt(141837, 153721)
decrypt(193429, 153721)
