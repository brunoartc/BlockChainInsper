#!/usr/bin/python
import random

# chave ex (141837, 153721) (193429, 153721)
# n (eg) 223*761 = 169703

def mmc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multInver(e, phi): 
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def caracts():
    frase = input("Frase: ")
    fraseAsc = []
    for c in frase:
        fraseAsc.append(ord(c))
    return fraseAsc

def criarKeys(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    h = mmc(e, phi)
    while h != 1 & e < phi:
        e = random.randrange(e, phi)
        h = mmc(e, phi)
    d = multInver(e, phi)
    print ((e, n), (d, n))
    return (n, e ,d)

def encrypt(keyE, n):
    mSent = caracts()
    mCryp = []
    for t in mSent:
        mCryp.append(t**keyE%n)
    print mCryp
    return mCryp

def decrypt(keyD, n, m):
    mRecebida = m
    mensagem = ""
    for g in mRecebida:
        mensagem = mensagem + chr((g**keyD)%n)
    print mensagem
    return mensagem


def main():
    p = input("1 primo:")
    q = input("2 primo:")
    n, e, d = criarKeys(p,q)
    m = encrypt(e, n)
    decrypt(d, n, m)

main()

